# utils/data_loader.py
import pandas as pd
import pdfplumber

def extract_from_csv(path):
    return pd.read_csv(path)

def extract_from_pdf(path):
    rows = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            rows.extend([line.split() for line in text.split("\n") if line])
    df = pd.DataFrame(rows, columns=["Date", "Description", "Amount"])
    return df
