import random
class Bubble(object):
    def __init__(self):
        pass
    def print(self):
        self.bubble = self.res_print()
    def extract_random(self):
        return random.sample(range(1,101),10)
    def res_print(self):
        print('### 랜덤 숫자 ###')
        print('*'*40)
        for i in self.extract_random():
            if i % 2 ==0: print(i)
            else: pass
        print('*'*40)
    @staticmethod
    def main():
        bubble = Bubble()
        bubble.print()
Bubble.main()