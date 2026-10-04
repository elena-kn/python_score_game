from question import questions


print("welcom")

score = 0

for item in questions :
    answer = input(item["question"])
    if answer.lower() == item["answer"]:
        print("correct")
        score += 1
    else:
        print("wrong")

print("your score is:", score)