test1_score = float(input("What is your score for Test 1: "))
test1_weightage = float(input("What is weightage for Test 1: "))

test2_score = float(input("What is your score for Test 2: "))
test2_weightage = float(input("What is weightage for Test 2: "))

test3_score = float(input("What is your score for Test 3: "))
test3_weightage = float(input("What is weightage for Test 3: "))

exam_score = float(input("What is your score for Exam: "))

test1_final = test1_score * test1_weightage / 100
test2_final = test2_score * test2_weightage / 100
test3_final = test3_score * test3_weightage / 100
exam_final = exam_score * 50 / 100

final_score = test1_final + test2_final + test3_final + exam_final

print("Your final score is", final_score)
