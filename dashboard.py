import streamlit as st
import tempfile
import os
import json

from src.pdf_parser import extract_text_from_pdf
from src.html_parser import extract_text_from_html
from src.extractor import extract_bid_info

# -----------------------------------
# Page Config
# -----------------------------------

st.set_page_config(
    page_title="AI Procurement Intelligence Dashboard",
    layout="wide"
)

# -----------------------------------
# Sidebar
# -----------------------------------

st.sidebar.title("📂 Dashboard Menu")

st.sidebar.info(
    "AI-powered procurement document extraction system."
)

# -----------------------------------
# Main Title
# -----------------------------------

st.title("🤖 AI Procurement Intelligence Dashboard")

st.write(
    "Upload procurement documents (PDF/HTML) "
    "to extract structured bid information."
)

# -----------------------------------
# File Upload
# -----------------------------------

uploaded_files = st.file_uploader(
    "Upload Files",
    type=["pdf", "html"],
    accept_multiple_files=True
)

# -----------------------------------
# Process Files
# -----------------------------------

if uploaded_files:

    all_text = ""

    file_count = 0

    for uploaded_file in uploaded_files:

        suffix = os.path.splitext(
            uploaded_file.name
        )[1]

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix
        ) as temp_file:

            temp_file.write(
                uploaded_file.read()
            )

            temp_path = temp_file.name

        # PDF
        if uploaded_file.name.endswith(".pdf"):

            text = extract_text_from_pdf(
                temp_path
            )

        # HTML
        elif uploaded_file.name.endswith(".html"):

            text = extract_text_from_html(
                temp_path
            )

        else:

            text = ""

        all_text += text + "\n"

        file_count += 1

    # -----------------------------------
    # Extraction
    # -----------------------------------

    structured_data = extract_bid_info(
        all_text
    )

    # -----------------------------------
    # Success Message
    # -----------------------------------

    st.success(
        f"Processed {file_count} files successfully!"
    )

    # -----------------------------------
    # Metrics
    # -----------------------------------

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Files Processed",
        file_count
    )

    col2.metric(
        "Fields Extracted",
        len(structured_data)
    )

    col3.metric(
        "Company",
        structured_data.get(
            "company_name",
            "N/A"
        )
    )

    # -----------------------------------
    # JSON View
    # -----------------------------------

    st.header("📌 Extracted Information")

    st.json(structured_data)

    # -----------------------------------
    # Structured Table
    # -----------------------------------

    st.header("📊 Structured Table")

    st.table(
        {
            "Field": structured_data.keys(),
            "Value": structured_data.values()
        }
    )

    # -----------------------------------
    # AI Summary
    # -----------------------------------

    st.header("🤖 AI Summary")

    st.info(
        structured_data.get(
            "bid_summary",
            "No summary available."
        )
    )

    # -----------------------------------
    # Download JSON
    # -----------------------------------

    json_data = json.dumps(
        structured_data,
        indent=4
    )

    st.download_button(
        label="⬇ Download JSON",
        data=json_data,
        file_name="output.json",
        mime="application/json"
    )

# -----------------------------------
# Footer
# -----------------------------------

st.markdown("---")

st.caption(
    "Built using Python, Streamlit, NLP, and AI-based document extraction."
)