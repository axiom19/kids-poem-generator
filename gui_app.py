import gradio as gr
from app import PoemGeneratorApp
import torch
import gc

torch.mps.empty_cache()
gc.collect()

# Initialize your application logic
app_logic = PoemGeneratorApp()


def generate_poem_interface(word, language):
    # Validate inputs
    if not word:
        return "Please enter a word.", None
    if not language:
        return "Please select a language.", None

    try:
        # Generate the poem
        poem_text = app_logic.generate_poem(word, language)

        # Convert poem to speech
        poem_audio_file = app_logic.text_to_speech(poem_text, language)

        # Generate music
        music_prompt = f"Music that complements a children's poem about {word}, in a soothing and cheerful style."
        music_audio_file = app_logic.generate_music(music_prompt)

        # Combine audio
        final_audio_file = app_logic.combine_audio(poem_audio_file, music_audio_file)

        # Return the poem text and the final audio file
        return final_audio_file
    except Exception as e:
        return f"An error occurred: {str(e)}", None


# Define the inputs
word_input = gr.Textbox(lines=1, label="Enter a word:")
language_input = gr.Dropdown(
    choices=['English', 'Spanish', 'French', 'German', 'Italian', 'Chinese', 'Japanese', 'Korean', 'Russian', 'Arabic',
             'Hindi', 'Punjabi', 'Bengali'],
    label="Choose a language:"
)

# Define the outputs
audio_output = gr.Audio(type="filepath", label="Poem with Music:")

# Create the interface
iface = gr.Interface(
    fn=generate_poem_interface,
    inputs=[word_input, language_input],
    outputs=[audio_output],
    title="Kid's Poem Generator",
    description="Enter a word and select a language to generate a children's poem with music.",
    allow_flagging="never",
    theme="monochrome",
    thumbnail="https://www.pngitem.com/pimgs/m/146-1468479_kids-poem-clipart-hd-png-download.png"
)

if __name__ == "__main__":
    iface.launch()
