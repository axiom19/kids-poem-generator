from pydub import AudioSegment


# Audio Combiner Service
class AudioCombiner:
    @staticmethod
    def combine_audio(poem_audio_file, music_audio_file, output_file):
        poem_audio = AudioSegment.from_file(poem_audio_file, format="mp3")
        music_audio = AudioSegment.from_file(music_audio_file, format="wav")

        # Adjust volumes
        poem_audio += 3
        music_audio -= 3

        # Loop or trim music to match the length of the poem
        if len(music_audio) < len(poem_audio):
            music_audio = music_audio * (int(len(poem_audio) / len(music_audio)) + 1)
        music_audio = music_audio[:len(poem_audio)]

        # Combine the audio tracks
        final_audio = music_audio.overlay(poem_audio)

        # Export the final audio
        final_audio.export(output_file, format='mp3')

# # test the audio combiner
# audio_combiner = AudioCombiner()
# audio_combiner.combine_audio("poem.mp3", "musicgen_out.wav", "demo_final_output.mp3")
# print("Audio combined successfully!")
