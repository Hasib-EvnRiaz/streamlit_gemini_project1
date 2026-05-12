from google import genai 
from dotenv import load_dotenv
import os,io
from PIL import Image
from gtts import gTTS


#loading the environment variable
load_dotenv()

my_key=os.getenv("GEMINI_API_KEY")

#initializing a client 
client=genai.Client(api_key=my_key)

#NODE GENERATOR
def note_generator(images):

    prompt="""summarize the picture in node 
    format at max 100 words, make sure to 
    add necessaray markdown to differntiate
      different section"""
    response= client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images,prompt]
    )
    return response.text

def audio_transcription(text):
   speech=gTTS(text,lang="en",slow=False)

   audio_buffer= io.BytesIO()
   speech.write_to_fp(audio_buffer)
   return audio_buffer

def quiz_generator(image,difficulty):
    prompt=f"Generate  3 quizes base don the {difficulty}.make sure to add markdown to diffrence with correct answers after the quiz."

    response= client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[image,prompt]
    )
    return response.text