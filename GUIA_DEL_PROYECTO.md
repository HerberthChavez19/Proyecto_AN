# Guía del Proyecto
## Limpieza de Audio mediante Transformada Rápida de Fourier (FFT)

Este documento explica en detalle qué hace cada parte del proyecto, cómo están organizados los archivos y cuál es el flujo completo de procesamiento. Está escrito para que cualquier persona pueda entender el proyecto, incluso si no tiene experiencia programando.

---

## 1. ¿De qué trata este proyecto?

El proyecto demuestra cómo la **Transformada Rápida de Fourier (FFT)** puede usarse para analizar señales de audio, detectar ruido y limpiarlo matemáticamente.

La idea central es la siguiente: una señal de audio es una mezcla de muchas frecuencias sonando al mismo tiempo. La FFT nos permite "desempacar" esa mezcla y ver exactamente qué frecuencias están presentes. Una vez que las vemos, podemos eliminar las que no queremos (el ruido) y reconstruir la señal limpia.

El ciclo completo del proyecto es:

```
Audio con ruido
      ↓
  Aplicar FFT          (dominio temporal → dominio frecuencial)
      ↓
  Identificar ruido    (buscar picos indeseados en el espectro)
      ↓
  Aplicar filtro       (poner esas frecuencias en cero)
      ↓
  Aplicar IFFT         (dominio frecuencial → dominio temporal)
      ↓
  Audio limpio
```

---

## 2. Estructura del proyecto

```
Proyecto_AN/
│
├── README.md                   ← Descripción general y objetivos del proyecto
├── GUIA_DEL_PROYECTO.md        ← Este archivo
├── requirements.txt            ← Lista de librerías necesarias
├── setup.sh                    ← Script para preparar el entorno automáticamente
│
├── data/
│   ├── raw/                    ← Audios originales sin modificar
│   │   ├── voz.wav             ← Grabación de voz hecha por los integrantes
│   │   └── PruebaAN.wav        ← Audio sintético generado en el notebook 01
│   └── processed/              ← Audios ya filtrados o procesados
│       ├── voz_arruinada.wav
│       ├── voz_rescatada.wav
│       ├── arcaico_ruidoso.wav
│       ├── arcaico_limpio.wav
│       ├── prueba_pasa_bajas_ruido.wav
│       ├── prueba_pasa_bajas_limpio.wav
│       ├── prueba_pasa_altas_ruido.wav
│       ├── prueba_pasa_altas_limpio.wav
│       ├── 1_audio_con_zumbido.wav
│       └── 2_audio_limpio_fft.wav
│
├── notebooks/                  ← Experimentos interactivos paso a paso
│   ├── 01_exploracion.ipynb
│   ├── 02_fft.ipynb
│   ├── 03_filtrado.ipynb
│   ├── 04_evaluacion.ipynb
│   └── demostracionFinal.ipynb
│
├── src/                        ← Código reutilizable del proyecto
│   ├── __init__.py
│   ├── audio_loader.py
│   ├── fft_utils.py
│   ├── filters.py
│   ├── metrics.py
│   └── visualization.py
│
├── tests/                      ← Pruebas automáticas
│   ├── test_filters.py
│   └── test_spectral_analysis.py
│
└── figures/                    ← Carpeta para guardar gráficas exportadas
```

---

## 3. Módulos de código (`src/`)

La carpeta `src/` contiene el código organizado por responsabilidad. Cada archivo tiene una función específica y puede ser reutilizado desde cualquier notebook.

---

### `audio_loader.py`

**¿Qué hace?** Carga un archivo de audio desde el disco y lo convierte en un arreglo de números que Python puede procesar.

**Función principal:** `load_audio(file_path)`

- Recibe la ruta de un archivo de audio (`.wav` u otros formatos compatibles).
- Usa la librería **Librosa** para leerlo.
- Devuelve dos cosas:
  - `signal` → un arreglo de números que representa la amplitud de la onda a lo largo del tiempo.
  - `sample_rate` → la frecuencia de muestreo del audio (cuántas muestras por segundo, típicamente 44,100 Hz).

**Ejemplo de uso:**
```python
from src.audio_loader import load_audio

signal, sample_rate = load_audio("data/raw/voz.wav")
```

---

### `fft_utils.py`

**¿Qué hace?** Aplica la Transformada de Fourier a una señal de audio para convertirla al dominio frecuencial, y también reconstruye la señal a partir de su espectro.

**Funciones:**

