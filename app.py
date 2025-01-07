# Main application for TalentScout Hiring Assistant Chatbot

import streamlit as st
from prompt_Design import generate_prompt
from tech_question_generator import generate_questions_from_tech_stack_and_experience
from context_manager import handle_context
from data_handler import save_candidate_info


# # Greeting Function
# def greeting():
#     return "Welcome to TalentScout Hiring Assistant! I will assist you in the initial screening process. Let's get started."

# def collect_information():
#     st.header("Candidate Information")
#     full_name = st.text_input("Full Name")
#     email = st.text_input("Email Address")
#     phone_number = st.text_input("Phone Number")
#     experience = st.slider("Years of Experience", 0, 30, 1)
#     position = st.text_input("Desired Position")
#     location = st.text_input("Current Location")
#     tech_stack = st.text_area("Tech Stack (e.g., Python, Django, PostgreSQL, AWS)")

#     if st.button("Submit Information"):
#         if not (full_name and email and phone_number and tech_stack):
#             st.warning("Please fill out all mandatory fields.")
#         else:
#             st.success("Information successfully recorded.")
#             return {
#                 "full_name": full_name,
#                 "email": email,
#                 "phone_number": phone_number,
#                 "experience": experience,
#                 "position": position,
#                 "location": location,
#                 "tech_stack": tech_stack.split(', ')
#             }

# def main():
#     st.title("TalentScout - Hiring Assistant Chatbot")
#     st.markdown("Welcome to TalentScout Hiring Assistant! I will assist you in the initial screening process. Let's get started.")
    
#     candidate_info = collect_information()

#     if candidate_info:
#         tech_stack = candidate_info.get("tech_stack", [])
#         questions = generate_questions(tech_stack, candidate_info["experience"])

#         if questions:
#             st.session_state.current_question_index = 0  
#             st.session_state.current_tech_index = 0  
#             st.session_state.answers = []  

#             # Start asking questions
#             ask_question(questions, candidate_info)

#         if "current_question_index" in st.session_state and st.session_state.current_question_index >= len(questions):
#             st.write("You've completed all the questions. Thank you for your time!")
#             st.session_state.clear()  # Clear session state at the end of conversation

#     if st.button("End Conversation"):
#         st.write("Thank you for using the TalentScout Hiring Assistant. Have a great day!")
#         st.session_state.clear()  # Clear session state when conversation ends

# def ask_question(questions, candidate_info):
#     current_tech_index = st.session_state.current_tech_index
#     tech = list(questions.keys())[current_tech_index]  # Get the current tech stack
#     current_question_index = st.session_state.current_question_index
#     question = questions[tech][current_question_index]

#     st.write(f"Bot: {question}")

#     user_input = st.text_area("Your answer: ", key="user_input")

#     if user_input:
#         # Record the answer
#         st.session_state.answers.append({"tech": tech, "question": question, "answer": user_input})

#         # Buttons for next question or end conversation
#         col1, col2 = st.columns(2)

#         with col1:
#             if st.button("Next Question"):
#                 # Move to the next question
#                 st.session_state.current_question_index += 1
#                 ask_question(questions, candidate_info)  # Ask the next question

#         with col2:
#             if st.button("End Conversation"):
#                 # Save candidate answers and end conversation
#                 save_candidate_info({
#                     "name": candidate_info["full_name"],
#                     "email": candidate_info["email"],
#                     "phone": candidate_info["phone_number"],
#                     "experience": candidate_info["experience"],
#                     "tech_stack": candidate_info["tech_stack"],
#                     "answers": st.session_state.answers
#                 })
#                 st.write("You've completed all the questions. Thank you for your time.")
#                 st.session_state.clear()  # Clear session state after ending conversation

#         # After answering all questions for the current tech stack
#         if current_question_index + 1 == len(questions[tech]):
#             if current_tech_index + 1 < len(questions):
#                 # Move to the next tech stack's questions
#                 st.session_state.current_question_index = 0  # Reset question index for the next tech stack
#                 st.session_state.current_tech_index += 1  # Move to the next tech stack
#                 ask_question(questions, candidate_info)  # Ask first question for the next tech stack
#             else:
#                 st.write("You've completed all the questions. Thank you for your time!")
#                 st.session_state.clear()  # Clear session state after all questions

