import streamlit as st
import pandas as pd
from finance_analyzer import analyze_finances, generate_saving_tips
from qa_engine import build_qa_chain, ask_question

st.set_page_config(page_title="Finance Insight Bot 💰", layout="centered", page_icon="💸")

st.title("💰 Finance Statement Insight Bot")
st.markdown(
    "Upload your **monthly financial statement (CSV)** to analyze spending patterns, visualize categories, "
    "get smart tips, and ask financial questions via AI 🤖."
)

uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    with st.expander("📋 View Uploaded Data"):
        st.dataframe(df)

    analysis, fig = analyze_finances(df)
    if analysis and fig:
        st.pyplot(fig)

        st.subheader("📊 Summary Insights")
        st.metric("💸 Total Spent", f"₹{analysis['total_spent']:,.2f}")
        st.metric("💳 Average Transaction", f"₹{analysis['avg_transaction']:,.2f}")

        st.subheader("💡 Smart Saving Tips")
        for tip in generate_saving_tips(analysis):
            st.write(f"- {tip}")

        # Q&A Interface
        st.divider()
        st.subheader("🤖 Ask Anything About Your Spending")

        if "qa_chain" not in st.session_state:
            st.session_state.qa_chain = build_qa_chain(df)

        user_question = st.text_input("💬 Type your question:")
        if user_question:
            with st.spinner("Thinking..."):
                response = ask_question(st.session_state.qa_chain, user_question)
            st.success(response)

else:
    st.info("Please upload a CSV file with at least two columns: `Category` and `Amount`.")
