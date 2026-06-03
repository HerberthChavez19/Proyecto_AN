# Proyecto Final - Análisis Numérico
## Limpieza de Audio mediante Transformada Rápida de Fourier (FFT)

Este proyecto desarrolla una aplicación experimental para estudiar el uso de la Transformada Rápida de Fourier (FFT) en el procesamiento digital de audio. El objetivo es analizar señales sonoras en el dominio de la frecuencia, identificar componentes no deseadas y aplicar filtros que permitan mejorar la calidad de la señal reconstruida.

La propuesta se enfoca en un enfoque práctico y progresivo, apoyado en herramientas consolidadas del ecosistema científico de Python, sin implementar la FFT desde cero. En su lugar, se utilizarán bibliotecas como NumPy y SciPy para el análisis numérico, y Matplotlib, Librosa y SoundFile para la carga, visualización y tratamiento de audio.

---

## 1. Descripción general del proyecto

En el dominio temporal, una señal de audio se representa como una variación de amplitud a lo largo del tiempo. Sin embargo, muchas tareas de análisis y limpieza resultan más claras cuando la señal se transforma al dominio frecuencial, donde es posible observar qué frecuencias están presentes, con qué intensidad aparecen y cómo se distribuye la energía espectral.

Este proyecto busca demostrar cómo la FFT permite:

- visualizar el contenido frecuencial de una señal de audio,
- detectar ruido o componentes no deseadas,
- aplicar filtros digitales básicos,
- reconstruir la señal mediante la transformada inversa,
- comparar el audio original con el audio procesado.

El resultado esperado es una herramienta educativa y experimental que conecte los fundamentos del Análisis Numérico con una aplicación concreta de DSP.

---

## 2. Objetivos

### Objetivo general

Desarrollar una aplicación experimental para analizar, filtrar y reconstruir señales de audio mediante FFT e IFFT, con el fin de estudiar su comportamiento en los dominios temporal y frecuencial.

### Objetivos específicos

- Cargar archivos de audio desde diferentes formatos compatibles.
- Visualizar la señal en el dominio temporal.
- Obtener y analizar su espectro de frecuencias mediante FFT.
- Identificar patrones asociados a ruido o interferencia.
- Implementar filtros pasa bajas, pasa altas y notch.
- Reconstruir la señal filtrada mediante IFFT.
- Comparar la señal original y la procesada mediante gráficas y métricas básicas.

---

## 3. Fundamentos teóricos breves

### Dominio temporal y dominio frecuencial

- **Dominio temporal**: muestra cómo cambia la amplitud de la señal a lo largo del tiempo. Es útil para observar duración, forma de onda y eventos transitorios.
- **Dominio frecuencial**: muestra qué frecuencias componen la señal y con qué magnitud aparecen. Es esencial para detectar ruido, armónicos y bandas dominantes.

### DFT

La **Transformada Discreta de Fourier (DFT)** convierte una secuencia discreta de muestras en otra secuencia que representa sus componentes frecuenciales. Matemáticamente, para una señal \(x[n]\) de longitud \(N\):

\[
X[k] = \sum_{n=0}^{N-1} x[n] e^{-j 2\pi kn/N}, \quad k = 0, 1, \dots, N-1
\]

La DFT es la base teórica del análisis espectral digital.

### FFT

La **Transformada Rápida de Fourier (FFT)** no es una transformada distinta, sino un algoritmo eficiente para calcular la DFT. Reduce de manera importante el costo computacional, haciendo viable el análisis de señales largas en tiempos razonables.

### IFFT

La **Transformada Inversa Rápida de Fourier (IFFT)** permite regresar del dominio frecuencial al dominio temporal. Es clave para reconstruir la señal después de aplicar filtros o modificaciones espectrales.

### Frecuencia de muestreo

La frecuencia de muestreo indica cuántas muestras por segundo se toman de una señal analógica para representarla digitalmente. Se expresa en Hz.

- Un valor de 44,100 Hz significa 44,100 muestras por segundo.
- A mayor frecuencia de muestreo, mayor capacidad para representar frecuencias altas.

### Teorema de Nyquist

Para evitar aliasing, la frecuencia de muestreo debe ser al menos el doble de la máxima frecuencia presente en la señal:

