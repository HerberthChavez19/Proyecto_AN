"""Métricas básicas para evaluar resultados de procesamiento de audio.

Este módulo apoyará la Fase 6 y permitirá comparar:

- error cuadrático medio,
- relación señal-ruido,
- diferencia entre señal original y procesada.
"""

from __future__ import annotations


import numpy as np

def mean_squared_error(reference: np.ndarray, estimate: np.ndarray) -> float:
    """Calcula el error cuadrático medio (MSE) entre dos señales."""
    # Aseguramos que ambas señales tengan el mismo tamaño recortando al mínimo
    min_len = min(len(reference), len(estimate))
    ref = reference[:min_len]
    est = estimate[:min_len]
    
    # MSE = Promedio de los errores al cuadrado
    mse = np.mean((ref - est) ** 2)
    return float(mse)


def signal_to_noise_ratio(reference: np.ndarray, estimate: np.ndarray) -> float:
    """Calcula una estimación básica de la relación señal-ruido (SNR) en dB."""
    min_len = min(len(reference), len(estimate))
    ref = reference[:min_len]
    est = estimate[:min_len]
    
    # El ruido residual es la diferencia entre lo que esperábamos (reference) 
    # y lo que obtuvimos (estimate)
    noise = ref - est
    
    power_signal = np.sum(ref ** 2)
    power_noise = np.sum(noise ** 2)
    
    # Evitamos la división por cero si el audio resultante es perfecto
    if power_noise == 0:
        return float('inf')
        
    snr = 10 * np.log10(power_signal / power_noise)
    return float(snr)