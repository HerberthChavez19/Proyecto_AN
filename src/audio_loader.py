"""Utilidades iniciales para cargar y explorar archivos de audio.

Este módulo se usará en la Fase 1 del proyecto para:

- leer archivos WAV y otros formatos compatibles,
- extraer la frecuencia de muestreo,
- obtener la señal como arreglo NumPy,
- preparar los datos para análisis posterior.

La lógica completa se implementará gradualmente.
"""

from __future__ import annotations

from pathlib import Path
from typing import Tuple

import numpy as np


def load_audio(file_path: str | Path) -> Tuple[np.ndarray, int]:
    """Carga un archivo de audio y devuelve la señal y su frecuencia de muestreo.

    Parameters
    ----------
    file_path:
        Ruta del archivo de audio.

    Returns
    -------
    tuple[np.ndarray, int]
        Señal de audio y frecuencia de muestreo.
    """
    raise NotImplementedError("La carga de audio se implementará en la Fase 1.")

