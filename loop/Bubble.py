from random_list import RandomList
class Bubble(object):
    def __init__(self):
        pass
    def print(self):
        rl = RandomList()
        ls = rl.get_random(10, 100, 10)
        for i in range(len(ls)-1):
            for j in range(len(ls)-1):
                if ls[j] > ls[j+1]:
                    ls[j], ls[j+1] =  ls[j+1], ls[j]
        print(ls)
    @staticmethod
    def main():
        bubble = Bubble()
        bubble.print()
Bubble.main()