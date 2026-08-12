import streamlit as st

# ==========================
# Import Utility Files
# ==========================

from utils.pdf_reader import extract_text_from_pdf
from utils.text_cleaner import clean_text
from utils.keyword_extractor import extract_keywords
from utils.summary import generate_summary
from utils.dashboard import document_statistics
from utils.search import search_text
from utils.report_generator import generate_report
from utils.charts import create_bar_chart, create_pie_chart
from utils.chatbot import chatbot_response
from utils.wordcloud_generator import create_wordcloud
from utils.quiz_generator import generate_quiz
from utils.sentiment import analyze_sentiment
from utils.download_summary import download_summary

# ==========================
# Page Configuration
# ==========================

st.set_page_config(
    page_title="AI Document Intelligence Platform",
    page_icon="📄",
    layout="wide"
)

# ==========================
# Session State
# ==========================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "stats" not in st.session_state:
    st.session_state.stats = None

if "report" not in st.session_state:
    st.session_state.report = None

if "text" not in st.session_state:
    st.session_state.text = ""

# ==========================
# Sidebar
# ==========================

st.sidebar.title("📂 Navigation")

menu = st.sidebar.radio(
    "Go To",
    [
        "🏠 Home",
        "📤 Upload Document",
        "📊 Dashboard",
        "📑 Reports",
        "ℹ About"
    ]
)
# ==========================================
# THEME SWITCHER
# ==========================================

theme = st.sidebar.selectbox(
    "🎨 Select Theme",
    ["Light", "Dark"]
)
if theme == "Dark":

    st.markdown("""
    <style>

    .stApp{
        background-color:#0E1117;
        color:white;
    }

    h1,h2,h3,h4,h5,h6{
        color:white;
    }

    section[data-testid="stSidebar"]{
        background:#111827;
    }

    </style>
    """, unsafe_allow_html=True)

else:

    st.markdown("""
    <style>

    .stApp{
        background:white;
        color:black;
    }

    h1,h2,h3,h4,h5,h6{
        color:#0F172A;
    }

    </style>
    """, unsafe_allow_html=True)

# ==========================
# HOME PAGE
# ==========================

if menu == "🏠 Home":

    st.title("📄 AI Document Intelligence Platform")

    st.markdown("""
## Welcome 👋

This application can:

- 📄 Read PDF Documents
- 📝 Generate AI Summary
- 🔑 Extract Keywords
- 😊 Sentiment Analysis
- 🔍 Search Inside PDF
- 🤖 AI Chat with PDF
- 📝 AI Quiz
- 📊 Dashboard
- 📈 Charts
- ☁️ Word Cloud
- 📑 Download AI Report
""")

    col1, col2 = st.columns(2)

    with col1:
        st.info("📄 PDF Reader")
        st.info("📝 AI Summary")
        st.info("🔑 Keyword Extraction")
        st.info("😊 Sentiment Analysis")

    with col2:
        st.info("🔍 Smart Search")
        st.info("🤖 AI Chat")
        st.info("📝 AI Quiz")
        st.info("📊 Dashboard")

    st.success("✅ Project Ready")# ==========================================
# UPLOAD DOCUMENT
# ==========================================

elif menu == "📤 Upload Document":

    st.header("📤 Upload Your Document")

    uploaded_file = st.file_uploader(
        "Choose a PDF File",
        type=["pdf"]
    )

    if uploaded_file is not None:

        st.success("✅ PDF Uploaded Successfully!")

        file_size = round(
            uploaded_file.size / 1024,
            2
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "📄 File Name",
                uploaded_file.name
            )

        with col2:
            st.metric(
                "📦 File Size",
                f"{file_size} KB"
            )

        with st.spinner("📖 Processing PDF..."):

            # Read PDF
            text, total_pages = extract_text_from_pdf(
                uploaded_file
            )

            # Save text
            st.session_state.text = text

            # Clean text
            cleaned_text = clean_text(text)

            # AI Summary
            summary = generate_summary(
                cleaned_text
            )

            # Sentiment Analysis
            sentiment, score = analyze_sentiment(
                text
            )

            # Keywords
            keywords = extract_keywords(
                cleaned_text
            )

            # AI Quiz
            quiz = generate_quiz(
                keywords
            )

            # Statistics
            stats = document_statistics(
                text,
                total_pages,
                keywords
            )

            st.session_state.stats = stats

            # Report
            report = generate_report(
                stats,
                summary,
                keywords
            )

            st.session_state.report = report

        st.success("🎉 Document Processed Successfully!")

        # ==================================
        # PDF INFORMATION
        # ==================================

        st.subheader("📄 PDF Information")

        st.write(
            f"**Total Pages:** {total_pages}"
        )

        # ==================================
        # EXTRACTED TEXT
        # ==================================

        st.subheader("📖 Extracted Text")

        st.text_area(
            "PDF Content",
            text,
            height=300
        )

        # ==================================
        # CLEANED TEXT
        # ==================================

        st.subheader("🧹 Cleaned Text")

        st.text_area(
            "Cleaned Text",
            cleaned_text,
            height=250
        )

        # ==================================
        # AI SUMMARY
        # ==================================

        st.subheader("🤖 AI Summary")

        st.write(summary)
        st.download_button(
        label="📥 Download Summary",
    data=download_summary(summary),
    file_name="summary.txt",
    mime="text/plain"
     )

        # ==================================
        # SENTIMENT ANALYSIS
        # ==================================

        st.divider()

        st.subheader("😊 Sentiment Analysis")

        st.success(
            f"Document Sentiment: {sentiment}"
        )

        st.write(
            f"Polarity Score: {score:.2f}"
        )

        # ==================================
        # KEYWORDS
        # ==================================

        st.subheader("🔑 Extracted Keywords")

        for word in keywords:

            st.write("✅", word)        # ==================================
        # SEARCH INSIDE PDF
        # ==================================

        st.divider()

        st.subheader("🔍 Search Inside PDF")

        query = st.text_input(
            "Enter a keyword to search"
        )

        if query:

            results = search_text(
                text,
                query
            )

            if results:

                st.success(
                    f"✅ {len(results)} Result(s) Found"
                )

                for result in results:

                    st.write(result)

            else:

                st.error(
                    "❌ No Matching Text Found."
                )

        # ==================================
        # AI QUIZ
        # ==================================

        st.divider()

        st.subheader("📝 AI Quiz")

        score = 0

        for i, q in enumerate(quiz):

            st.write(f"### Question {i+1}")

            st.write(q["question"])

            user_answer = st.radio(
                "Choose your answer",
                q["options"],
                key=f"quiz_{i}"
            )

            if user_answer == q["answer"]:

                score += 1

        if st.button("Submit Quiz"):

            st.success(
                f"🎉 Your Score: {score}/{len(quiz)}"
            )

        # ==================================
        # AI CHAT
        # ==================================

        st.divider()

        st.subheader("🤖 AI Chat with PDF")

        question = st.text_input(
            "Ask a question about this PDF",
            key="chat_question"
        )

        if st.button("Ask AI"):

            if question.strip() != "":

                answer = chatbot_response(
                    text,
                    question
                )

                st.session_state.chat_history.append(
                    ("You", question)
                )

                st.session_state.chat_history.append(
                    ("AI", answer)
                )

            else:

                st.warning(
                    "⚠ Please enter a question."
                )

        if st.session_state.chat_history:

            st.subheader("💬 Chat History")

            for sender, message in st.session_state.chat_history:

                if sender == "You":

                    st.markdown(
                        f"🧑 **You:** {message}"
                    )

                else:

                    st.markdown(
                        f"🤖 **AI:** {message}"
                    )# ==========================================
