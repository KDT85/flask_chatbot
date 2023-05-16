import chat_functions
import q_a_string
import tkinter as tk

import webbrowser

import logging
#set up the log config
logging.basicConfig(filename = "chatbot_log.log", level=logging.INFO, 
                    format='%(asctime)s - %(message)s')


# prossesss the question and answer strings into a list of dictionary question and answer pairs
Q = chat_functions.remove_stopwords(q_a_string.Q.lower())
Q = chat_functions.lemmatize_word(Q)

questions = Q.split('?')
answers = q_a_string.A.split('\n')
qa_pairs = []

for i in range(len(questions)):
    qa_pair = {"question": questions[i], "answer": answers[i]}
    qa_pairs.append(qa_pair)


# Define a function to process user input
def process_user_input(user_input_raw):
    status = bool
    user_input = chat_functions.remove_stopwords(user_input_raw)
    user_input = chat_functions.lemmatize_word(user_input)
    print(user_input)

    # find the best matching question-answer pair
    best_match_pair = chat_functions.find_best_match(user_input, qa_pairs)

    # if a best matching question-answer pair was found, retrieve the answer and extract named entities
    if best_match_pair is not None:
        answer = best_match_pair["answer"]
        response = answer
        status = True
    
    elif user_input in ["cheers", "thanks", "thank you", "nice one"]:
        response = "You're welcome!"
        status = True

    else:
        response = "I'm sorry, I couldn't understand your question. Can you please try again?"
        status = False
    #print(response)
    log = f"{status} - {user_input_raw} - {user_input} - {response}"
    logging.info(log)
    return response

# Help function
def help():
    webbrowser.open('https://www.staffs.ac.uk/students/course-administration/frequently-asked-questions')
