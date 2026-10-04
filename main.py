import os
from dotenv import load_dotenv
from question import questions
name = input("whats your name?")

load_dotenv()
admin_password = os.getenv("QUIZ_ADMIN_PASSWORD")
open_admin = input("do you want to open admin mode ? yes/no")
if open_admin.lower() == "yes":
    entered_password = input("enter admin password")
    if entered_password == admin_password:
        print("admin!  hi")
    else:
        print("wrong password")


print("welcom")

score = 0

for item in questions :
    answer = input(item["question"])
    if answer.lower() == item["answer"]:
        print("correct")
        score += 1
    else:
        print("wrong")

print("your score is:", score,"aut of",len(questions))
if score == len(questions):
    print("excelent job", name)
elif score >= 2:
    print("good job", name)
else:
    print("keep praticing", name)

with open("result.txt", "a") as file:
    file.write(f"{name} - {score} / {len(questions)}\n ")
