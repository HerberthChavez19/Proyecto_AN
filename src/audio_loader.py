"""
Utilidades iniciales para cargar y explorar archivos de audio.

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
#Librosa es una biblioteca popular para el procesamiento de audio en Python.
import librosa


def load_audio(file_path: str | Path) -> Tuple[np.ndarray, int]:
    """
    Carga un archivo de audio y devuelve la señal y su frecuencia de muestreo.
    Parameters
    ----------
    file_path:
        Ruta del archivo de audio.
    Returns
    -------
    tuple[np.ndarray, int]
        Señal de audio y frecuencia de muestreo.
    """
    
    # Convertimos a string en caso de que entre un objeto Path
    path_str = str(file_path)
    
    # Cargamos el audio manteniendo su frecuencia de muestreo original y en mono
    signal, sample_rate = librosa.load(path_str, sr=None, mono=True)
    
    return signal, sample_rate

