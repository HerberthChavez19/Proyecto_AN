"""Base para filtros en el dominio frecuencial.

Este módulo será usado en la Fase 3 para prototipos de filtros simples como:

- pasa bajas,
- pasa altas,
- notch.

La versión inicial solo reserva el espacio para futuras implementaciones.
"""

import numpy as np

def apply_notch_mask(spectrum: np.ndarray, center_hz: float, bandwidth_hz: float, sample_rate: int) -> np.ndarray:
    """
    Aplica una máscara notch para atenuar una frecuencia específica en el dominio frecuencial.
    
    Parameters
    ----------
    spectrum: np.ndarray
        El arreglo de números complejos resultante de aplicar la FFT.
    center_hz: float
        La frecuencia central que deseamos eliminar (ej. 60.0 Hz).
    bandwidth_hz: float
        El ancho de banda a borrar alrededor de la frecuencia central (ej. 2.0 Hz).
    sample_rate: int
        Frecuencia de muestreo del audio original.

    Returns
    -------
    np.ndarray
        El espectro de frecuencias modificado (con la máscara aplicada).
    """
    # 1. Obtenemos el número total de muestras
    N = len(spectrum)
    
    # 2. Reconstruimos el eje de frecuencias exacto de la FFT
    freqs = np.fft.fftfreq(N, 1 / sample_rate)
    
    # 3. Copiamos el espectro para no modificar el original
    espectro_filtrado = spectrum.copy()
    
    # 4. Definimos los límites superior e inferior de lo que vamos a borrar
    limite_inf = center_hz - (bandwidth_hz / 2)
    limite_sup = center_hz + (bandwidth_hz / 2)
    
    # 5. Buscamos los índices de las frecuencias no deseadas. 
    # Usamos np.abs(freqs) porque la FFT de señales reales produce 
    # un espectro simétrico (los 60 Hz existen en positivo y en negativo).
    mascara = (np.abs(freqs) >= limite_inf) & (np.abs(freqs) <= limite_sup)
    
    # 6. ¡Magia frecuencial! Multiplicamos esas frecuencias por 0
    espectro_filtrado[mascara] = 0.0
    
    return espectro_filtrado


def apply_lowpass_mask(spectrum: np.ndarray, cutoff_hz: float, sample_rate: int) -> np.ndarray:
    """
    Aplica una máscara pasa-bajas para atenuar todas las frecuencias por encima de un corte.
    
    Parameters
    ----------
    spectrum: np.ndarray
        El espectro resultante de aplicar la FFT.
    cutoff_hz: float
        La frecuencia a partir de la cual se borrará todo (ej. 3000.0 Hz).
    sample_rate: int
        Frecuencia de muestreo del audio.

    Returns
    -------
    np.ndarray
        El espectro con las frecuencias altas eliminadas a cero.
    """
    N = len(spectrum)
    freqs = np.fft.fftfreq(N, 1 / sample_rate)
    espectro_filtrado = spectrum.copy()
    
    # Buscamos las frecuencias que sean MAYORES al punto de corte 
    # (Usamos abs() para afectar la parte positiva y negativa del espectro)
    mascara_altas = np.abs(freqs) > cutoff_hz
    
    # Eliminamos esas frecuencias altas poniéndolas en cero
    espectro_filtrado[mascara_altas] = 0.0
    
    return espectro_filtrado

