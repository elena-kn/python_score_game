print("welcom")

score = 0

answer = input("what language are we using?")
if answer.lower() == "python":
    print("bravo")
    score += 1

else:
    print("wrong")

print("your score is:", score)