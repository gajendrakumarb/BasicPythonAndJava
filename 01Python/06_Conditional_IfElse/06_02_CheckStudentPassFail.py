# WAP check student is pass or fail in 4 subjects
# if stud get less than 33% in any one of the subject, he considered fail
# Well as if total marks percentage less than 40 then he considered as fail
# consider each subject is off 100 marks
stud1_marks = [98,23,56,74]
stud2_marks = [46,33,37,34]
stud3_marks = [87,34,48,71]
print('student 1 marks : '+str(stud1_marks))
print('student 2 marks : '+str(stud2_marks))
print('student 2 marks : '+str(stud3_marks))

print("Checking student s is pass or fail")
if(stud3_marks[0]<33 or stud3_marks[1]<33 or stud3_marks[2]<33 or stud3_marks[3]<33):
    print("Marks in one or many subject are less than 33. Result : Fail ")
elif(sum(stud3_marks)/4*100<40):
    print("Total marks are less than 40 percent. Result : Fail")
else:
    print("Result: Pass")





