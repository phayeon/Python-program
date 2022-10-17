'''
키와 몸무게를 입력받아서 비만도를 측정하는 프로그램을 완성하시오.
BMI 지수를 구하는 공식은 다음과 같다.
BMI지수 = 몸무게(70kg) / (키(1.7m) * 키(1.7m))
BMI 지수에 따른 결과는 다음과 같다.
고도 비만 : 35 이상
중(重)도 비만 (2단계 비만) : 30 - 34.9
경도 비만 (1단계 비만) : 25 - 29.9
과체중 : 23 - 24.9
정상 : 18.5 - 22.9
저체중 : 18.5 미만
해당값을 입력받으면 다음과 같이 출력되도록 하시오.
***************************
이름 키(cm) 몸무게(kg) 비만도
***************************
홍길동 170 79 정상
***************************
'''

class bmi(object):
    def __init__(self, name, cm, kg):
        self.cm = cm
        self.kg = kg
        self.name = name

    def cal(self):
        name = self.name
        cm = self.cm
        kg = self.kg
        m = cm/100
        result = kg / m * m
        if result >= 35:
            biman = "고도 비만"
        elif result >= 30:
            biman = "중(重)도 비만 (2단계 비만)"
        elif result >= 25:
            biman = "경도 비만 (1단계 비만)"
        elif result >= 23:
            biman = "과체중"
        elif result >= 18.5:
            biman = "정상"
        else :
            biman = "저체중"
        print(f"***************************\n이름 키(cm) 몸무게(kg) 비만도\n{name} {cm} {kg} {biman} {result}\n***************************")

if __name__ == "__main__":
    name = input("이름 : ")
    cm = float(input("키(cm) : "))
    kg = float(input("몸무게(kg) : "))
    bmi = bmi(name, kg, cm)
    bmi.cal()