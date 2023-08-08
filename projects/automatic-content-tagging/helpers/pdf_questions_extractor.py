import re
import csv
from pdfminer.high_level import extract_text

def convert_pdf_to_markdown(pdf_path):
    # Convert PDF to text
    pdf_text = extract_text(pdf_path)
    # Roughly convert the text to markdown
    lines = pdf_text.split("\n")
    markdown_lines = []
    for line in lines:
        if line.strip() == '':
            continue
        if line.isupper():  # headings are usually in uppercase
            markdown_lines.append(f"## {line}")
        else:
            markdown_lines.append(line)
    return "\n".join(markdown_lines)

def extract_math_questions(markdown_content):
    # Extract questions based on segmentation patterns
    pattern_segmented = r"(Questão \d+ - Matemática e suas Tecnologias.*?)(?=Questão \d+ - Matemática e suas Tecnologias|## PROVA|$)"
    matches_segmented = re.findall(pattern_segmented, markdown_content, re.DOTALL)
    # Remove "Questão {number} - Matemática e suas Tecnologias" from the beginning of each question
    cleaned_questions = [re.sub(r"^Questão \d+ - Matemática e suas Tecnologias", "", question).strip() for question in matches_segmented]
    return cleaned_questions

def save_to_csv(questions, csv_path):
    # Prepare data for CSV
    csv_data = [["Question Number", "Question Content"]]
    for idx, question in enumerate(questions, 136):  # Starting from 136 as it's the starting number for these questions
        csv_data.append([f"Question {idx}", question])
    # Save data to CSV
    with open(csv_path, 'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(csv_data)

if __name__ == "__main__":
    # Convert PDF to Markdown
    markdown_content = convert_pdf_to_markdown("/path/to/your/pdf/file.pdf")
    # Extract math questions
    questions = extract_math_questions(markdown_content)
    # Save questions to CSV
    save_to_csv(questions, "/path/where/you/want/to/save.csv")
