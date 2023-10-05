from gtts import gTTS
import os

def text_to_speech(text, lang='fr', output_file='output.mp3'):
    """
    Convert text to speech using gTTS and save it to an output file.

    :param text: Text to convert to speech.
    :param lang: Language to use for the speech. Default is 'en' (English).
    :param output_file: The filename to save the speech audio. Default is 'output.mp3'.
    """
    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save(output_file)
        print(f"File saved as {output_file}")
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    text = input("Enter the text to convert to speech: ")
    text_to_speech(text)
