"""Funciones de visualización para audio y espectros.

Este módulo se usará para la Fase 1, Fase 2 y Fase 6:

- graficar señal temporal,
- graficar espectro de magnitud,
- comparar señal original y señal filtrada.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt


def plot_time_domain(signal: np.ndarray, sample_rate: int, title: str = "Señal de audio en el dominio temporal") -> None:
    """Grafica la señal en el dominio temporal."""
    time_axis = np.arange(len(signal)) / sample_rate

    plt.figure(figsize=(12, 4))
    plt.plot(time_axis, signal, linewidth=0.8)
    plt.title(title)
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Amplitud")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_frequency_domain(frequencies: np.ndarray, magnitude: np.ndarray, title: str = "Espectro de Frecuencias", xlim: float | None = None) -> None:
    """Grafica el espectro de magnitud de una señal."""
    plt.figure(figsize=(12, 4))
    plt.plot(frequencies, magnitude, color="darkorange", linewidth=1)
    plt.title(title)
    plt.xlabel("Frecuencia [Hz]")
    plt.ylabel("Magnitud")
    if xlim is not None:
        plt.xlim(0, xlim)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
