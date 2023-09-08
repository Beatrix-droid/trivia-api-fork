import requests
import json
from time import sleep


# url="https://the-trivia-api.com/v2/questions?tags=food&limit=1"

# questions=[]
# i = 0
# while i < 300:

#         r= requests.get(url, timeout=5)
#         question= r.json()[0]
#         print(question)

#         if question in questions:
#             print("it's already here")
#         else:
#             print("new question, adding it to the list if questions")
#             questions.append(question)
#         i+=1
#         print(i)
#         sleep(2)

#     # write the set of questions to a json file
# json_questions=json.dumps(questions, indent=4)
# with open ("questions.json", "w") as file:
#         file.write(json_questions)

# with open ("public/questions/italianTranslation.json", "r") as jsonfile:
#     data=json.load(jsonfile)
#     with open("domande.txt", "w") as textfile:
#         textfile.write("totale domande: "+ str(len(data))+ "\n")
#         for question in data:
#             textfile.write("\n")
#             textfile.write(f"{data.index(question)+ 1}:  {question['question']['text']} \n")
#             textfile.write(f"   risposta corretta: {question['correctAnswer']} \n")
#             textfile.write(f"   risposte sbagliate: {question['incorrectAnswers']} \n")



Lokal_questions=[]

question_blueprint={
  "category": "società_e_cultura",
  "id": "622a1c3d7cc59eab6f951c17",
  "correctAnswer": "Rapa",
  "incorrectAnswers": [
    "zucche",
    "Patata",
    "Carota"
  ],
  "question": {
    "text": "Da cosa furono realizzate le prime Jack-o-Lantern?"
  },
  "tags": [
    "cibo",
    "Halloween",
    "tradizioni",
    "società_e_cultura"
  ],
  "type": "scelta_testo",
  "difficulty": "difficile",
  "regions": [],
  "isNiche": False
}
r=requests.get("https://server.opexams.com/quiz-data/EkUQ0vM8wX2", timeout=5)
data=r.json()
generated_questions=data["questions"]
for question in generated_questions:
    question.pop("id")
    domanda=question["question"]
    risposta_corretta=question["answer"]
    options=question["options"]
    wrong_answers=[option["value"] for option in options]
    wrong_answers.remove(risposta_corretta)


    # build the json object:
    question_object={
                      "category": "any string is fine",
                      "id": "any string is fine",
                      "correctAnswer": risposta_corretta,
                      "incorrectAnswers": wrong_answers,
                      "question": {
                                    "text": domanda
                                   },
                      "tags": [
                                "cibo",
                                "whatever",
                                "you ",
                                "want"
                                ],
                      "type": "scelta_testo",
                      "difficulty": "difficile",
                      "regions": [],
                      "isNiche": False
                    }   
    Lokal_questions.append(question_object)

Lokal_questions_json=json.dumps(Lokal_questions, indent=4)
with open("lokal-questions.json", "w") as file:
    file.write(Lokal_questions_json)
    
  #  print(wrong_answers)
#print(generated_questions)


# with open("domande-Lokal.txt", "w") as textfile:
#         textfile.write("totale domande: "+ str(len(data["questions"]))+ "\n")
#         for question in data["questions"]:
#             questionBody=question["question"]
#             answer=question["answer"]
#             wrong_answers=question["options"]["value"]
#             textfile.write("\n")
#             textfile.write(f"{data['questions'].index(question)+ 1}:  {questionBody} \n")
#             textfile.write(f"   risposta corretta: {answer} \n")
#             textfile.write(f"   risposte sbagliate: {wrong_answers} \n")
