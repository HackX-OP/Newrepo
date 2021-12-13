def student():
    rno=int(input("Enter rno: "))
    name=input("Enter name: ")
    print("*******************")
    print(rno,".",name)
    print("*******************")


def faculty():
    name=input("Enter name of faculty: ")
    sub=input("Enter course of faculty: ")
    print("**************************************")
    print("Sub name=",sub,"Faculty name=",name)
    print("**************************************")

def exams():
    sub1=input("Enter test subject: ")
    num=int(input("Enter total marks in exam: "))
    print("**************************************")
    print("Sub=",sub1,"Total marks=",num)
    print("**************************************")

def result():
    marks=int(input("Enter marks obtained: "))
    print("**************************************")
    print("Marks obtained=",marks)
    print("**************************************")

def college():
    student()
    faculty()
    exams()
    result()

college()