"""Funciones base para análisis espectral con FFT e IFFT.

Este módulo servirá como núcleo para la Fase 2 y parte de la Fase 4:

- cálculo de FFT,
- cálculo de IFFT,
- generación del eje de frecuencias.

Por ahora solo se declaran las funciones con documentación y type hints.
"""

# from __future__ import annotations

# from typing import Tuple

# import numpy as np


# def compute_fft(signal: np.ndarray) -> np.ndarray:
#     """Calcula la FFT de una señal 1D.

#     Parameters
#     ----------
#     signal:
#         Vector de muestras en el dominio temporal.

#     Returns
#     -------
#     np.ndarray
#         Espectro complejo de la señal.
#     """
#     raise NotImplementedError("La FFT se implementará en la Fase 2.")


# def compute_ifft(spectrum: np.ndarray) -> np.ndarray:
#     """Calcula la transformada inversa para reconstruir la señal temporal.

#     Parameters
#     ----------
#     spectrum:
#         Espectro complejo modificado en el dominio de la frecuencia.

#     Returns
#     -------
#     np.ndarray
#         Señal reconstruida en el dominio temporal.
#     """
#     raise NotImplementedError("La IFFT se implementará en la Fase 4.")


# def get_frequency_axis(num_samples: int, sample_rate: int) -> np.ndarray:
#     """Construye el eje de frecuencias asociado a una FFT.

#     Parameters
#     ----------
#     num_samples:
#         Número de muestras de la señal.
#     sample_rate:
#         Frecuencia de muestreo en Hz.

#     Returns
#     -------
#     np.ndarray
#         Vector con las frecuencias correspondientes a cada bin espectral.
#     """
#     raise NotImplementedError("El eje de frecuencias se implementará en la Fase 2.")

import numpy as np
from scipy.fft import fft, fftfreq
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

