import os
import openai
from dotenv import load_dotenv

def text_completion(promptText):
    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=promptText,
        temperature=1,
        max_tokens=30,
        top_p=1.0,
        n=3
    )
    print(response)
    
def image_generation(promptText):
    response = openai.Image.create(
        prompt=promptText,
        n=1,
        response_format="url"
    )
    print(response)

if __name__ == "__main__":
    load_dotenv()
    openai.organization = os.getenv("OPENAI_ORG_KEY")
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    text_completion(input("Enter prompt for text completion:: "))
    image_generation(input("Enter text for image generation:: "))