"""
이름, 나이(950101-1), 거주지를 입력받아서
회원명부를 관리하는 어플을 제작하고자 한다.
출력되는 결과는 다음과 같다.

### 자기소개어플 ###
********************************
이름 : 홍길동
나이 : 25살 (만 나이)
주소 : 서울
********************************

"""
class Person(object):
    def __init__(self, name, ssn, local):
        self.name = name
        self.ssn = ssn
        self.local = local
        self.age = 0    # output 값도 프로퍼티

    def solution(self):
        self.set_gender()
        self.set_year()
        self.set_age()
        self.person = self.print_intro()

    def set_gender(self):
        ssn = self.ssn
        gender = ssn[7] # 성별번호 / [7:8] 인데 1개 값만 구하는 거라 생략
        self.gender = gender

    def set_year(self):
        gender = self.gender
        if gender == "1" or gender == "2": year = 1900
        else : year = 2000
        self.year = year

    def set_age(self):
        ssn = self.ssn
        year = self.year
        age = 2022 - (year + int(ssn[:2]))
        self.age = age

    def print_intro(self):
        name = self.name
        age = self.age
        local = self.local
        title = "### 자기소개어플 ###"
        aster = "*"*40
        print(f'{title}\n{aster}\n이름 : {name}\n나이 : {age}\n주소 : {local}\n{aster}')

    @staticmethod
    def main():
        name = input("이름 : ")
        ssn = input("주민번호 : ")
        local = input("주소 : ")
        person = Person(name, ssn, local)
        person.solution()

Person.main()