#### `calcular_fft(signal, sample_rate)`
- Recibe la señal de audio y su frecuencia de muestreo.
- Calcula la FFT usando SciPy (altamente optimizada).
- Devuelve solo la **mitad positiva** del espectro, porque la FFT de señales reales produce un resultado simétrico y la parte negativa es redundante.
- Devuelve:
  - `frecuencias` → el eje X del espectro (valores en Hz).
  - `magnitud` → el eje Y del espectro (qué tan intensa es cada frecuencia).

#### `reconstruir_senal(spectrum)`
- Recibe el espectro (modificado o no por un filtro).
- Aplica la **IFFT** (Transformada Inversa) para regresar al dominio temporal.
- Devuelve solo la parte real de la señal, descartando residuos imaginarios mínimos que aparecen por precisión numérica.

**Ejemplo de uso:**
```python
from src.fft_utils import calcular_fft, reconstruir_senal

frecuencias, magnitud = calcular_fft(signal, sample_rate)
senal_reconstruida = reconstruir_senal(espectro_filtrado)
```

---

### `filters.py`

**¿Qué hace?** Aplica máscaras frecuenciales al espectro para eliminar componentes no deseadas. Contiene tres tipos de filtros.

Todos los filtros funcionan sobre el mismo principio: reciben el espectro complejo de la FFT, identifican qué frecuencias deben eliminarse y las ponen en cero. Luego el espectro modificado puede pasarse a `reconstruir_senal` para obtener el audio limpio.

---

#### `apply_notch_mask(spectrum, center_hz, bandwidth_hz, sample_rate)`

Elimina una **frecuencia específica** y un pequeño rango a su alrededor.

| Parámetro | Descripción |
|---|---|
| `spectrum` | El espectro resultante de la FFT |
| `center_hz` | La frecuencia central a eliminar (ej. 60.0 para zumbido eléctrico) |
| `bandwidth_hz` | El ancho del rango a borrar (ej. 2.0 Hz alrededor del centro) |
| `sample_rate` | La frecuencia de muestreo del audio |

**Cuándo usarlo:** cuando el ruido está concentrado en una frecuencia muy precisa, como el zumbido de 50/60 Hz de la red eléctrica, o un pitido de tono fijo.

---

#### `apply_lowpass_mask(spectrum, cutoff_hz, sample_rate)`

Elimina todas las frecuencias **por encima** del punto de corte. Deja pasar solo las frecuencias bajas.

| Parámetro | Descripción |
|---|---|
| `spectrum` | El espectro resultante de la FFT |
| `cutoff_hz` | La frecuencia de corte (ej. 1000.0 Hz — todo lo mayor a esto se borra) |
| `sample_rate` | La frecuencia de muestreo del audio |

**Cuándo usarlo:** cuando el ruido es agudo (alta frecuencia), como el siseo de una radio o interferencia electrónica de alta frecuencia.

---

#### `apply_highpass_mask(spectrum, cutoff_hz, sample_rate)`

Elimina todas las frecuencias **por debajo** del punto de corte. Deja pasar solo las frecuencias altas.

| Parámetro | Descripción |
|---|---|
| `spectrum` | El espectro resultante de la FFT |
| `cutoff_hz` | La frecuencia de corte (ej. 500.0 Hz — todo lo menor a esto se borra) |
| `sample_rate` | La frecuencia de muestreo del audio |

**Cuándo usarlo:** cuando el ruido es grave (baja frecuencia), como vibraciones de fondo, ruidos de motor o componentes DC que desplazan la señal.

---

### `metrics.py`

**¿Qué hace?** Calcula métricas numéricas para evaluar qué tan bien funcionó el filtrado. Compara la señal ideal (sin ruido) con la señal que obtuvimos después de filtrar.

**Funciones:**

#### `mean_squared_error(reference, estimate)`
Calcula el **Error Cuadrático Medio (MSE)**. Mide la diferencia promedio entre dos señales elevada al cuadrado.
- Un MSE de **0** significa que las señales son idénticas.
- Un MSE más **cercano a 0** indica mejor calidad de filtrado.

#### `signal_to_noise_ratio(reference, estimate)`
Calcula la **Relación Señal-Ruido (SNR)** en decibeles (dB). Mide qué tan fuerte es la señal útil comparada con el ruido residual.
- Valores **más altos** indican mejor calidad.
- Por encima de 20 dB se considera una señal notablemente más fuerte que el ruido.

---

### `visualization.py`

