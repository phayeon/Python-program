# 비만도 계산기 - 완성

class Bmi(object):
    def __init__(self, name, cm, kg):
        self.name = name
        self.cm = cm
        self.kg = kg
        self.biman = ""

    def execute(self):
        self.biman = self.get_biman()
        self.get_biman()
        self.print_biman()

    def get_bmi(self):
        m = self.cm / 100
        kg = self.kg
        return kg / m ** 2 # ** 제곱

    def get_biman(self):
        cal = self.get_bmi()
        if cal >= 35:
            biman = "고도 비만"
        elif cal >= 30:
            biman = "중(重)도 비만 (2단계 비만)"
        elif cal >= 25:
            biman = "경도 비만 (1단계 비만)"
        elif cal >= 23:
            biman = "과체중"
        elif cal >= 18.5:
            biman = "정상"
        else:
            biman = "저체중"
        self.biman = biman

    def print_biman(self):
        name = self.name
        biman = self.biman
        cm = self.cm
        kg = self.kg
        title = " ### 비만도 계산기 ### "
        aster = "*"*40
        schema = "이름 키(cm) 몸무게(kg) 비만도"
        result = f'{name} {cm} {kg} {biman}'
        print(f'{title}\n{aster}\n{schema}\n{aster}\n{result}\n{aster}')

    @staticmethod
    def main():
        name = input("이름 : ")
        cm = int(input("키(cm) : "))
        kg = int(input("몸무게(kg) : "))
        bmi = Bmi(name, cm, kg)
        bmi.execute()

Bmi.main()