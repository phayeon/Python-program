class Grade(object):
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.gra = ""
    
    def solution(self):
        self.total_result()
        self.avg_result()
        self.grade_result()
        self.grade = self.print_grade()

    def total_result(self):
        return self.kor + self.eng + self.math

    def avg_result(self):
        return self.total_result()/3

    def grade_result(self):
        avg = self.avg_result()
        if avg >= 90:
            gra = "A"
        elif avg >= 80:
            gra = "B"
        else:
            gra = "F"
        return gra

    @staticmethod
    def print_menu():
        print('1. 점수 등록\n2. 성적 출력\n3. 성적 삭제\n4. 종료')
        return int(input("메뉴 선택 : "))

    @staticmethod
    def new_grade():
        return Grade(input("이름 : "), int(input("국어 : ")), int(input("영어 : ")), int(input("수학 : ")))
    
    def print_grade(self):
        return f'{self.name} {self.kor} {self.eng} {self.math} {self.total_result()} {self.avg_result()} {self.grade_result()}'

    @staticmethod
    def get_grade(ls):
        print(f"{'*'*40}\n이름 국어 영어 수학 총점 평균 학점\n{'*'*40}")
        for i in ls:
            print(f'{Grade.print_grade(i)}')
        print(f'{"*"*40}')

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Grade.print_menu()
            if menu == 1:
                print("### 점수 등록 ###")
                grade = Grade.new_grade()
                ls.append(grade)
            elif menu == 2:
                print("### 성적 출력 ###")
                Grade.get_grade(ls)
            elif menu == 3:
                print("### 성적 삭제 ###")
            elif menu == 4:
                print("성적 출력을 종료합니다.")
                break

Grade.main()