import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer,AutoModelForSeq2SeqLM

# model_name = "gpt2"  
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name)
# def generate_questions(tech_stack, experience):
#     st.header("Technical Questions")
#     if not tech_stack:
#         st.warning("No tech stack provided to generate questions.")
#         return {}

#     questions = {}
#     for tech in tech_stack:
#         prompt = (f"Create 3-5 intermediate-level technical interview questions for the technology: {tech}, considering the candidate has {experience} years of experience.")
        
#         # Tokenize input
#         inputs = tokenizer.encode(prompt, return_tensors="pt")
        
#         # Generate response using the generate() method
#         outputs = model.generate(inputs, max_length=500, num_return_sequences=1, temperature=0.7)
        
#         # Decode and split the response
#         response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
#         # Split by newlines and store
#         questions[tech] = response.split('\n')

#     return questions

# def display_questions(questions):
#     if questions:
#         for tech, qs in questions.items():
#             st.subheader(f"Questions for {tech}")
#             for idx, question in enumerate(qs):
#                 st.write(f"{idx + 1}. {question}")
model_name = "google/flan-t5-large"  # You can use 'flan-t5-base' or 'flan-t5-large' for more capabilities
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
def generate_questions_from_tech_stack_and_experience(tech_stack):
    """
    Generate distinct and contextual technical questions for each item in the tech stack.
    """
    questions_by_stack = {}

    for tech in tech_stack.split(","):
        tech = tech.strip()  # Clean whitespace
        if not tech:
            continue

        # Define distinct prompts for better variability
        input_prompts = [
            f"Generate three technical interview questions for a candidate proficient in {tech}.",
            f"Create three advanced technical questions to test a candidate's problem-solving skills in {tech}.",
            f"List three interview questions that assess a candidate's practical experience with {tech} in large-scale applications.",
        ]

        questions = set()  # Use a set to ensure unique questions

        for prompt in input_prompts:
            try:
                # Encode the input prompt and generate output
                inputs = tokenizer.encode(prompt, return_tensors="pt", max_length=512, truncation=True)
                outputs = model.generate(inputs, max_length=512, num_return_sequences=1, temperature=0.7)
                generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

                # Split the generated response into questions
                questions.update([q.strip() for q in generated_text.split("\n") if q.strip()])
            except Exception as e:
                questions.add(f"Error generating questions for {tech}: {e}")

        # Ensure at least 3 unique questions for the stack item
        # while len(questions) < 4:
        #     questions.add(f"What are the most common challenges faced when working with {tech}?")

        # Convert set to list and store in the result dictionary
        questions_by_stack[tech] = list(questions)[:3]

    return questions_by_stack