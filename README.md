Documentation for TalentScout Hiring Assistant Chatbot

Project Overview

The TalentScout Hiring Assistant Chatbot is designed to assist recruitment agencies by automating the initial screening process for candidates in technical roles. The chatbot dynamically generates technical interview questions based on the candidate's declared tech stack and years of experience. The system also allows candidates to submit answers for these questions interactively.

Features

1. Dynamic Question Generation

Generates unique technical questions for each tech stack item using a free, open-source LLM model (Flan-T5).

Ensures at least three distinct questions for each tech stack.

2. Interactive Answer Collection

Presents questions one tech stack at a time.

Allows candidates to submit answers for each tech stack interactively.

Provides an option to save all responses and conclude the interaction.

3. Personalized and Context-Aware Prompts

Prompts focus solely on tech stack and experience to create relevant and specific questions.

4. Data Handling

Saves candidate information, questions, and answers in a structured JSON file for future review.

Ensures data privacy and lightweight storage.

Code Breakdown

1. app.py

The main application file that:

Manages user interactions via the chatbot UI using Streamlit.

Handles question-answer flow for each tech stack.

Saves candidate responses and personal details.

Key Functions:

next_question(): Moves to the next tech stack.

end_conversation(): Saves all collected data and concludes the interaction.

2. tech_question_generator.py

Generates contextually relevant and unique technical questions using the Flan-T5 model from Hugging Face.

Key Features:

Dynamically crafts prompts for each tech stack.

Generates at least three unique questions per stack, ensuring fallback for lesser-known technologies.

3. data_handler.py

Manages storage and retrieval of candidate information and their responses.

Key Functions:

save_candidate_info(candidate_data): Stores candidate information and responses in a JSON file.

get_all_candidates(): Retrieves all stored candidate data.

delete_candidate(name): Deletes data for a specific candidate by name.

4. prompt_Design.py

Creates structured prompts tailored to the chatbot's current context.

Key Updates:

Improved logic to generate tech-stack-specific and experience-based prompts dynamically.

How It Works

Workflow

Candidate Details Collection:

The chatbot collects essential candidate details (name, email, experience, etc.) via a form.

Dynamic Question Generation:

Questions are generated for each tech stack item using tech_question_generator.py.

Each stack receives unique, non-repetitive questions.

Interactive Answer Submission:

Candidates answer questions one stack at a time.

They can navigate to the next stack or submit all responses.

Data Storage:

All information, including questions and answers, is stored securely in candidates_data.json.

Example Interaction

Input

Tech Stack: Python, React

Experience: 3 years

Generated Questions

Python:

How do you handle memory-intensive tasks in Python efficiently?

Explain the use of Python's asyncio module in real-world scenarios.

How do you debug and optimize slow Python scripts in large-scale applications?

React:

How do you manage side effects in React using hooks?

What are the challenges of server-side rendering (SSR) in React, and how do you address them?

How do you implement and optimize lazy loading in a React project?

Installation and Setup

1. Prerequisites

Python 3.8+

Required Python libraries (install via requirements.txt):

pip install -r requirements.txt

2. Running the Application

Navigate to the project directory:

cd path/to/project

Run the Streamlit app:

python -m streamlit run app.py

3. File Structure

project/
├── app.py
├── tech_question_generator.py
├── data_handler.py
├── prompt_Design.py
├── candidates_data.json
├── requirements.txt

Future Improvements

Advanced Question Customization:

Incorporate more specific prompts for niche technologies.

Answer Analysis:

Use LLMs to analyze candidate responses for quality and correctness.

Cloud Deployment:

Host the application on AWS or GCP for live usage.

Credits:

Hugging Face: For the Flan-T5 model.

Streamlit: For the interactive web interface.


