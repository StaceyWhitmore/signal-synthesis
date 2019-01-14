from __future__ import print_function, division
%matplotlib qt5

import thinkdsp
import thinkplot

import warnings
warnings.filterwarnings('ignore')

from IPython.html.widgets import interact, fixed
from IPython.display import display

signal = (thinkdsp.SinSignal(freq=400, amp=1.0) +
          thinkdsp.SinSignal(freq=600, amp=0.5) +
          thinkdsp.SinSignal(freq=800, amp=0.25))
signal.plot()


# Here are some arbitrary components I chose.  It makes an interesting waveform!
signal = (thinkdsp.SinSignal(freq=400, amp=1.0) +
          thinkdsp.SinSignal(freq=600, amp=0.5) +
          thinkdsp.SinSignal(freq=800, amp=0.25))
signal.plot()

# Use the signal to make a wave
wave2 = signal.make_wave(duration=1)
wave2.apodize()

#this is what it sounds like--
wave2.make_audio()

# Since the components are all multiples of 200 Hz, they make a coherent sounding tone.
#The spectrum looks like this--
spectrum = wave2.make_spectrum()
spectrum.plot(high=2000)

#When you add a multiple that is not a multiple of 200 Hz, you will hear it as a distinctive pitch--
signal += thinkdsp.SinSignal(freq=450)
signal.make_wave().make_audio()
