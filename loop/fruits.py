'''
과일 판매상에서 메뉴를 진열하는 어플을 제작하고자 한다.
입력되는 값은 없다.
다만, 실행했을 때 출력되는 결과는 다음과 같다.

### 과일번호표 ###
*******************************
1번 과일 : 바나나
2번 과일 : 사과
3번 과일 : 망고
*******************************
구매할 과일 : 바
1번 과일 : 바나나
'''
class Fruits:
    def __init__(self):
        self.menu = ["바나나", "사과", "망고"]
    def solution(self):
        self.fruits = self.print_menu()
    def print_menu(self):
        title = "### 과일번호표 ###"
        aster = '*'*20
        print(f"{title}\n{aster}")
        j = 0
        for i in self.menu:
            print(f"{j+1}번 과일 : {i}")
            j += 1
        print(f"{aster}")
    
    def search_fruits(self,buy):
        self.buy = buy
        if buy[:1] == "바" or buy[:2] == "바나" or buy[:3] == "바나나" : print("바나나")
        elif buy[:1] == "사" or buy[:2] == "사과" : print("사과")
        elif buy[:1] == "망" or buy[:2] == "망고" : print("망고")
        else: print("잘못 입력하셨습니다.")

    @staticmethod
    def main():
        fruits = Fruits()
        fruits.solution()
        buy = input("구매할 과일 : ")
        fruits.search_fruits(buy)

Fruits.main()
    