# if __name__ == "__main__":
#     main()

# Initialize Streamlit app
st.set_page_config(page_title="TalentScout Hiring Assistant")
st.title("TalentScout Hiring Assistant")
st.write("Welcome to TalentScout! I am here to help screen candidates for technology roles.")

# Define session state
if 'conversation' not in st.session_state:
    st.session_state['conversation'] = []
if 'questions' not in st.session_state:
    st.session_state['questions'] = []
if 'answers' not in st.session_state:
    st.session_state['answers'] = []
if 'current_question' not in st.session_state:
    st.session_state['current_question'] = 0

# Function to handle question-answer flow
def next_question():
    if st.session_state['current_question'] < len(st.session_state['questions']) - 1:
        st.session_state['current_question'] += 1

def end_conversation():
    # Save all data
    candidate_data = {
        "name": st.session_state.get('name', ""),
        "email": st.session_state.get('email', ""),
        "phone": st.session_state.get('phone', ""),
        "experience": st.session_state.get('experience', 0),
        "position": st.session_state.get('position', ""),
        "location": st.session_state.get('location', ""),
        "tech_stack": st.session_state.get('tech_stack', ""),
        "questions_and_answers": list(zip(st.session_state['questions'], st.session_state['answers']))
    }
    save_candidate_info(candidate_data)
    st.success("Thanks for submitting your answers! Your responses have been saved.")

# Candidate Details Input
st.write("## Candidate Details")
with st.form("candidate_form"):
    st.session_state['name'] = st.text_input("Full Name")
    st.session_state['email'] = st.text_input("Email Address")
    st.session_state['phone'] = st.text_input("Phone Number")
    st.session_state['experience'] = st.number_input("Years of Experience", min_value=0, max_value=50, step=1)
    st.session_state['position'] = st.text_input("Desired Position")
    st.session_state['location'] = st.text_input("Current Location")
    st.session_state['tech_stack'] = st.text_area("Tech Stack (comma-separated)")
    save_info = st.form_submit_button("Save Details")

if save_info:
    # Generate unique questions for each tech stack item
    st.session_state['questions_by_stack'] = generate_questions_from_tech_stack_and_experience(st.session_state['tech_stack'])
    st.session_state['current_stack'] = list(st.session_state['questions_by_stack'].keys())
    st.session_state['current_index'] = 0
    st.session_state['answers_by_stack'] = {stack: [] for stack in st.session_state['current_stack']}
    st.success("Candidate information saved. Start answering the questions!")

# Question and Answer Flow
if 'questions_by_stack' in st.session_state and st.session_state['current_stack']:
    current_stack = st.session_state['current_stack'][st.session_state['current_index']]
    questions = st.session_state['questions_by_stack'][current_stack]

    st.write(f"### Questions for {current_stack}")
    for i, question in enumerate(questions, 1):
        st.write(f"**Q{i}:** {question}")
    
    with st.form(f"answer_form_{current_stack}"):
        answers = [st.text_area(f"Answer for Q{i+1}") for i in range(len(questions))]
        next_clicked = st.form_submit_button("Next Stack")
        submit_clicked = st.form_submit_button("Submit All Answers")

        if next_clicked:
            # Save answers for the current stack
            st.session_state['answers_by_stack'][current_stack] = answers
            if st.session_state['current_index'] < len(st.session_state['current_stack']) - 1:
                st.session_state['current_index'] += 1
            else:
                st.info("You have answered all questions for all tech stacks. Submit your responses.")
        
        if submit_clicked:
            # Save all data, including questions and answers
            candidate_data = {
                "name": st.session_state.get('name', ""),
                "email": st.session_state.get('email', ""),
                "phone": st.session_state.get('phone', ""),
                "experience": st.session_state.get('experience', 0),
                "position": st.session_state.get('position', ""),
                "location": st.session_state.get('location', ""),
                "tech_stack": st.session_state.get('tech_stack', ""),
                "questions_and_answers": st.session_state['answers_by_stack']
            }
            save_candidate_info(candidate_data)
            st.success("Thanks for submitting your answers! Your responses have been saved.")