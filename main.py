##
# 성적관리 프로그램
# 5명의 학생의 세개의 교과목 (영어, C-언어, 파이썬)에 대하여
# 키보드로부터 학번, 이름, 영어점수, C-언어 점수, 파이썬 점수를 입력받아 총점, 평균, 학점, 등수를 계산하는 프로그램 작성
# 지도교수 : 황경순
# 강의실 : S4-1 103호
# 2022041060 이인수
# #

def input_data():
    stdNumber = input("학번: ")
    stdName = input("이름: ")
    scoreEng = int(input("영어 점수: "))
    scoreC = int(input("C-언어 점수: "))
    scorePy = int(input("파이썬 점수: "))
    return stdNumber, stdName, scoreEng, scoreC, scorePy


def sum_avg(Eng, C, Py):
    sum = Eng + C + Py
    avg = sum / 3
    return sum, avg


def grade(avg):
    grade = ''
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

def rank(stdudents):
    for student in stdudents:
        student["rank"] = 1
    
    for std1 in stdudents:
        for std2 in stdudents:
            if std1["sum"] > std2["sum"]:
                std1["rank"] += 1

def prt(students):
    print("\n성적 결과")
    print("==================================================")
    print("학번\t\t\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
    print("==================================================")

    for student in students:
        print(f"{student['number']}\t{student['name']}\t{student['Eng']}\t{student['C']}\t"
              f"{student['Py']}\t{student['sum']}\t{student['avg']:.2f}\t{student['grade']}\t{student['rank']}")


def main():
    students=[]
    for i in range(5):
        stdNumber, stdName, scoreEng, scoreC, scorePy = input_data()
        student = {
            "number": stdNumber,
            "name": stdName,
            "Eng": scoreEng,
            "C": scoreC,
            "Py": scorePy
        }
        students.append(student)

    for student in students:
        student["sum"], student["avg"] = sum_avg(student["Eng"], student["C"], student["Py"])

    for student in students:
        student["grade"] = grade(student["avg"])
        
    rank(students)
    
    prt(students)



if __name__ == '__main__':
    main()