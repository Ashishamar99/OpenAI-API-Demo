import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.organization = os.getenv("OPENAI_ORG_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.Model.list())