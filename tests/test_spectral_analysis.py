"""Pruebas automáticas para las funciones de src/fft_utils.py"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

import numpy as np
from src.fft_utils import calcular_fft, reconstruir_senal
from scipy.fft import fft


def crear_senal_prueba(freq_hz: float = 440.0, sample_rate: int = 44100, duration: float = 1.0) -> np.ndarray:
    """Crea una señal pura para usar en pruebas."""
    t = np.arange(int(sample_rate * duration)) / sample_rate
    return np.sin(2 * np.pi * freq_hz * t)


# --- PRUEBAS calcular_fft ---

def test_fft_devuelve_solo_mitad_positiva():
    sample_rate = 44100
    senal = crear_senal_prueba(sample_rate=sample_rate)
    N = len(senal)
    frecuencias, magnitud = calcular_fft(senal, sample_rate)
    assert len(frecuencias) == N // 2
    assert len(magnitud) == N // 2
    print("OK - calcular_fft devuelve exactamente N/2 puntos (mitad positiva)")


def test_fft_frecuencias_son_positivas():
    frecuencias, _ = calcular_fft(crear_senal_prueba(), 44100)
    assert np.all(frecuencias >= 0)
    print("OK - calcular_fft devuelve solo frecuencias positivas")


def test_fft_detecta_frecuencia_dominante():
    sample_rate = 44100
    freq_objetivo = 440.0
    senal = crear_senal_prueba(freq_hz=freq_objetivo, sample_rate=sample_rate)
    frecuencias, magnitud = calcular_fft(senal, sample_rate)
    freq_detectada = frecuencias[np.argmax(magnitud)]
    assert abs(freq_detectada - freq_objetivo) < 1.0
    print(f"OK - calcular_fft detecta correctamente el pico en {freq_objetivo} Hz")


# --- PRUEBAS reconstruir_senal ---

def test_reconstruir_devuelve_senal_real():
    senal = crear_senal_prueba()
    espectro = fft(senal)
    senal_reconstruida = reconstruir_senal(espectro)
    assert np.isrealobj(senal_reconstruida)
    print("OK - reconstruir_senal devuelve una señal real (sin parte imaginaria)")


def test_reconstruir_conserva_longitud():
    senal = crear_senal_prueba()
    espectro = fft(senal)
    senal_reconstruida = reconstruir_senal(espectro)
    assert len(senal_reconstruida) == len(senal)
    print("OK - reconstruir_senal conserva la misma longitud que la señal original")


def test_reconstruir_aproxima_senal_original():
    senal = crear_senal_prueba()
    espectro = fft(senal)
    senal_reconstruida = reconstruir_senal(espectro)
    error = np.max(np.abs(senal - senal_reconstruida))
    assert error < 1e-10
    print(f"OK - reconstruir_senal reproduce la señal original con error < 1e-10 ({error:.2e})")


if __name__ == "__main__":
    test_fft_devuelve_solo_mitad_positiva()
    test_fft_frecuencias_son_positivas()
    test_fft_detecta_frecuencia_dominante()
    test_reconstruir_devuelve_senal_real()
    test_reconstruir_conserva_longitud()
    test_reconstruir_aproxima_senal_original()
    print("\nTodas las pruebas pasaron correctamente.")
