'''
두자리 정수 랜덤숫자 10개를 뽑아서
사용자가 검색하는 숫자의 배수만
출력하는 프로그램을 개발하시오.
예) [12, 23,48, …,]
사용자의 input 값이 12인 경우
출력값이 12, 48만 되도록 한다.
'''
from random_list import RandomList
class Search(object):
    def __init__(self, num):
        self.num = num
    def print(self):
        num = self.num
        r1 = RandomList()
        ls = r1.get_random(10,100,10)
        print(ls)
        for i in ls:
            if i % num == 0: print(i)
            else: pass
    @staticmethod
    def main():
        num = int(input("숫자 : "))
        search = Search(num)
        search.print()
Search.main()