import openai
import fastapi
from fastapi import Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os


app = fastapi.FastAPI()



load_dotenv()
openai.api_key = os.getenv('API_KEY')

class Prompt(BaseModel):
    prompt: str

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )


@app.post("/api/prompt", description="Enter your question here", name="Ask me anything")
def generate_response(prompt: Prompt):
    
    prompt_text = prompt.prompt
    model_engine = "text-davinci-003"
    max_tokens = 500
    temperature = 0.7

    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt_text,
        max_tokens=max_tokens,
        temperature=temperature
    )

    generated_text = response.choices[0]['text']

    return { "response" : generated_text }

