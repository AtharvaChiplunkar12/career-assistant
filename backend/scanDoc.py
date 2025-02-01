
from langchain.prompts import FewShotPromptTemplate
from PyPDF2 import PdfReader
import re
from genai import input_resume


# os.environ["HUGGINGFACEHUB_API_TOKEN"] = huggingface_access_key

# repo_id = "mistralai/Mistral-7B-Instruct-v0.3"

# llm = HuggingFaceEndpoint(
#     repo_id=repo_id, temperature=0.2, token= huggingface_access_key
# )

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows all origins
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all methods
#     allow_headers=["*"],  # Allows all headers
# )

# @app.get("/{query}")


def scan_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
        break
    return text

    
def extract_sections(text):
    sections = {
        "education": "",
        "skills": "",
        "professional experience": "",
        "projects": "",
        "others": ""
    }

    # Define regex patterns for each section
    section_patterns = {
        "education",
        "skills",
        "professional experience",
        "projects",
    }

    text_list = re.split(r'\n', text)
    curr_key = "others"
    for line in text_list:
        currLine = line.strip().lower()
        # print(currLine)
        # print("\n")
        if not currLine:
            continue
        if currLine in section_patterns:
            curr_key = currLine
        else:
            sections[curr_key] += (currLine + "\n")

    return sections

def read_root(query):
    return  


def main():
    pdf_text = scan_pdf("documents/Atharva Chiplunkar_Resume.pdf")
    sections = extract_sections(pdf_text)
    # for section, content in sections.items():
    #     print(f"--- {section} ---\n{content}\n")
    #print(sections['professional experience'])
    answers = input_resume(sections)
    print(answers['text'])

if __name__ == "__main__":
    main()