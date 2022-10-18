class Grade(object):
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = 0  
        self.avg = 0.0
        self.gra = ""
    
    def solution(self):
        self.total_result()
        self.avg_result()
        self.grade_result()
        self.grade = self.print_grade()

    def total_result(self):
        total = self.kor + self.eng + self.math
        self.total = total

    def avg_result(self):
        total = self.total
        avg = total/3
        self.avg = avg

    def grade_result(self):
        avg = self.avg
        if avg >= 90:
            gra = "A"
        elif avg >= 80:
            gra = "B"
        else:
            gra = "F"
        self.gra = gra  

    def print_grade(self):
        name = self.name
        kor = self.kor
        eng = self.eng
        math = self.math
        total = self.total
        avg = self.avg
        gra = self.gra
        title = "### 성적표 ### "
        aster = "*"*40
        schema = "이름 국어 영어 수학 총점 평균 학점"
        result = f'{name} {kor} {eng} {math} {total} {avg} {gra}'
        print(f"{title}\n{aster}\n{schema}\n{aster}\n{result}\n{aster}")

    @staticmethod
    def main():
        name = input("이름 : ")
        kor = int(input("국어 : "))
        eng = int(input("영어 : "))
        math = int(input("수학 : "))
        grade = Grade(name, kor, eng, math)
        grade.solution()

Grade.main()