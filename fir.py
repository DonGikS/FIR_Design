import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 필터 사양 정의
fs = 1000  # 샘플링 주파수
nyquist_freq = 0.5 * fs

# 밴드패스 필터 파라미터 정의
pass_band = [40, 200]  # 패스밴드 주파수 범위
stop_band = [0, 20, 220, 500]  # 스톱밴드 주파수 범위

# 필터 계수 계산
num_taps = 687  # 필터 길이 (계수 개수)
pass_band_normalized = [f / nyquist_freq for f in pass_band]
stop_band_normalized = [f / nyquist_freq for f in stop_band]
b = signal.firwin(num_taps, pass_band_normalized, pass_zero=False)

# FIR 필터의 주파수 응답 플로팅 (게인을 -80dB로 제한하여 변환)
w, h = signal.freqz(b, worN=8000)
freq_response_db = 20 * np.log10(np.abs(h))  # 게인을 dB로 변환
freq_response_db_limited = np.maximum(freq_response_db, -80)  # -80dB까지 제한
plt.figure()
plt.plot(0.5 * fs * w / np.pi, freq_response_db_limited, 'b')
plt.axvline(pass_band[0], color='green', linestyle='--')
plt.axvline(pass_band[1], color='green', linestyle='--')
for i in range(0, len(stop_band), 2):
    plt.axvline(stop_band[i], color='red', linestyle='--')
    plt.axvline(stop_band[i + 1], color='red', linestyle='--')
plt.xlim(0, 0.5 * fs)
plt.ylim(-80, 5)  # -80dB까지 표시하도록 y축 범위 제한
plt.title("Bandpass Filter Frequency Response")
plt.xlabel('Frequency [Hz]')
plt.ylabel('Gain [dB]')
plt.grid()
plt.show()