# DASHBOARD
# ==========================================

elif menu == "📊 Dashboard":

    st.header("📊 Dashboard")

    if st.session_state.stats is not None:

        stats = st.session_state.stats

        st.success("✅ Dashboard Loaded Successfully!")

        # -------------------------
        # Statistics
        # -------------------------

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "📄 Total Pages",
                stats["Pages"]
            )

            st.metric(
                "📝 Total Words",
                stats["Words"]
            )

        with col2:

            st.metric(
                "🔤 Characters",
                stats["Characters"]
            )

            st.metric(
                "📖 Sentences",
                stats["Sentences"]
            )

        with col3:

            st.metric(
                "🔑 Keywords",
                stats["Keywords"]
            )

            st.metric(
                "⏱ Reading Time",
                f"{stats['Reading Time']} min"
            )

        st.divider()

        # -------------------------
        # Charts
        # -------------------------

        st.subheader("📈 Document Analytics")

        left, right = st.columns(2)

        with left:

            st.subheader("📊 Bar Chart")

            fig_bar = create_bar_chart(stats)

            st.pyplot(fig_bar)

        with right:

            st.subheader("🥧 Pie Chart")

            fig_pie = create_pie_chart(stats)

            st.pyplot(fig_pie)

        st.divider()

        # -------------------------
        # Word Cloud
        # -------------------------

        st.subheader("☁️ Word Cloud")

        if st.session_state.text != "":

            fig_wc = create_wordcloud(
                st.session_state.text
            )

            st.pyplot(fig_wc)

        else:

            st.info(
                "Please upload a PDF first."
            )

    else:

        st.warning(
            "⚠ Please upload a document first."
        )# ==========================================
# REPORTS PAGE
# ==========================================

elif menu == "📑 Reports":

    st.header("📑 AI Report")

    if st.session_state.report is not None:

        st.success("✅ Report Generated Successfully!")

        st.write(
            "Click the button below to download your report."
        )

        with open(
            st.session_state.report,
            "rb"
        ) as file:

            st.download_button(
                label="📥 Download AI Report",
                data=file,
                file_name="AI_Report.pdf",
                mime="application/pdf"
            )

    else:

        st.warning(
            "⚠ Please upload a document first."
        )


# ==========================================
# ABOUT PAGE
# ==========================================

elif menu == "ℹ About":

    st.title("ℹ About Project")

    st.markdown("""
# 📄 AI Document Intelligence Platform

This project is developed using Artificial Intelligence (AI)
and Natural Language Processing (NLP).

---

## 🚀 Features

✅ PDF Reader

✅ Text Cleaning

✅ AI Summary

✅ Sentiment Analysis

✅ Keyword Extraction

✅ Smart Search

✅ AI Quiz

✅ AI Chat with PDF

✅ Dashboard

✅ Bar Chart

✅ Pie Chart

✅ Word Cloud

✅ AI Report Generation

---

## 🛠 Technologies Used

- Python
- Streamlit
- PDFPlumber
- NLTK
- TextBlob
- Transformers
- Scikit-learn
- Matplotlib
- WordCloud
- ReportLab

---

## 👩‍💻 Developed By

**Lavisha**

BCA (AI/ML)

Academic Project

Version **1.0**
""")

    st.divider()

    st.info("📚 AI + NLP Based Academic Project")

    st.success("🎉 Thank you for using AI Document Intelligence Platform!")

    st.caption(
        "Made with ❤️ using Python, Streamlit & AI"
    )