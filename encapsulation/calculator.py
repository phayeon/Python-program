class Calculator(object): # class 상수, (object) = 상속 → Calculator가 객체가 됨
    def __init__(self, num1, op, num2): # 생성자
        self.num1 = num1    # 속성
        self.op = op
        self.num2 = num2    # 속성
        
    def cal(self): # def Method, self 객체 자신을 의미
        num1 = self.num1
        op = self.op
        num2 = self.num2
        if self.op == "+":
            result = num1 + num2
        elif self.op == "-":
            result = num1 - num2
        elif self.op == "*":
            result = num1 * num2
        elif self.op == "/":
            result = num1 / num2
        elif self.op == "%":
            result = num1 % num2
        else :
            result = "잘못된 연산자 입니다."
        print(f"{self.num1} {self.op} {self.num2} = {result}")

if __name__ == "__main__":
    num1 = int(input("숫자 : "))
    op = input("연산자 : ")
    num2 = int(input("숫자 : "))
    Calculator = Calculator(num1, op, num2) # Calculator의 인스턴스화(메모리로 이동)
    Calculator.cal() # Calculator = 인스턴스 객체