\[
f_s \ge 2 f_{max}
\]

La mitad de la frecuencia de muestreo se conoce como **frecuencia de Nyquist**. Todo componente por encima de ese límite puede producir distorsión si no se filtra correctamente.

### Ruido en señales de audio

El ruido es cualquier componente no deseada que altera la señal original. Puede aparecer como:

- zumbido de red eléctrica,
- interferencia de alta frecuencia,
- ruido blanco o impulsivo,
- artefactos de grabación o digitalización.

Identificar el tipo de ruido ayuda a elegir el filtro adecuado.

### Filtros pasa bajas, pasa altas y notch

- **Pasa bajas**: permite el paso de frecuencias bajas y atenúa las altas. Útil para reducir ruido de alta frecuencia.
- **Pasa altas**: permite el paso de frecuencias altas y atenúa las bajas. Útil para eliminar tendencias lentas o componentes graves no deseadas.
- **Notch**: atenúa una frecuencia muy específica o una banda estrecha. Es útil para eliminar el zumbido de 50/60 Hz.

### Importancia de visualizar el espectro

Ver el espectro de frecuencias permite entender de forma inmediata qué está ocurriendo dentro de la señal. En audio, esto es especialmente útil para:

- localizar picos de ruido,
- distinguir señales útiles de interferencias,
- validar el efecto del filtrado,
- evaluar si la reconstrucción conserva la información relevante.

---

## 4. Alcance del proyecto

Este proyecto se desarrollará con un enfoque académico y experimental. Su alcance incluye:

- análisis de audio monofónico o estéreo,
- estudio espectral mediante FFT,
- filtrado básico en frecuencia,
- reconstrucción de la señal procesada,
- comparación visual y cualitativa de resultados.

No se busca construir un sistema profesional de restauración de audio ni implementar filtros adaptativos avanzados. El objetivo principal es comprender y demostrar conceptos matemáticos y numéricos aplicados al procesamiento de señales.

---

## 5. Arquitectura propuesta

La aplicación se organizará de forma modular para facilitar pruebas y extensión futura:

1. **Módulo de entrada**
   - carga de archivos de audio,
   - validación del formato,
   - lectura de frecuencia de muestreo.

2. **Módulo de preprocesamiento**
   - conversión a mono si es necesario,
   - normalización,
   - recorte o segmentación opcional.

3. **Módulo de análisis espectral**
   - cálculo de FFT,
   - obtención de magnitud y fase,
   - generación de eje de frecuencias.

4. **Módulo de filtrado**
   - diseño de máscaras o filtros simples en frecuencia,
   - aplicación de filtros pasa bajas, pasa altas o notch.

5. **Módulo de reconstrucción**
   - aplicación de IFFT,
   - recuperación de la señal filtrada,
   - ajuste de escala si es necesario.

6. **Módulo de visualización y evaluación**
   - gráficas temporal y frecuencial,
   - comparación antes/después,
   - métricas básicas y observaciones.

---

## 6. Tecnologías utilizadas

- **Python 3**: lenguaje principal del proyecto.
- **NumPy**: operaciones numéricas y cálculo de FFT/IFFT.
- **SciPy**: utilidades científicas y apoyo para filtrado.
- **Matplotlib**: visualización de señales y espectros.
- **Librosa**: carga y exploración de audio.
- **SoundFile**: lectura y escritura de archivos de audio.
- **Jupyter Notebook**: desarrollo experimental y documentación interactiva.
- **Git**: control de versiones y seguimiento del avance del proyecto.

---

## 7. Estructura de carpetas recomendada

```text
proyecto_fft_audio/
├── README.md
├── .gitignore
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_carga_visualizacion.ipynb
│   ├── 02_fft_analisis_espectral.ipynb
│   ├── 03_filtros.ipynb
│   └── 04_comparacion_resultados.ipynb
├── src/
│   ├── __init__.py
│   ├── audio_io.py
│   ├── spectral_analysis.py
│   ├── filters.py
│   ├── reconstruction.py
│   └── visualization.py
├── reports/
│   ├── figures/
│   └── notes/
└── tests/
    ├── test_spectral_analysis.py
    └── test_filters.py
```

