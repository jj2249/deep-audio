from audio_handler import Song, Sample
import os

CWD = os.getcwd()
sev = Song(CWD+'/songs/1759.wav')
sev.load_song()
sev_samp = Sample()
sev_samp.song_to_samples(sev, sample_length=sev.get_rate())
#print(sev_samp.get_audio())
sev2 = Song()
sev2.samples_to_song(sev_samp)
print(sev2.get_audio().shape)