import openai
from pydub import AudioSegment
from decouple import config

openai.api_key = config("OPENAI_API_KEY")

input_file = "data/sample_audio.ogg"
mp3_file = "data/sample_audio.mp3"

audio_file = AudioSegment.from_ogg(input_file)

audio_file.export(mp3_file, format="mp3")
audio_file = open(mp3_file, "rb")

whisper_response = openai.Audio.transcribe(
        file=audio_file,
        model="whisper-1",
        language="en",
        temperature=0.5,
        )
audio_file.close()
print(whisper_response)

