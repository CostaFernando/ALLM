# Automatic Content Tagging using LLMs

## Introduction

This repository contains the code and associated data for a project involving the use of Large Language Models (LLMs) for the task of Automatic Content Tagging. Specifically, we are exploring the tagging of exam content based on pre-defined skills and knowledge areas. This project is specifically focused on the ENEM exams.

## Data

- `ENEM_tagged_questions.csv` - This file contains tagged questions from the ENEM exams. The columns include:

  - `Year`: The year the exam was administered
  - `Discipline`: The general discipline or subject area associated with the question
  - `SG_AREA`: The knowledge area associated with the question. The possible values are:
    - CH: Humanities
    - CN: Natural Sciences
    - LC: Language and Codes
    - MT: Mathematics and Technologies
  - `TX_COR`: The color of the test booklet (Azul indicates a blue booklet)
  - `CO_PROVA`: The unique code of the exam
  - `Question_Number`: The sequence number of the question within the exam
  - `Question_Text`: The text of the question itself
  - `Skill_Number`: The code representing the ability or skill that the question is designed to test

- `ENEM_Reference_Matrix.csv` - This file serves as a reference for the skills tested by the ENEM exams. The columns include:
  - `Discipline`: The general discipline or subject area associated with the skill
  - `Skill_Number`: The unique number assigned to the skill
  - `Skill_Description`: A detailed description of the skill

## Streamlit App

Our Streamlit application provides a user-friendly interface for automatic content tagging. It allows you to upload a CSV file of exam questions without assigned skills, along with a CSV file of potential skills. The application will then generate embeddings for both the questions and skills using a large language model, match each question to the most relevant skill, and return a downloadable CSV file with the predicted skill for each question.

<img width="748" alt="image" src="https://github.com/CostaFernando/ALLM/assets/17749414/f7fc4914-e57c-4047-be0c-8e1e824c863d">

### Setting up and Running the App

To run this application locally, follow these steps:

1. **Create a Python virtual environment**:

A virtual environment is an isolated Python environment that allows you to install specific versions of packages without affecting your system-wide Python setup. To create a virtual environment, navigate to the `streamlit-app` directory in your terminal and enter the following command:

```bash
python3 -m venv venv
```

This will create a new virtual environment in a folder named `venv` within your current directory.

2. **Activate the virtual environment**:

Before installing any packages or running the app, you'll need to activate your virtual environment. You can do so with the following command:

- On Unix or MacOS, enter:

  ```bash
  source venv/bin/activate
  ```

- On Windows, enter:
  ```bash
  .\venv\Scripts\activate
  ```

3. **Install the necessary packages**:

You can install all the necessary Python packages using the `requirements.txt` file included in the `streamlit-app` directory. Enter the following command in your terminal:

```bash
pip install -r requirements.txt
```

This will install all required packages in your virtual environment.

4. **Set up environment variables**:

Copy the `.env.example` file and rename it to `.env`. Fill in the necessary environment variables.

5. **Run the Streamlit app**:

Now you're ready to run the app! Enter the following command in your terminal:

```bash
streamlit run app.py
```

This will start the Streamlit server and open the app in a new tab in your default web browser. If it doesn't open automatically, you can manually navigate to `http://localhost:8501`.

The application will prompt you to upload two CSV files. The first should contain the exam questions you want to tag, and the second should contain the list of potential skills. After you upload these files, the app will process them and provide a link to download a new CSV file. This file will contain your original questions, along with the predicted skill for each one.

## Acknowledgements

This project used ENEM's microdata, which is available at: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem.
