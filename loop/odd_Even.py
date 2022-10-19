from random_list import RandomList
class Oddeven(object):
    def __init__(self):
        pass

    def print(self):
        r1 = RandomList()
        print(r1.get_random(10, 100, 10))
        for i in r1.get_random(10, 100, 10):
            if i % 2 == 0:
               print(f"짝수 : {i}")
            else:
                print(f"홀수 : {i}")

    @staticmethod
    def main():
        oe = Oddeven()
        oe.print()

Oddeven.main()