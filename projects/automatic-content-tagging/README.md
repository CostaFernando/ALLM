# Automatic Content Tagging using LLMs

## Introduction

This repository contains the code and associated data for a project involving the use of Large Language Models (LLMs) for the task of Automatic Content Tagging. Specifically, we are exploring the tagging of exam content based on pre-defined skills and knowledge areas. This project is specifically focused on the ENEM exams.

## Project Structure

The repository is structured as follows:

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

## Usage

This project is designed to train a Large Language Model to automatically tag questions from the ENEM exams based on their content. The main script reads in the `ENEM_tagged_questions.csv` file and uses the question text and associated tags to train the model. The model can then be used to predict the tags for new, untagged questions.

The `ENEM_Reference_Matrix.csv` file serves as a reference for understanding the meaning of the tags and the skills they represent.

## Acknowledgements

This project used ENEM's microdata, which is available at: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem.
