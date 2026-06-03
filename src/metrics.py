"""Métricas básicas para evaluar resultados de procesamiento de audio.

Este módulo apoyará la Fase 6 y permitirá comparar:

- error cuadrático medio,
- relación señal-ruido,
- diferencia entre señal original y procesada.
"""

from __future__ import annotations

import numpy as np


def mean_squared_error(reference: np.ndarray, estimate: np.ndarray) -> float:
    """Calcula el error cuadrático medio entre dos señales."""
    raise NotImplementedError("Las métricas se implementarán en la Fase 6.")


def signal_to_noise_ratio(reference: np.ndarray, estimate: np.ndarray) -> float:
    """Calcula una estimación básica de la relación señal-ruido."""
    raise NotImplementedError("Las métricas se implementarán en la Fase 6.")