**¿Qué hace?** Proporciona funciones reutilizables para graficar señales y espectros con Matplotlib, sin necesidad de escribir el código de la gráfica desde cero en cada notebook.

**Funciones:**

#### `plot_time_domain(signal, sample_rate, title)`
Grafica la señal en el **dominio temporal** (amplitud vs. tiempo). Genera automáticamente el eje de tiempo a partir de la frecuencia de muestreo.

#### `plot_frequency_domain(frequencies, magnitude, title, xlim)`
Grafica el **espectro de frecuencias** (magnitud vs. Hz). Acepta un parámetro `xlim` opcional para hacer zoom en un rango específico de frecuencias.

---

## 4. Notebooks (`notebooks/`)

Los notebooks son el espacio de experimentación del proyecto. Cada uno cubre una fase del desarrollo y contiene tanto el código como explicaciones en texto.

---

### `01_exploracion.ipynb` — Fase 1: Carga y visualización

**¿Qué hace?**
1. Crea un audio sintético de prueba: un tono puro de 440 Hz mezclado con un zumbido de 60 Hz y ruido blanco. Lo guarda en `data/raw/PruebaAN.wav`.
2. Carga el audio usando `audio_loader.py`.
3. Muestra información básica: frecuencia de muestreo, número de muestras, duración, amplitud mínima y máxima.
4. Grafica la señal en el dominio temporal.

**¿Por qué crear un audio sintético?** Porque al construirlo nosotros mismos sabemos exactamente qué frecuencias contiene. Eso nos permite verificar que la FFT y los filtros funcionan correctamente en las siguientes fases.

---

### `02_fft.ipynb` — Fase 2: Análisis espectral

**¿Qué hace?**
1. Carga el audio sintético generado en la fase anterior.
2. Aplica la FFT usando `fft_utils.py`.
3. Grafica el espectro de frecuencias haciendo zoom en el rango 0–1,000 Hz.

**¿Qué se observa?** Dos picos muy claros: uno exacto en 60 Hz (el zumbido que inyectamos) y otro en 440 Hz (la nota La). También se ven pequeñas irregularidades al ras del suelo que representan el ruido blanco aleatorio.

---

### `03_filtrado.ipynb` — Fase 3: Filtrado con Notch

**¿Qué hace?**
1. Carga el audio sintético.
2. Aplica la FFT para obtener el espectro.
3. Aplica el filtro **Notch en 60 Hz** usando `filters.py` para eliminar el zumbido eléctrico.
4. Grafica el espectro antes y después del filtro en una comparación lado a lado.
5. Aplica la IFFT para reconstruir el audio limpio.
6. Exporta ambos audios (con y sin zumbido) a `data/processed/`.

---

### `04_evaluacion.ipynb` — Fase 4: Evaluación con métricas

**¿Qué hace?**
1. Carga el audio con zumbido y el audio filtrado desde `data/processed/`.
2. Genera matemáticamente la señal ideal (tono puro de 440 Hz, sin ningún ruido).
3. Calcula el **MSE** y el **SNR** comparando la señal ideal contra:
   - el audio con zumbido (antes del filtro)
   - el audio filtrado (después del filtro)
4. Imprime el reporte final de métricas.

**Resultados típicos obtenidos:**

| Métrica | Antes del filtro | Después del filtro |
|---|---|---|
| SNR | 3.56 dB | 10.97 dB |
| MSE | 0.055056 | 0.009990 |

El SNR casi se triplica y el MSE cae a una quinta parte, lo que confirma numéricamente que el filtrado mejoró significativamente la calidad de la señal.

---

### `demostracionFinal.ipynb` — Demostración completa

Este es el notebook principal de presentación. Reúne todo el proyecto en acción con tres demostraciones:

#### Demo 1: Prueba con voz real
- Carga una grabación de voz de los integrantes (`data/raw/voz.wav`).
- Inyecta un pitido artificial de **800 Hz** para simular interferencia.
- Guarda el audio arruinado.
- Aplica un filtro Notch en 800 Hz para eliminar el pitido.
- Guarda el audio rescatado.
- Muestra una gráfica comparativa del espectro antes y después del filtro.

#### Demo 2: DFT manual (método arcaico)
Implementa la Transformada Discreta de Fourier **desde cero**, sin usar librerías, con dos bucles anidados. Esto muestra cómo funciona la matemática por dentro.

