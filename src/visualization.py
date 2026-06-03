"""Funciones de visualización para audio y espectros.

Este módulo se usará para la Fase 1, Fase 2 y Fase 6:

- graficar señal temporal,
- graficar espectro de magnitud,
- comparar señal original y señal filtrada.
"""

from __future__ import annotations

import numpy as np


def plot_time_domain(signal: np.ndarray, sample_rate: int) -> None:
    """Grafica la señal en el dominio temporal."""
    raise NotImplementedError("La visualización se implementará gradualmente.")


def plot_frequency_domain(frequencies: np.ndarray, magnitude: np.ndarray) -> None:
    """Grafica el espectro de magnitud de una señal."""
    raise NotImplementedError("La visualización se implementará gradualmente.")

