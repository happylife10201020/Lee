##
# 성적관리 프로그램
# 5명의 학생의 세개의 교과목 (영어, C-언어, 파이썬)에 대하여
# 키보드로부터 학번, 이름, 영어점수, C-언어 점수, 파이썬 점수를 입력받아 총점, 평균, 학점, 등수를 계산하는 프로그램 작성
# 입력 함수, 총점/평균 계산 함수,  학점계산 함수, 등수계산 함수, 출력 함수
# 삽입 함수, 삭제 함수, 탐색함수(학번, 이름), 정렬(총점)함수, 80점이상 학생 수 카운트 함수
# 지도교수 : 황경순
# 강의실 : S4-1 103호
# 2022041060 이인수
##

class Student:
    def __init__(self, student_id, name, english, c_language, python):
        self.student_id = student_id
        self.name = name
        self.scores = {"English": english, "C-Language": c_language, "Python": python}
        self.total = sum(self.scores.values())
        self.average = self.total / len(self.scores)
        self.grade = self.calculate_grade()
        self.rank = None

    def calculate_grade(self):
        if self.average >= 95:
            return 'A+'
        elif self.average >= 90:
            return 'A'
        elif self.average >= 85:
            return 'B+'
        elif self.average >= 80:
            return 'B'
        elif self.average >= 75:
            return 'C+'
        elif self.average >= 70:
            return 'C'
        elif self.average >= 65:
            return 'D+'
        elif self.average >= 60:
            return 'D'
        else:
            return 'F'


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        try:
            student_id = int(input("Enter Student Number: "))
            name = input("Enter Student Name: ")
            english = int(input("Enter English Score: "))
            c_language = int(input("Enter C-Language Score: "))
            python = int(input("Enter Python Score: "))
            student = Student(student_id, name, english, c_language, python)
            self.students.append(student)
            self.calculate_ranks()
        except ValueError:
            print("Invalid Input")

    def remove_student(self):
        try:
            student_id = int(input("Enter Student Number to remove: "))
            self.students = [s for s in self.students if s.student_id != student_id]
            self.calculate_ranks()
            print("Student Deleted!\n")
        except ValueError:
            print("Invalid Input")

    def search_student(self):
        search_key = input("Enter Student's name or number: ")
        try:
            student_id = int(search_key)
            student = next((s for s in self.students if s.student_id == student_id), None)
        except ValueError:
            student = next((s for s in self.students if s.name == search_key), None)

        if student:
            print(f"Found: {student.name}, Total Score: {student.total}, Grade: {student.grade}")
        else:
            print("ERROR: No such student exists!\n")

    def sort_students(self):
        self.students.sort(key=lambda s: s.total, reverse=True)  # 🔹 정렬만 수행
        self.calculate_ranks()  # 등수 계산을 여기서만 한 번 호출

    def count_above_80(self):
        count = sum(1 for s in self.students if s.average >= 80)
        print(f"Number of students with average score >= 80: {count}")

    def calculate_ranks(self):
        for idx, student in enumerate(self.students):
            student.rank = idx + 1  # 🚀 등수 계산만 수행

    def display_students(self):
        if not self.students:
            print("No students exist!\n")
            return

        print("\n" + "=" * 80)
        print(
            f"| {'Name':<10} | {'Num':<5} | {'Eng':<7} | {'C-Lang':<7} | {'Python':<7} | {'Sum':<5} | {'Avg':<5} | {'Grade':<5} | {'Rank':<5} |")
        print("=" * 80)
        for student in self.students:
            print(
                f"| {student.name:<10} | {student.student_id:<5} | {student.scores['English']:<7} | {student.scores['C-Language']:<7} | {student.scores['Python']:<7} | {student.total:<5} | {student.average:<5.2f} | {student.grade:<5} | {student.rank:<5} |")
        print("=" * 80)


def CHOICE():
    print("\n1. Add new Student")
    print("2. Remove Student")
    print("3. Print Student Details")
    print("4. Count students over 80 score")
    print("5. Search for Student")
    print("6. Sort by Total Score")
    print("0. Exit")

    while True:
        try:
            return int(input("Enter your choice: "))
        except ValueError:
            print("Enter a valid choice.")


def main():
    manager = StudentManager()

    while True:
        choice = CHOICE()
        if choice == 1:
            manager.add_student()
        elif choice == 2:
            manager.remove_student()
        elif choice == 3:
            manager.display_students()
        elif choice == 4:
            manager.count_above_80()
        elif choice == 5:
            manager.search_student()
        elif choice == 6:
            manager.sort_students()
        elif choice == 0:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
