import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd


def analyze_finances(df: pd.DataFrame):
    """Analyze uploaded financial data and return key insights + visualization."""
    if "Category" not in df.columns or "Amount" not in df.columns:
        st.error("Uploaded file must contain 'Category' and 'Amount' columns.")
        return None, None

    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce").fillna(0)
    total_spent = df["Amount"].sum()
    avg_transaction = df["Amount"].mean()
    top_categories = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)

    analysis = {
        "total_spent": total_spent,
        "avg_transaction": avg_transaction,
        "top_categories": top_categories,
    }

    plt.style.use("dark_background")
    sns.set_theme(style="darkgrid")

    fig, ax = plt.subplots(figsize=(4.5, 3), dpi=130)
    sns.barplot(
        x=top_categories.values,
        y=top_categories.index,
        ax=ax,
        palette="cool",
    )
    ax.set_title("💸 Top Spending Categories", fontsize=10, color="#E0E0E0", pad=8)
    ax.set_xlabel("Amount (₹)", fontsize=8, color="#AAAAAA")
    ax.set_ylabel("")
    ax.tick_params(axis="x", colors="#AAAAAA", labelsize=7)
    ax.tick_params(axis="y", colors="#DDDDDD", labelsize=7)
    plt.tight_layout()

    return analysis, fig


def generate_saving_tips(analysis: dict):
    total_spent = analysis["total_spent"]
    avg_txn = analysis["avg_transaction"]
    top_cat = analysis["top_categories"].index[0]

    tips = [
        f"💰 You spent ₹{total_spent:,.0f} this month — review '{top_cat}' expenses for potential savings.",
        f"📉 Try keeping your average transaction (₹{avg_txn:,.0f}) under a daily limit.",
        f"💡 Use automatic saving tools when '{top_cat}' expenses are low.",
    ]
    return tips
