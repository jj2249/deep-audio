from scipy.io import wavfile
import torch
import os
import numpy as np

CWD = os.getcwd()

class Audio:
	"""
	Audio has data and an assosciated rate
	"""
	def __init__(self):
		self.rate = None
		self.data = np.array([])
		self.channels = None

	def get_channels(self):
		return self.rate

	def get_rate(self):
		return self.rate

	def get_audio(self):
		return self.data


class Song(Audio):
	"""
	Song class is audio along with a path
	"""
	def __init__(self, path=''):
		super().__init__()
		# is there a better way to handle the blank path case?
		self.path = path
		self.length = None

	def load_song(self):
		# fetches the song data from the song's path
		if self.path == '':
			print('Errrr... the Song needs a path please!')
		else:
			try:
				self.rate, self.data = wavfile.read(self.path)
				self.length = self.data[:,0].shape[0]
			except FileNotFoundError:
				print("Not a valid path.")

	def set_path(self, path):
		self.path # path

	def samples_to_song(self, sample_obj):
		stacked_samples = np.array(np.concatenate(sample_obj.data))
		with_end = np.array(np.concatenate((stacked_samples, sample_obj.remainder)))
		self.data = with_end

	

class Sample(Audio):
	"""
	Contains a song broken into samples of a given length, plus the remainder
	"""
	def __init__(self):
		super().__init__()
		self.remainder = np.array([])
		self.no_samples = None

	def get_samples(self):
		return self.samples

	def song_to_samples(self, song_obj, sample_length=1000):
		self.no_samples = np.floor(song_obj.length / sample_length)
		self.remainder = song_obj.data[int(self.no_samples*sample_length):][:]
		self.data = np.array(np.split(song_obj.data[:int(self.no_samples*sample_length)][:], self.no_samples, axis=0))