Esta estructura es sugerida y puede adaptarse según el avance del proyecto y los requerimientos del curso.

---

## 8. Flujo general de procesamiento del audio

1. Cargar el archivo de audio.
2. Obtener la frecuencia de muestreo y el vector de muestras.
3. Visualizar la señal en el dominio temporal.
4. Aplicar FFT para obtener su representación frecuencial.
5. Inspeccionar el espectro para localizar ruido o picos anómalos.
6. Diseñar y aplicar el filtro adecuado.
7. Aplicar IFFT para reconstruir la señal.
8. Comparar señal original vs. señal procesada.
9. Exportar resultados si se requiere.

---

## 9. Posibles experimentos

- Comparar el efecto de diferentes frecuencias de corte en un filtro pasa bajas.
- Evaluar cómo cambia la señal al aplicar un filtro pasa altas.
- Eliminar interferencia de 50 Hz o 60 Hz mediante notch.
- Analizar el impacto de la longitud de la señal en el cálculo de FFT.
- Estudiar la diferencia entre trabajar con audio mono y estéreo.
- Comparar espectros antes y después del filtrado.
- Medir visualmente la reducción de ruido y la preservación de componentes útiles.

---

## 10. Consideraciones matemáticas importantes

- La FFT trabaja sobre muestras discretas, no sobre la señal continua original.
- La resolución en frecuencia depende de la longitud de la señal analizada.
- El eje frecuencial debe construirse correctamente a partir de la frecuencia de muestreo.
- La magnitud del espectro suele analizarse con normalización y, en muchos casos, en escala logarítmica.
- La fase también contiene información importante, especialmente para la reconstrucción.
- Al modificar el espectro, es necesario cuidar la simetría conjugada en señales reales para obtener una señal temporal válida.
- El aliasing puede distorsionar la interpretación espectral si el muestreo es insuficiente.

---

## 11. Riesgos y limitaciones

- La FFT no elimina ruido por sí sola; solo permite analizarlo y diseñar estrategias de filtrado.
- Un filtro mal elegido puede eliminar información útil de la señal.
- La calidad de la reconstrucción depende de la precisión numérica y del diseño del filtrado.
- El audio real puede contener ruido no estacionario, difícil de resolver con filtros simples.
- Si la señal original ya fue grabada con baja calidad, el filtrado puede mejorar solo parcialmente el resultado.
- La percepción subjetiva de mejora no siempre coincide con métricas numéricas simples.

---

## 12. Próximos pasos

- Definir el formato de audio de entrada que se usará en las pruebas.
- Implementar la fase de carga y visualización.
- Construir el análisis espectral con FFT.
- Prototipar filtros en frecuencia.
- Incorporar reconstrucción con IFFT.
- Agregar comparaciones visuales y métricas básicas.
- Documentar cada experimento en notebooks o reportes.

---

## Desarrollo incremental por fases

### Fase 1: Carga y visualización de audio

- Lectura del archivo.
- Exploración de frecuencia de muestreo.
- Gráficas de la señal en el tiempo.

### Fase 2: Aplicación de FFT y análisis espectral

- Cálculo de la FFT.
- Visualización de magnitud y, si aplica, fase.
- Identificación de bandas relevantes y ruido.

### Fase 3: Implementación de filtros

- Diseño de filtros pasa bajas, pasa altas y notch.
- Pruebas sobre segmentos de audio.
- Comparación del espectro antes y después del filtrado.

### Fase 4: Reconstrucción de la señal

- Aplicación de IFFT.
- Generación del audio filtrado.
- Exportación opcional del resultado.

### Fase 5: Comparación y evaluación de resultados

- Gráficas comparativas.
- Revisión auditiva.
- Discusión de ventajas, limitaciones y posibles mejoras.

---

## Referencias conceptuales

- Transformada Discreta de Fourier.
- Transformada Rápida de Fourier.
- Teorema de muestreo de Nyquist-Shannon.
- Procesamiento digital de señales de audio.

---

## Licencia

Este proyecto se desarrolla con fines académicos. La licencia final puede definirse de acuerdo con los lineamientos del curso o del equipo de trabajo.

