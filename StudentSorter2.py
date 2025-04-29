from tkinter import *
from tkinter import ttk, messagebox
import json

def studentsorter(ogfile,newfile):
    # open the file
    with open(ogfile, 'r') as file:
        students = json.load(file)

    # creating a list of names and their average grades
    st_avg = []
    for key, data in students.items():
        name = data["Name"]
        grades = [value for k, value in data.items() if k != "Name"]
        avg_grade = sum(grades) / len(grades)
        st_avg.append((key, name, avg_grade, data))

    # sorting using selection sort
    n = len(st_avg)
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if st_avg[j][2] > st_avg[max_index][2]:
                max_index = j
        st_avg[i], st_avg[max_index] = st_avg[max_index], st_avg[i]

    #  make the new ordered data
    st_sorted = {}
    for i, (key, name, avg, data) in enumerate(st_avg, 1):
        st_sorted[f"Student{i}"] = data

    # put it in the new file
    with open(newfile, 'w') as file:
        json.dump(st_sorted, file, indent=4)



#Student sorter interface
win = Tk()
win.title("Student Sorter")
# Set the geometry of tkinter frame
win.geometry("400x200")
win.resizable(False, False)

# Create a button to start the sorting
button = ttk.Button(win, text="Sort", command=studentsorter('student_database.txt', 'student_database_sorted.txt')).pack(pady=10)

win.mainloop()