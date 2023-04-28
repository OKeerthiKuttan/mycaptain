import csv
import os

def inputs():
    rollno = input("Enter Roll No: ")
    name = input("Enter Name: ")
    score = input("Enter CGPA: ")
    grade = input("Enter Year of Study: ")
    print("One Students Data Added")
    return [rollno, name, score, grade]

def process(students):
    if os.path.isfile("admindata.csv"):
        with open("admindata.csv", mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for student in students:
                writer.writerow(student)
    else:
        with open("admindata.csv", mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Roll No", "Name", "CGPA", "Year of Study"])
            for student in students:
                writer.writerow(student)

def dataread():
    data = []
    if os.path.isfile("admindata.csv"):
        with open("admindata.csv", mode='r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                data.append(row)
        return data
    

#Driver Code
while True:
    studData = dataread()
    x = int(input("1. Add Student\n2. Display Student Records\n3. Exit\n"))
    print()
    if x == 1:
        num = int(input("Enter number of students: "))
        data = []
        for i in range(num):
            data.append(inputs())
        process(data)
    elif x == 2:
        data = dataread()
        print("Roll No||Name||CGPA||Year of Study")
        for i in data:
            for j in i:
                print(j, end="||")
            print()
    elif x == 3:
        break
    

