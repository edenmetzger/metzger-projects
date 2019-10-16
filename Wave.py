import math
import stdaudio

global sample_rate
sample_rate = 44100
samples = []

class Wave:

	def __init__(self, hz, seconds, amplitude):
		self.hz = hz
		self.seconds = seconds
		self.amplitude = amplitude
		for i in range(0,seconds):
			for i in range(1, sample_rate):
				samp = self.amplitude * math.sin(2*math.pi * self.hz * i/sample_rate)
				samples.append(samp)

	def play(self):
		stdaudio.playSamples(samples)
	#this does not work
	def record(self, name):
		stdaudio.save(name, samples)


