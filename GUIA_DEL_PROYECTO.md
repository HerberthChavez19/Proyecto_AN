# Guía del Proyecto
## Limpieza de Audio mediante Transformada Rápida de Fourier (FFT)

Este documento está pensado para orientar al equipo de trabajo sobre:

- cómo está organizada la estructura del proyecto,
- cómo se planea desarrollar el trabajo por fases,
- qué librerías se necesitan,
- y cuál será el flujo general de colaboración.

La idea es que todos tengamos una referencia clara y simple para avanzar de forma ordenada.

---

## 1. Propósito del proyecto

El proyecto busca estudiar cómo la Transformada Rápida de Fourier (FFT) puede ayudarnos a analizar señales de audio, detectar ruido, aplicar filtros y reconstruir la señal procesada.

No se trata de implementar algoritmos complejos desde cero, sino de construir una base sólida para aprender y demostrar conceptos de Análisis Numérico y DSP con Python.

---

## 2. Estructura del proyecto

La organización actual del repositorio está pensada para que cada parte del trabajo tenga un lugar claro.

```text
proyecto_fft_audio/
├── README.md
├── GUIA_DEL_PROYECTO.md
├── requirements.txt
├── setup.sh
├── .gitignore
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_exploracion.ipynb
│   ├── 02_fft.ipynb
│   ├── 03_filtrado.ipynb
│   └── 04_evaluacion.ipynb
│
├── src/
│   ├── __init__.py
│   ├── audio_loader.py
│   ├── fft_utils.py
│   ├── filters.py
│   ├── visualization.py
│   └── metrics.py
│
├── tests/
└── figures/
```

### ¿Qué hace cada carpeta?

- `data/raw/`: contiene los audios originales que se van a analizar.
- `data/processed/`: guarda los audios ya filtrados o reconstruidos.
- `notebooks/`: espacio de trabajo experimental para desarrollar cada fase.
- `src/`: código reutilizable del proyecto, separado por responsabilidad.
- `tests/`: pruebas futuras para validar funciones importantes.
- `figures/`: gráficas, capturas y resultados visuales.

---

## 3. Cómo planeamos trabajar

La estrategia de trabajo será incremental. Eso significa que iremos construyendo el proyecto paso a paso, sin saltarnos etapas.

### Fase 1: Carga de audio

Objetivo:

- leer archivos WAV,
- obtener frecuencia de muestreo,
- visualizar la señal en el dominio temporal.

Archivos relacionados:

- `src/audio_loader.py`
- `notebooks/01_exploracion.ipynb`

### Fase 2: FFT

Objetivo:

- calcular la transformada de Fourier,
- obtener el espectro de frecuencias,
- empezar a interpretar el contenido de la señal.

Archivos relacionados:

- `src/fft_utils.py`
- `notebooks/02_fft.ipynb`

### Fase 3: Visualización del espectro

Objetivo:

- graficar magnitud y, si es necesario, fase,
- identificar picos de energía y ruido,
- comparar señales en tiempo y frecuencia.

Archivos relacionados:

- `src/visualization.py`
- `notebooks/02_fft.ipynb`

### Fase 4: Filtrado

Objetivo:

- probar filtros simples como pasa bajas, pasa altas y notch,
- reducir componentes no deseadas,
- mantener la señal útil lo mejor posible.

Archivos relacionados:

- `src/filters.py`
- `notebooks/03_filtrado.ipynb`

### Fase 5: Reconstrucción mediante IFFT

Objetivo:

- volver al dominio temporal,
- reconstruir el audio procesado,
- guardar resultados si hace falta.

Archivos relacionados:

- `src/fft_utils.py`
- `data/processed/`

### Fase 6: Comparación de resultados

Objetivo:

- comparar señal original vs. señal filtrada,
- evaluar visualmente y con métricas básicas,
- documentar qué funcionó y qué no.

Archivos relacionados:

- `src/metrics.py`
- `src/visualization.py`
- `notebooks/04_evaluacion.ipynb`

---

## 4. Librerías necesarias

Las dependencias principales del proyecto están en `requirements.txt`.

### Librerías base

- **numpy**: manejo de arreglos y operaciones numéricas.
- **scipy**: herramientas científicas y apoyo para procesamiento de señales.
- **matplotlib**: creación de gráficas.
- **pandas**: organización y análisis de datos tabulares cuando sea necesario.
- **librosa**: carga y análisis de audio.
- **soundfile**: lectura y escritura de archivos de audio.
- **jupyter**: ejecución de notebooks.

### ¿Para qué se usará cada una?

- `numpy`: representación de señales y espectros.
- `scipy`: apoyo en filtrado y operaciones matemáticas.
- `matplotlib`: visualización temporal y frecuencial.
- `pandas`: registrar resultados o comparar experimentos.
- `librosa`: cargar audio fácilmente en notebooks.
- `soundfile`: exportar audios procesados.
- `jupyter`: documentar el proceso de desarrollo paso a paso.

---

## 5. Cómo preparar el entorno

El archivo `setup.sh` automatiza la configuración inicial.

Pasos generales:

```bash
./setup.sh
```

Eso hará lo siguiente:

- crear un entorno virtual `.venv`,
- activarlo,
- actualizar `pip`,
- instalar las dependencias necesarias.

Si alguien prefiere hacerlo manualmente, el flujo sería equivalente a:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

## 6. Convenciones de trabajo

Para mantener el proyecto ordenado, vamos a seguir estas ideas:

- cada fase debe quedar documentada en su notebook correspondiente,
- el código reusable debe vivir en `src/`,
- los audios de prueba deben colocarse en `data/raw/`,
- los resultados procesados deben guardarse en `data/processed/`,
- las gráficas finales deben exportarse en `figures/`,
- antes de cambiar algo importante, conviene revisar si afecta a otra fase.

---

## 7. Qué no se hará por ahora

Para mantener el proyecto manejable en esta etapa inicial:

- no se implementarán filtros avanzados,
- no se buscará una restauración profesional del audio,
- no se construirán modelos complejos de aprendizaje automático,
- no se complicará el código con optimizaciones prematuras.

El foco está en aprender FFT, visualizar correctamente la señal y construir una base limpia para futuras mejoras.

---

## 8. Siguientes pasos sugeridos

1. Colocar uno o más archivos WAV de prueba en `data/raw/`.
2. Empezar a trabajar sobre `notebooks/01_exploracion.ipynb`.
3. Implementar `src/audio_loader.py`.
4. Completar `src/fft_utils.py` con FFT, IFFT y eje de frecuencias.
5. Agregar visualización del espectro.
6. Probar filtros simples en frecuencia.
7. Comparar resultados y documentar hallazgos.

---

## 9. Resumen para el equipo

En pocas palabras, este proyecto se organiza así:

- primero cargamos y entendemos la señal,
- luego la llevamos al dominio de la frecuencia,
- después filtramos el ruido,
- finalmente reconstruimos y comparamos.

Si todos seguimos la misma estructura, el proyecto será más fácil de entender, mantener y presentar.

