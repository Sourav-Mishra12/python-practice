import numpy as np

#students_marks = [45, 67, 67, 72, 55, 80, 90, 67, 75, 60]

#print(f"The average performance of this naughty class is : {np.mean(students_marks)} , they need to study hard!!")
#print(f"The middle performer of this class is {np.median(students_marks)} , haha no wonder he's from MIDDLE east!!")
#values , counts = np.unique(students_marks , return_counts=True)
#max_count = np.max(counts)
#modes = values[counts == max_count]

#print(f"The most frequent score for this class is : {modes} , should've scored 2 marks more")



#temp = [28, 30, 31, 33, 29, 30, 31]

#print(f"My goodness the average temperature was :{np.ceil(np.mean(temp))} , DAMMNN")
#print(f"The MIDDLE east of temps is here : {np.median(temp)} , NICEE")
#values , counts = np.unique(temp , return_counts=True)
#mode_temp = values[counts == np.max(counts)]
#print(f"Here comes the repetitor : {mode_temp} , don't repeat be unique ")


#factory_productions = [29,78,88,99,120,31,56,87]

#mean = np.mean(factory_productions)
#median= np.median(factory_productions)
#values,counts = np.unique(factory_productions , return_counts = True)
#mode = values[counts == np.max(counts)]

#print("MEAN" ,mean)
#print("MEDIAN" , median)
# print("MODE" , mode)


shoe_sizes = [8, 8, 9, 9, 9, 10, 10, 11, 8, 9]

mean =  np.mean(shoe_sizes)
median = np.median(shoe_sizes)
values , counts = np.unique(shoe_sizes , return_counts= True)
mode =  values[counts == np.max(counts)]

print("mean:",mean)
print("median:",median)
print("mode:",mode)
print("THE MODE IS THE BEST FOR THE COMPANY FOR ANALYSIS")


