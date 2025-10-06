import os
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
# from langchain.chat_models import ChatGoogleGenerativeAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
import pandas as pd
load_dotenv()  # load .env file


# Initialize Gemini
def get_llm():
    api_key = os.getenv("GOOGLE_API_KEY","").strip()
    if not api_key:
        raise ValueError("Please set GOOGLE_API_KEY environment variable.")
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key,   # <-- explicitly pass API key
        temperature=0.2
    )

def build_qa_chain(df: pd.DataFrame):
    """Builds a LangChain pipeline for Q&A over financial data."""
    llm = get_llm()
    csv_summary = df.to_string(index=False)
    prompt = PromptTemplate(
        input_variables=["question"],
        template=(
            "You are a financial data assistant. Use the below statement data to answer:\n"
            "{data}\n\nQuestion: {question}\n"
            "Give a clear, concise, factual answer."
        ),
    )
    return LLMChain(llm=llm, prompt=prompt.partial(data=csv_summary))


def ask_question(chain, question: str):
    """Ask question and get AI response."""
    return chain.run(question=question)
