from transformers import pipeline
from scipy.io.wavfile import write
import torch


# Music Generator Service
class MusicGenerator:
    def __init__(self, model_name="facebook/musicgen-small"):
        self.device = "mps" if torch.backends.mps.is_available() else "cpu"
        self.synthesizer = pipeline(
            task="text-to-audio",
            model=model_name,
            device_map=self.device
        )

    def generate_music(self, text_prompt, output_file):
        music = self.synthesizer(
            text_prompt,
            forward_params={"do_sample": True}
        )

        write("musicgen_out.wav", rate=music["sampling_rate"], data=music["audio"])



# # test the music generator
# music_gen = MusicGenerator()
# music_gen.generate_music("lo-fi music with a soothing melody complementing a children's poem.", "musicgen_out.wav")
# print("Music generated successfully!")
