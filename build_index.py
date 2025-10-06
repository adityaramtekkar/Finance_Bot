# build_index.py
import pandas as pd
from utils.data_loader import extract_from_csv
from utils.categorizer import categorize_expense
from utils.vector_store import create_vector_store

# 1️⃣ Load your data
df = extract_from_csv("data/sample.csv")

# 2️⃣ Categorize expenses
df["Category"] = df["Description"].apply(categorize_expense)

# 3️⃣ Create FAISS vector store
create_vector_store(df)

print("✅ FAISS vector index created successfully at embeddings/faiss_index/")
