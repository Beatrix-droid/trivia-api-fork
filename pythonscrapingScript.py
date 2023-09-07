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

with open ("public/questions/italianTranslation.json", "r") as jsonfile:
    data=json.load(jsonfile)
    with open("domande.txt", "w") as textfile:
        textfile.write("totale domande: "+ str(len(data))+ "\n")
        for question in data:
            textfile.write("\n")
            textfile.write(f"{data.index(question)+ 1}:  {question['question']['text']} \n")
            textfile.write(f"   risposta corretta: {question['correctAnswer']} \n")
            textfile.write(f"   risposte sbagliate: {question['incorrectAnswers']} \n")