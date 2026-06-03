"""Base para filtros en el dominio frecuencial.

Este módulo será usado en la Fase 3 para prototipos de filtros simples como:

- pasa bajas,
- pasa altas,
- notch.

La versión inicial solo reserva el espacio para futuras implementaciones.
"""

from __future__ import annotations

import numpy as np


def apply_lowpass_mask(spectrum: np.ndarray, cutoff_hz: float, sample_rate: int) -> np.ndarray:
    """Aplica una máscara simple pasa bajas en el dominio frecuencial."""
    raise NotImplementedError("El filtrado se implementará en la Fase 3.")


def apply_highpass_mask(spectrum: np.ndarray, cutoff_hz: float, sample_rate: int) -> np.ndarray:
    """Aplica una máscara simple pasa altas en el dominio frecuencial."""
    raise NotImplementedError("El filtrado se implementará en la Fase 3.")


def apply_notch_mask(spectrum: np.ndarray, center_hz: float, bandwidth_hz: float, sample_rate: int) -> np.ndarray:
    """Aplica una máscara notch para atenuar una frecuencia específica."""
    raise NotImplementedError("El filtrado se implementará en la Fase 3.")

