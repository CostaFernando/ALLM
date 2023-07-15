import streamlit as st
import pandas as pd
import numpy as np
from numpy.linalg import norm
import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Set the OpenAI API key.
openai.api_key = os.getenv('OPENAI_API_KEY')

def cosine_similarity(a, b):
    return np.dot(a, b)/(norm(a)*norm(b))

# Define the function for getting embeddings.
def get_embedding(texts, model="text-embedding-ada-002"):
    texts = [text.replace("\n", " ") for text in texts]

    embeddings = openai.Embedding.create(input = texts, model=model)['data']
    embeddings = [embedding['embedding'] for embedding in embeddings]

    return embeddings

# Define the function to predict skill.
def predict_skill(question_embedding, reference_matrix):
    similarities = [cosine_similarity(question_embedding, skill_embedding) for skill_embedding in reference_matrix['Skill_Embedding']]
    top_skill_index = np.argmax(similarities)
    return reference_matrix.iloc[top_skill_index]['Skill_Number']

def main():
    st.title('Skill Matcher for Questions')

    st.markdown('Upload a CSV file containing questions and another one containing potential skills. The application will match each question with the best skill.')
    st.markdown('The CSV file with questions should have a column named `Question_Text` containing the text of the question.')
    st.markdown('The CSV file with skills should have a column named `Skill_Description` containing the text of the skill and a column named `Skill_Number` containing the number of the skill.')

    questions_file = st.file_uploader('Upload questions CSV', type='csv')
    skills_file = st.file_uploader('Upload skills CSV', type='csv')

    if questions_file and skills_file:
        questions_df = pd.read_csv(questions_file)
        reference_matrix_df = pd.read_csv(skills_file)

        st.write('Processing... This may take a while for large datasets.')

        # Get the embeddings for the skills and the questions.
        reference_matrix_df['Skill_Embedding'] = get_embedding(reference_matrix_df['Skill_Description'].tolist())
        questions_df['Question_Embedding'] = get_embedding(questions_df['Question_Text'].tolist())

        # Predict the best skill for each question.
        questions_df['Predicted_Skill'] = questions_df['Question_Embedding'].apply(predict_skill, reference_matrix=reference_matrix_df)
        
        questions_df = questions_df.drop(columns=['Question_Embedding'])
        
        # Save the dataframe with predictions to a CSV file.
        questions_df.to_csv('questions_with_skills.csv', index=False)

        st.write('Processing complete! Download the CSV file with the predicted skills for each question below.')
        st.download_button(
            label="Download CSV with Skills",
            data=open('questions_with_skills.csv', 'r').read(),
            file_name="questions_with_skills.csv",
            mime="text/csv"
        )

if __name__ == '__main__':
    main()
