from random_list import RandomList
class Oddeven(object):
    def __init__(self):
        pass

    def print(self):
        r1 = RandomList()
        rannum = r1.get_random(10, 100, 10)
        for i in rannum:
            if i % 2 == 0:
               print(f"짝수 : {i}")
            else:
                print(f"홀수 : {i}")
        print([f"짝수 : {i}" if i % 2 == 0 else f"홀수 : {i}" for i in rannum])

    @staticmethod
    def main():
        oe = Oddeven()
        oe.print()

Oddeven.main()