- Crea un micro-audio de solo 1,000 muestras para que sea computable (un segundo real con 44,100 muestras tardaría horas).
- Aplica la DFT manual para ir al dominio frecuencial.
- Elimina manualmente la frecuencia de ruido borrando índices específicos del espectro.
- Aplica la IDFT manual para reconstruir el audio.
- **Benchmark:** compara el tiempo de ejecución de la DFT manual O(N²) vs la FFT O(N log N) con 2,000 muestras. Resultado típico: la FFT es más de **1,600 veces más rápida**.

#### Demo 3: Filtros Pasa-Bajas y Pasa-Altas
Demuestra los otros dos tipos de filtros implementados en el proyecto:

**Pasa-Bajas:**
- Señal útil: 440 Hz + ruido agudo de 5,000 Hz.
- Corte en 1,000 Hz — todo lo mayor a eso se elimina.
- El pico de 5,000 Hz desaparece completamente.

**Pasa-Altas:**
- Señal útil: 3,000 Hz + ruido grave (rumble) de 80 Hz.
- Corte en 500 Hz — todo lo menor a eso se elimina.
- El pico de 80 Hz desaparece completamente.

---

## 5. Pruebas automáticas (`tests/`)

Las pruebas automáticas verifican matemáticamente que el código funciona correctamente, sin necesidad de escuchar el audio ni revisar gráficas manualmente. Si alguien modifica el código y rompe algo sin darse cuenta, las pruebas lo detectan de inmediato.

Para correr las pruebas:
```bash
python tests/test_filters.py
python tests/test_spectral_analysis.py
```

---

### `test_filters.py` — 6 pruebas

| Prueba | Qué verifica |
|---|---|
| `test_notch_elimina_frecuencia_objetivo` | El filtro Notch reduce a casi cero la frecuencia que debe eliminar |
| `test_notch_conserva_frecuencias_fuera_de_banda` | El Notch no afecta frecuencias fuera de su banda |
| `test_lowpass_elimina_frecuencias_altas` | El pasa-bajas lleva a cero las frecuencias sobre el corte |
| `test_lowpass_conserva_frecuencias_bajas` | El pasa-bajas no modifica las frecuencias bajo el corte |
| `test_highpass_elimina_frecuencias_bajas` | El pasa-altas lleva a cero las frecuencias bajo el corte |
| `test_highpass_conserva_frecuencias_altas` | El pasa-altas no modifica las frecuencias sobre el corte |

### `test_spectral_analysis.py` — 6 pruebas

| Prueba | Qué verifica |
|---|---|
| `test_fft_devuelve_solo_mitad_positiva` | `calcular_fft` devuelve exactamente N/2 puntos |
| `test_fft_frecuencias_son_positivas` | El eje de frecuencias no tiene valores negativos |
| `test_fft_detecta_frecuencia_dominante` | El pico máximo cae en la frecuencia correcta |
| `test_reconstruir_devuelve_senal_real` | `reconstruir_senal` no devuelve números imaginarios |
| `test_reconstruir_conserva_longitud` | La señal reconstruida tiene el mismo número de muestras |
| `test_reconstruir_aproxima_senal_original` | El error de reconstrucción es menor a 1×10⁻¹⁰ |

---

## 6. Librerías utilizadas

| Librería | Para qué se usa |
|---|---|
| **NumPy** | Representación de señales como arreglos numéricos y operaciones matemáticas |
| **SciPy** | Cálculo de FFT e IFFT con algoritmos optimizados |
| **Matplotlib** | Generación de todas las gráficas del proyecto |
| **Librosa** | Carga de archivos de audio en diferentes formatos |
| **SoundFile** | Exportación de audios procesados a formato WAV |
| **Jupyter** | Entorno de notebooks interactivos |

---

## 7. Cómo preparar el entorno

```bash
# Opción 1: usando el script automático
./setup.sh

# Opción 2: manualmente
python -m venv .venv
source .venv/bin/activate       # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## 8. Flujo completo resumido

```
[Archivo de audio]
        ↓
  audio_loader.py          → carga el audio como arreglo NumPy
        ↓
  fft_utils.calcular_fft   → transforma al dominio frecuencial
        ↓
  visualization.py          → gráfica el espectro para identificar el ruido
        ↓
  filters.py               → aplica notch / pasa-bajas / pasa-altas
        ↓
  fft_utils.reconstruir    → regresa al dominio temporal (IFFT)
        ↓
  metrics.py               → calcula MSE y SNR para evaluar la mejora
        ↓
[Audio limpio exportado]
```
