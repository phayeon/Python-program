import random
class RandomList(object):
    def __init__(self):
        pass
    def get_random(self, start, end, count):
        return random.sample(range(start,end), k=count)
    def print(self):
        print(self.get_random(10, 100, 10))

'''
작동하지 않게 하려고 클래스 외부로 뺌
    @staticmethod
    def main():
        r1 = RandomList()
        r1.print()
RandomList.main()
'''

if __name__ == "__main__":
    r1 = RandomList()
    r1.print()