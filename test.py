subjectnum = 0
while subjectnum == ValueError or subjectnum == 0:
    try:
        subjectnum = int(input ("how many subjects?\n"))
        if subjectnum == 0:
            print("we can't help you.")
            break
    except ValueError:
        print("please input number.\n")


names = []
for subjectnum_follow in range(0, subjectnum):
    names.append(str(input("What's name of the subject number {}?\n" .format(subjectnum_follow + 1))))



scores = []
for subjectnum_follow in range(0, subjectnum):
    try:
         score = int(input("Whats your score for {}?\n" .format(names[subjectnum_follow])))
         scores.append(score)
         if score != ValueError:
              subjectnum_follow += 1
    except ValueError:
        print("please insert number.\n")

total_score = 0
for subjectnum_follow in range(0, subjectnum):
    total_score += scores[subjectnum_follow]

avr_score = total_score / subjectnum

for subjectnum_follow in range(0, subjectnum):
    print("subject ", subjectnum_follow, ": ", names[subjectnum_follow], "\nScore:", scores[subjectnum_follow], "\n\n")

if avr_score >= 90:
    grade = "A"
elif avr_score >= 80 and avr_score <= 89:
    grade = "B"
elif avr_score >= 70 and avr_score <= 79:
    grade = "C"
elif avr_score >= 60 and avr_score <= 69:
    grade = "D"
elif avr_score <= 59:
    grade = "F"
else:
    print("critical error")
    sys.exit()

print("Average score: ", (avr_score), "\nGrade: ", grade)