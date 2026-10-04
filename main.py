from question import questions
name = input("whats your name?")

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