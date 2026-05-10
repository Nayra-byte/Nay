import matplotlib.pyplot as plt
students_names=["qw",'er','rt','yu','io','as','gh','nn']
students_marks=[1,2,3,4,5,6,7,8]
marks_perc=[]
for x in student_marks:
    res=(x/50)*100
    marks_perc.append(res)
print(marks_perc)
def marks_line_chart():
    plt.plot(students_names,students_marks)
    plt.title('students marks graphhhhhhhhhhhhhhhhhhhhhh')
    plt.xlabel('names')
    plt.ylabel('markssssssssssssssssssssssss')
    plt.show()
marks_line_chart()
#.............................................................................................................................................................................................................................................................................................................................................................
def percentage_bar_chart():
    plt.bar(students_names,marks_perc)
    plt.title('percentage graph of the students')
    plt.xlabel('names of students')
    plt.ylabel('percentage of students')
percentage_bar_chart()
