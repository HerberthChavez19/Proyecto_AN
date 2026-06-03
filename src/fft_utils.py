"""Funciones base para análisis espectral con FFT e IFFT.

Este módulo servirá como núcleo para la Fase 2 y parte de la Fase 4:

- cálculo de FFT,
- cálculo de IFFT,
- generación del eje de frecuencias.

Por ahora solo se declaran las funciones con documentación y type hints.
"""

from __future__ import annotations

from typing import Tuple

import numpy as np


def compute_fft(signal: np.ndarray) -> np.ndarray:
    """Calcula la FFT de una señal 1D.

    Parameters
    ----------
    signal:
        Vector de muestras en el dominio temporal.

    Returns
    -------
    np.ndarray
        Espectro complejo de la señal.
    """
    raise NotImplementedError("La FFT se implementará en la Fase 2.")


def compute_ifft(spectrum: np.ndarray) -> np.ndarray:
    """Calcula la transformada inversa para reconstruir la señal temporal.

    Parameters
    ----------
    spectrum:
        Espectro complejo modificado en el dominio de la frecuencia.

    Returns
    -------
    np.ndarray
        Señal reconstruida en el dominio temporal.
    """
    raise NotImplementedError("La IFFT se implementará en la Fase 4.")


def get_frequency_axis(num_samples: int, sample_rate: int) -> np.ndarray:
    """Construye el eje de frecuencias asociado a una FFT.

    Parameters
    ----------
    num_samples:
        Número de muestras de la señal.
    sample_rate:
        Frecuencia de muestreo en Hz.

    Returns
    -------
    np.ndarray
        Vector con las frecuencias correspondientes a cada bin espectral.
    """
    raise NotImplementedError("El eje de frecuencias se implementará en la Fase 2.")

