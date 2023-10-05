import json



list_of_questions=[]



with open ("txt docs/domande.txt", "r") as file:
    questions=file.read()
    
    # clean the question list and put it into json
    raw_question_list=questions.split("\n----------\n")
    question_list=[question.replace("\n"," ") for question in raw_question_list]
    

    for question in question_list[:-1]:
        #isolate the actual question
        question_parts=question.split("A)")
        question_text=question_parts[0]
        
        #isolate the multiple option parts
        question_options=question_parts[1].split("B)")
        option_A=question_options[0]
        
        question_parts_2=question_options[1].split("C)")
        option_B=question_parts_2[0]

        question_parts_3=question_parts_2[1].split("D)")
        option_C=question_parts_3[0]
        option_D=question_parts_3[1]

        #locate the correct answer
        if "✔" in option_A:
            correct_answer=option_A.strip("✔")
            incorrect_answers=[option_B, option_C, option_D]
        elif"✔" in option_B:
            correct_answer=option_B.strip("✔")
            incorrect_answers=[option_A, option_C, option_D]
        elif"✔" in option_C:
            correct_answer=option_C.strip("✔")
            incorrect_answers=[option_A, option_B, option_D]
        elif"✔" in option_D:
            correct_answer=option_D.strip("✔")
            incorrect_answers=[option_A, option_B, option_C]

        question_obj={
        "category": "society_and_culture",
        "id": "622a1c3d7cc59eab6f951c17",
        "correctAnswer": f"{correct_answer}",
        "incorrectAnswers": [
            f"{incorrect_answers[0]}",
            f"{incorrect_answers[1]}",
            f"{incorrect_answers[2]}"
        ],
        "question": {
            "text": f"{question_text}"
        },
        "tags": [
            "food",
            "halloween",
            "traditions",
            "society_and_culture"
        ],
        "type": "text_choice",
        "difficulty": "hard",
        "regions": [],
        "isNiche": False
    }
        
    list_of_questions.append(question_obj)


json_list_of_questions=json.dumps(list_of_questions, indent=4)
with open("lokal-questions.json","w") as outfile:
    outfile.write(json_list_of_questions)
