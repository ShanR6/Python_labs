import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(16, 8))

freq1 = 1.0
ampl1 = 1.0
freq2 = 1.0
ampl2 = 1.0


def update_plots():
    ax1.cla()
    ax2.cla()
    ax3.cla()
    t = np.linspace(0, 10, 1000)

    wave1 = ampl1 * np.sin(2 * np.pi * freq1 * t)
    wave2 = ampl2 * np.sin(2 * np.pi * freq2 * t)
    wave_sum = wave1 + wave2

    ax1.plot(t, wave1, color="r")
    ax1.set_title("Wave 1")
    ax2.plot(t, wave2, color="g")
    ax2.set_title("Wave 2")
    ax3.plot(t, wave_sum, color="b")
    ax3.set_title("Wave sum")

    fig.canvas.draw()


axfreq1 = plt.axes((0.25, 0.94, 0.6, 0.03))
axampl1 = plt.axes((0.25, 0.92, 0.6, 0.03))
axfreq2 = plt.axes((0.25, 0.04, 0.6, 0.03))
axampl2 = plt.axes((0.25, 0.02, 0.6, 0.03))

slider_freq1 = Slider(axfreq1, "Frequency 1", 0.1, 10.0, valinit=freq1)
slider_ampl1 = Slider(axampl1, "Amplitude 1", 0.1, 10.0, valinit=ampl1)
slider_freq2 = Slider(axfreq2, "Frequency 2", 0.1, 10.0, valinit=freq2)
slider_ampl2 = Slider(axampl2, "Amplitude 2", 0.1, 10.0, valinit=ampl2)


def update_wave(val):
    global freq1, ampl1, freq2, ampl2
    freq1 = slider_freq1.val
    ampl1 = slider_ampl1.val
    freq2 = slider_freq2.val
    ampl2 = slider_ampl2.val
    update_plots()


slider_freq1.on_changed(update_wave)
slider_ampl1.on_changed(update_wave)
slider_freq2.on_changed(update_wave)
slider_ampl2.on_changed(update_wave)

update_plots()
plt.show()
