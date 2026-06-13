"""Funciones base para análisis espectral con FFT e IFFT.

Este módulo servirá como núcleo para la Fase 2 y parte de la Fase 4:

- cálculo de FFT,
- cálculo de IFFT,
- generación del eje de frecuencias.

Por ahora solo se declaran las funciones con documentación y type hints.
"""


import numpy as np
from scipy.fft import fft, ifft, fftfreq
from typing import Tuple

def calcular_fft(signal: np.ndarray, sample_rate: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Calcula la Transformada Rápida de Fourier (FFT) de una señal 1D real.

    Parameters
    ----------
    signal: np.ndarray -> Arreglo con la señal de audio en el dominio temporal.
    sample_rate: int ->Frecuencia de muestreo del audio en Hz.

    Returns
    -------
    tuple[np.ndarray, np.ndarray] -> Arreglo de frecuencias (eje X) y arreglo de magnitudes (eje Y).
    """
    # Número total de muestras
    N = len(signal)
    
    # 1. Calculamos la FFT usando SciPy (que es altamente optimizada)
    yf = fft(signal)
    
    # 2. Calculamos el eje de frecuencias correspondiente
    xf = fftfreq(N, 1 / sample_rate)
    
    # IMPORTANTE: Dado que nuestra señal de audio es un arreglo de números reales, 
    # el resultado de la FFT es simétrico. Para el análisis, solo nos interesa 
    # la mitad positiva del espectro de frecuencias.
    frecuencias_positivas = xf[:N//2]
    
    # Calculamos la magnitud matemática (valor absoluto de los números complejos)
    # y la normalizamos dividiendo por N/2 para que la amplitud coincida con la real.
    magnitud = (2.0 / N) * np.abs(yf[:N//2])
    
    return frecuencias_positivas, magnitud


def reconstruir_senal(spectrum: np.ndarray) -> np.ndarray:
    """
    Reconstruye la señal temporal a partir de su espectro frecuencial (IFFT).

    Parameters
    ----------
    spectrum: np.ndarray
        Arreglo de números complejos resultante de aplicar FFT (y opcionalmente filtros).

    Returns
    -------
    np.ndarray
        Señal reconstruida en el dominio temporal (solo parte real).
    """
    return np.real(ifft(spectrum))

