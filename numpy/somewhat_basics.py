import numpy as np

#students_marks = [45, 67, 67, 72, 55, 80, 90, 67, 75, 60]

#print(f"The average performance of this naughty class is : {np.mean(students_marks)} , they need to study hard!!")
#print(f"The middle performer of this class is {np.median(students_marks)} , haha no wonder he's from MIDDLE east!!")
#values , counts = np.unique(students_marks , return_counts=True)
#max_count = np.max(counts)
#modes = values[counts == max_count]

#print(f"The most frequent score for this class is : {modes} , should've scored 2 marks more")



temp = [28, 30, 31, 33, 29, 30, 31]
print(f"My goodness the average temperature was :{np.ceil(np.mean(temp))} , DAMMNN")
print(f"The MIDDLE east of temps is here : {np.median(temp)} , NICEE")
values , counts = np.unique(temp , return_counts=True)
mode_temp = values[counts == np.max(counts)]
print(f"Here comes the repetitor : {mode_temp} , don't repeat be unique ")