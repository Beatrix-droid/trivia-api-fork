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

r=requests.get("https://server.opexams.com/quiz-data/EkUQ0vM8wX2", timeout=5)
data=r.json()
print(data)

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
