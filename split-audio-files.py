from pydub import AudioSegment
from pydub.silence import split_on_silence

sound = AudioSegment.from_mp3("recording.mp3")
audio_chunks = split_on_silence(sound, min_silence_len=500, silence_thresh=-40 )
for i, chunk in enumerate(audio_chunks):
   output_file = "chunk{0}.mp3".format(i)
   print("Exporting file", output_file)
   chunk.export(output_file, format="mp3")
