from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.chains.summarize import load_summarize_chain
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
print("Loading GenAI...")
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_chain():
    prompt_template = """
    Below is profile of a person. Just summarize the profile and name the role that suits the person the best and also the specilization. take into consideration the skills and experience of the person. 

    Profile: 
    {context}
    """

    # Set up the model
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)

    # Create the prompt template with the required input variables
    prompt = PromptTemplate(template=prompt_template, input_variables=["context"])

    # Load the summarize chain
    chain = LLMChain(llm=model, prompt=prompt)
    return chain

def input_resume(resume):
    chain = get_chain()
        # Pass each section as individual documents under 'text'
    
    documents = [
        f"Education: {resume['education']}",
        f"Skills: {resume['skills']}",
        f"Experience: {resume['professional experience']}",
        f"Projects: {resume['projects']}",
        f"Others: {resume['others']}"
    ]

    # Passing documents as input to the chain
    response = chain({"context": documents}, return_only_outputs=True)
    return response

    
    return response