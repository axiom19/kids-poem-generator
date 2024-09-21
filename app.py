import logging
from gen_poem import LLMService
from audio_join import AudioCombiner
from music_gen import MusicGenerator
from tts import TTSService
import os
import gc
import torch

torch.mps.empty_cache()
gc.collect()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Main Application class
class PoemGeneratorApp:
    def __init__(self):
        self.llm_service = LLMService()
        self.tts_service = TTSService()
        self.music_generator = MusicGenerator()
        self.audio_combiner = AudioCombiner()

    def generate_poem(self, word, language):
        logger.info(f"Generating a poem about '{word}' in {language}...")
        poem = self.llm_service.generate_poem(word, language)
        logger.info(f"Generated poem:\n{poem}")
        return poem['text']

    def text_to_speech(self, text, language):
        language_code = self.tts_service.get_language_code(language)
        poem_audio_file = "poem.mp3"
        self.tts_service.text_to_speech(text, language_code, poem_audio_file)
        logger.info(f"Poem audio saved as '{poem_audio_file}'.")
        return poem_audio_file

    def generate_music(self, prompt):
        music_audio_file = 'musicgen_out.wav'
        self.music_generator.generate_music(prompt, music_audio_file)
        logger.info(f"Music audio saved as '{music_audio_file}'.")
        return music_audio_file

    def combine_audio(self, poem_audio_file, music_audio_file):
        output_file = 'final_output.mp3'
        self.audio_combiner.combine_audio(poem_audio_file, music_audio_file, output_file)
        logger.info(f"Final audio saved as '{output_file}'.")
        return output_file


# Run the application
if __name__ == "__main__":
    app = PoemGeneratorApp(word="Butterfly", language="English")
    app.run()
