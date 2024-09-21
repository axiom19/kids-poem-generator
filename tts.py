import gtts

# TTS Service to handle text-to-speech conversion
class TTSService:
    @staticmethod
    def get_language_code(language_name):
        language_codes = {
            'English': 'en',
            'Spanish': 'es',
            'French': 'fr',
            'German': 'de',
            'Italian': 'it',
            'Chinese': 'zh-CN',
            'Japanese': 'ja',
            'Korean': 'ko',
            'Russian': 'ru',
            'Arabic': 'ar',
            'Hindi': 'hi',
            'Punjabi': 'pa',
            'Bengali': 'bn',
        }
        return language_codes.get(language_name, 'en')  # Default to English

    @staticmethod
    def text_to_speech(text, language_code, filename):
        tts = gtts.gTTS(text=text, lang=language_code)
        tts.save(filename)
