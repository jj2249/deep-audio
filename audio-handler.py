from scipy.io import wavfile
import torch
import os
import numpy as np

CWD = os.getcwd()

class Song:
	"""
	Song class contains song data (audio + rate), and a path to the original data
	"""
	def __init__(self, path=''):
		# is there a better way to handle the blank path case?
		self.path = CWD + path
		self.rate = None
		self.song = np.array([])
		self.length = None

	def load_song(self):
		# fetches the song data from the
		if self.path = CWD:
			print('Errrr... the Song needs a path please!')
		else:
			self.rate, self.song = wavfile.read(self.path)
			self.length = self.song[:,0].shape[0]

	def set_path(self, path):
		self.path = CWD + path

	def get_rate(self):
		return self.rate

	def get_song(self):
		return self.song

	def samples_to_song(self, sample_obj):
		stacked_samples = np.array(np.concatenate(sample_obj.samples))
		with_end = np.array(np.concatenate((stacked_samples, sample_obj.remainder)))
		self.song = with_end

	

class Sample(Song):
	"""
	Contains a song broken into samples of a given length, plus the remainder
	"""
	def __init__(self):
		self.samples = np.array([])
		self.remainder = np.array([])
		self.no_samples = None
		self.path=''

	def get_samples(self):
		return self.samples

	def song_to_samples(self, song_obj, sample_length=1000):
		self.no_samples = np.floor(song_obj.length / sample_length)
		self.remainder = song_obj.song[int(self.no_samples*sample_length):][:]
		self.samples = np.array(np.split(song_obj.song[:int(self.no_samples*sample_length)][:], self.no_samples, axis=0))


sev = Song('/songs/1759.wav')
sev.load_song()
samps1 = Sample()
print(samps1.get_samples())
samps1.song_to_samples(sev)
print(samps1.get_samples())
sev1 = Song()
sev1.samples_to_song(samps1)
print(sev1.get_song().shape)