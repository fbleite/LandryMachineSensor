import pyaudio


rate = 44100
chunck = 8192

print ("starting")
stream_input = pyaudio.PyAudio().open(format=pyaudio.paInt16,
                                      channels=1, rate=rate,
                                      input=True, frames_per_buffer=chunck
                                      )
stream_output = pyaudio.PyAudio().open(format=pyaudio.paInt16,
                                      channels=1, rate=rate,
                                      output=True, frames_per_buffer=chunck)

print ("record and play")

for i in range(int(10 * rate/ chunck)):
    stream_output.write(stream_input.read(chunck))

stream_input.stop_stream()
stream_input.close()
stream_output.stop_stream()
stream_output.close()