# utils/vector_store.py
import faiss
import numpy as np
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def create_vector_store(df):
    df['text'] = df.apply(lambda x: f"On {x['Date']}, you spent {x['Amount']} for {x['Category']} ({x['Description']}).", axis=1)
    texts = df['text'].tolist()
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(texts, embedding=embeddings)
    vectorstore.save_local("embeddings/faiss_index")
    return vectorstore
