import time
from langchain_community.chat_models import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from openai import OpenAI
import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

def getOpenAI():
    llm = ChatOpenAI(temperature=0, model_name='gpt-4o')
    return llm

def getGenAI():
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0,
        max_output_tokens=200,
        google_api_key=GOOGLE_API_KEY
    )
    return llm

def progress_bar (msg):
    progress_text = msg
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.08)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    return my_bar

def makeAudio(text, name):
    if not os.path.exists("audio"):
        os.makedirs("audio")
    model = openAiModel()

    response = model.audio.speech.create(
        model="tts-1",
        input=text,
        voice="nova",
        response_format="mp3",
        speed=1.1,
    )
    response.stream_to_file("audio/" +name)


def openAiModel():
    client = OpenAI(api_key=OPENAI_API_KEY)
    return client