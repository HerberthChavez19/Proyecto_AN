"""Pruebas automáticas para los filtros del módulo src/filters.py"""

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

import numpy as np
from scipy.fft import fft, ifft, fftfreq
from src.filters import apply_notch_mask, apply_lowpass_mask, apply_highpass_mask


def crear_senal_con_frecuencia(freq_hz: float, sample_rate: int = 44100, duration: float = 1.0) -> np.ndarray:
    """Crea una señal pura de una sola frecuencia para usar en pruebas."""
    t = np.arange(int(sample_rate * duration)) / sample_rate
    return np.sin(2 * np.pi * freq_hz * t)


def magnitud_en_frecuencia(spectrum: np.ndarray, target_hz: float, sample_rate: int) -> float:
    """Devuelve la magnitud del espectro en una frecuencia específica."""
    N = len(spectrum)
    freqs = fftfreq(N, 1 / sample_rate)
    idx = np.argmin(np.abs(freqs - target_hz))
    return float(np.abs(spectrum[idx]))


# --- PRUEBAS NOTCH ---

def test_notch_elimina_frecuencia_objetivo():
    senal = crear_senal_con_frecuencia(60.0)
    espectro = fft(senal)
    espectro_filtrado = apply_notch_mask(espectro, center_hz=60.0, bandwidth_hz=2.0, sample_rate=44100)
    assert magnitud_en_frecuencia(espectro_filtrado, 60.0, 44100) < 1.0
    print("OK - Notch elimina la frecuencia objetivo (60 Hz)")


def test_notch_conserva_frecuencias_fuera_de_banda():
    senal = crear_senal_con_frecuencia(440.0)
    espectro = fft(senal)
    mag_antes = magnitud_en_frecuencia(espectro, 440.0, 44100)
    espectro_filtrado = apply_notch_mask(espectro, center_hz=60.0, bandwidth_hz=2.0, sample_rate=44100)
    mag_despues = magnitud_en_frecuencia(espectro_filtrado, 440.0, 44100)
    assert abs(mag_antes - mag_despues) < 1.0
    print("OK - Notch no afecta frecuencias fuera de su banda (440 Hz intacto)")


# --- PRUEBAS PASA-BAJAS ---

def test_lowpass_elimina_frecuencias_altas():
    senal = crear_senal_con_frecuencia(5000.0)
    espectro = fft(senal)
    espectro_filtrado = apply_lowpass_mask(espectro, cutoff_hz=1000.0, sample_rate=44100)
    assert magnitud_en_frecuencia(espectro_filtrado, 5000.0, 44100) == 0.0
    print("OK - Pasa-bajas elimina frecuencias por encima del corte (5000 Hz a 0)")


def test_lowpass_conserva_frecuencias_bajas():
    senal = crear_senal_con_frecuencia(440.0)
    espectro = fft(senal)
    mag_antes = magnitud_en_frecuencia(espectro, 440.0, 44100)
    espectro_filtrado = apply_lowpass_mask(espectro, cutoff_hz=1000.0, sample_rate=44100)
    mag_despues = magnitud_en_frecuencia(espectro_filtrado, 440.0, 44100)
    assert abs(mag_antes - mag_despues) < 1.0
    print("OK - Pasa-bajas conserva frecuencias por debajo del corte (440 Hz intacto)")


# --- PRUEBAS PASA-ALTAS ---

def test_highpass_elimina_frecuencias_bajas():
    senal = crear_senal_con_frecuencia(80.0)
    espectro = fft(senal)
    espectro_filtrado = apply_highpass_mask(espectro, cutoff_hz=500.0, sample_rate=44100)
    assert magnitud_en_frecuencia(espectro_filtrado, 80.0, 44100) == 0.0
    print("OK - Pasa-altas elimina frecuencias por debajo del corte (80 Hz a 0)")


def test_highpass_conserva_frecuencias_altas():
    senal = crear_senal_con_frecuencia(3000.0)
    espectro = fft(senal)
    mag_antes = magnitud_en_frecuencia(espectro, 3000.0, 44100)
    espectro_filtrado = apply_highpass_mask(espectro, cutoff_hz=500.0, sample_rate=44100)
    mag_despues = magnitud_en_frecuencia(espectro_filtrado, 3000.0, 44100)
    assert abs(mag_antes - mag_despues) < 1.0
    print("OK - Pasa-altas conserva frecuencias por encima del corte (3000 Hz intacto)")


if __name__ == "__main__":
    test_notch_elimina_frecuencia_objetivo()
    test_notch_conserva_frecuencias_fuera_de_banda()
    test_lowpass_elimina_frecuencias_altas()
    test_lowpass_conserva_frecuencias_bajas()
    test_highpass_elimina_frecuencias_bajas()
    test_highpass_conserva_frecuencias_altas()
    print("\nTodas las pruebas pasaron correctamente.")
