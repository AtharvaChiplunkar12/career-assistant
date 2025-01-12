from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
print("Loading GenAI...")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def get_chain():
    prompt_template = """
    """
    model=ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    