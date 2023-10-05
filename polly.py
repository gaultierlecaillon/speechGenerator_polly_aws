import boto3
from pygame import mixer
import io
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def aws_polly_speak(text):
    # Retrieve AWS credentials from environment variables
    aws_access_key = os.getenv('AWS_ACCESS_KEY')
    aws_secret_key = os.getenv('AWS_SECRET_KEY')
    aws_region = os.getenv('AWS_REGION')

    # Initialize a session using Amazon Polly
    polly_client = boto3.Session(
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=aws_region).client('polly')

    try:
        # Request speech synthesis
        response = polly_client.synthesize_speech(VoiceId='Joanna',
                                                  OutputFormat='mp3',
                                                  Text=text)

        # Play the generated speech using pygame
        soundfile = io.BytesIO(response['AudioStream'].read())
        mixer.init()
        mixer.music.load(soundfile)
        mixer.music.play()

        # Keep the script alive until audio playback is done
        while mixer.music.get_busy() == True:
            pass

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    text = "Hello, how can I assist you today?"
    aws_polly_speak(text)
