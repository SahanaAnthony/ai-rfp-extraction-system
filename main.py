import os
import json

from src.pdf_parser import extract_text_from_pdf
from src.html_parser import extract_text_from_html
from src.extractor import extract_bid_info
from src.llm_processor import generate_bid_summary


DATA_FOLDER = "data"

all_text = ""
file_count = 0

for file in os.listdir(DATA_FOLDER):

    file_path = os.path.join(DATA_FOLDER, file)

    # PDF files
    if file.endswith(".pdf"):

        print(f"Reading PDF: {file}")

        text = extract_text_from_pdf(file_path)

        all_text += text + "\n"
        file_count += 1

    # HTML files
    elif file.endswith(".html"):

        print(f"Reading HTML: {file}")

        text = extract_text_from_html(file_path)

        all_text += text + "\n"
        file_count += 1
       

print(f"\nProcessed {file_count} files successfully.")

print("Text extraction completed successfully.")

structured_data = extract_bid_info(all_text)

summary = generate_bid_summary(all_text)

print("\n========== STRUCTURED DATA ==========\n")

final_output = {
    "metadata": structured_data,
    "ai_summary": summary
}

print("Structured data extracted successfully.")
print("\nExtracted Information:")

for key, value in structured_data.items():

    print(f"{key}: {value}")

with open("output/output.json", "w") as f:

    json.dump(final_output, f, indent=4)

print("\nJSON file saved successfully!")

