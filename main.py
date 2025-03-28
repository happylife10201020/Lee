##
# 성적관리 프로그램
# 5명의 학생의 세개의 교과목 (영어, C-언어, 파이썬)에 대하여
# 키보드로부터 학번, 이름, 영어점수, C-언어 점수, 파이썬 점수를 입력받아 총점, 평균, 학점, 등수를 계산하는 프로그램 작성
# 입력 함수, 총점/평균 계산 함수,  학점계산 함수, 등수계산 함수, 출력 함수
# 삽입 함수, 삭제 함수, 탐색함수(학번, 이름), 정렬(총점)함수, 80점이상 학생 수 카운트 함수
# 지도교수 : 황경순
# 강의실 : S4-1 103호
# 2022041060 이인수
# #


#choice the options
def CHOICE():
    print("\n1. Add new Student")
    print("2. Remove Student")
    print("3. Print Student Details")
    print("4. Count students over 80 score")
    print("5. Search for Student")
    print("6. Sort")
    print("0 r. Exit")
    while 1:
        try:
            print("\n")
            number = int(input("Enter your choice: "))
            break
        except:
            print("Enter a valid choice")
    return number

#Get Details of New Std
def getStudentDetails():
    while True:
        try:
            StdNum = int(input("Enter Student Number: "))
            StdName = input("Enter Student Name: ")
            StdEngScore = int(input("Enter Student English Score: "))
            StdCScore = int(input("Enter Student C Score: "))
            StdPyScore = int(input("Enter Student Python Score: "))

            sumScore = StdEngScore + StdCScore + StdPyScore
            avgScore = sumScore / 3
            break
        except:
            print("Invalid Input")

    grade = getGrade(avgScore)
    student = {"StdNum": StdNum,
               "StdName": StdName,
               "StdEngScore": StdEngScore,
               "StdCScore": StdCScore,
               "StdPyScore": StdPyScore,
               "sumScore": sumScore,
               "avgScore": avgScore,
               "grade": grade,
               "rank":  1
               }
    return student

#Cal grade of std
def getGrade(avg):
    if avg >= 95:
        grade = 'A+'
    elif avg >= 90:
        grade = 'A'
    elif avg >= 85:
        grade = 'B+'
    elif avg >= 80:
        grade = 'B'
    elif avg >= 75:
        grade = 'C+'
    elif avg >= 70:
        grade = 'C'
    elif avg >= 65:
        grade = 'D+'
    elif avg >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade

#pop stdudent's inform by stdnumber
def removeStudent(students):
    while True:
        try:
            StudentNum = int(input("Enter Student Number: "))
            break
        except:
            print("Invalid Input")
    state = 1
    for student in students:
        if student["StdNum"] == StudentNum:
            students.pop(students.index(student))
            print("Student Deleted!\n")
            state = 0

    if state == 1:
        print("No such student exists!\n")

def printStudentDetails(students):
    if len(students) == 0:
        print("No students exists!\n")
        return

    for student in students:
        student["rank"] = 1

    for std1 in students:
        for std2 in students:
            if std1["avgScore"] < std2["avgScore"]:
                std1["rank"] = std1["rank"] + 1

    print("===============================================")
    headers = ["Name", "Num", "English Score", "C Score", "Python Score", "Sum", "Avg", "Grade", "Rank"]
    print("Name\tNum\tEng\tClan\tPy\tsum\tAvg\tGrade\tRank")
    print("===============================================")

    for student in students:
        print(f"{student['StdNum']}\t{student['StdName']}\t{student['StdEngScore']}\t{student['StdCScore']}\t{student['StdPyScore']}\t{student['sumScore']}"
            f"\t{student['avgScore']:.2f}\t{student['grade']}\t{student['rank']}")
        #tabulate(student, headers=headers, tablefmt="plain")


def countOver80(students):
    over80 = []
    for student in students:
        if student["avgScore"] >= 80:
            over80.append([student["StdNum"], student["StdName"], student["avgScore"]])

    print("\nStudent Over 80 : ", len(over80))
    for student in over80:
        print(f"학번 : {student[0]}\t 이름 : {student[1]}\t 평균 : {student[2]}")

def searchStudent(students):
    searchKey = input("Enter Student`s name or number: ")
    state = 1
    try:
        stdNum = int(searchKey)

        for student in students:
            if student["StdNum"] == stdNum:
                state = 0
                print(
                    f"{student['StdNum']}\t{student['StdName']}\t{student['StdEngScore']}\t{student['StdCScore']}\t{student['StdPyScore']}\t{student['sumScore']}"
                    f"\t{student['avgScore']:.2f}\t{student['grade']}\t{student['rank']}")
    except:
        stdName = searchKey
        for student in students:
            if student["StdName"] == stdName:
                state = 0
                print(
                    f"{student['StdNum']}\t{student['StdName']}\t{student['StdEngScore']}\t{student['StdCScore']}\t{student['StdPyScore']}\t{student['sumScore']}"
                    f"\t{student['avgScore']:.2f}\t{student['grade']}\t{student['rank']}")

    if state == 1:
        print("ERROR: No such student exists!\n")


def sortStudents(students):
    students.sort(key=lambda student: student["avgScore"], reverse=True)

def main():
    students = []
    while 1:
        number = CHOICE()
        if number == 0:
            print("Program Terminated!\n")
            break
        elif number == 1:
            students.append(getStudentDetails())
        elif number == 2:
            removeStudent(students)
        elif number == 3:
            printStudentDetails(students)
        elif number == 4:
            countOver80(students)
        elif number == 5:
            searchStudent(students)
        elif number == 6:
            sortStudents(students)
        else:
            print("Invalid Input\n")

if __name__ == '__main__':
    main()