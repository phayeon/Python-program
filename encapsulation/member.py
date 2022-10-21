'''
아아디, 비밀번호, 이름을 받아서
회원가입, 목록, 탈퇴하는 프로그램을 개발하시오.
'''

class Member(object):
    def __init__(self, id, pw, name):
        self.id = id
        self.pw = pw
        self.name = name
    @staticmethod
    def add_member():
        return Member(input("아이디 : "), input("비밀번호 : "), input("이름 : "))
    @staticmethod
    def print_menu():
        print(f'메뉴 선택\n1.회원가입\n2.목록\n3.탈퇴')
        return int(input("작업 선택 : "))

    def print_info(self):
        return f'{self.id} {self.pw} {self.name}'

    @staticmethod
    def get_info(ls):
        print("아이디 비밀번호 이름")
        [print(i.print_info()) for i in ls]
    @staticmethod
    def main():
        ls = []
        while True:
            menu = Member.print_menu()
            if menu == 1:
                print("회원가입")
                info = Member.add_member()
                ls.append(info)
            elif menu == 2:
                print("목록")
                Member.get_info(ls)
            elif menu == 3:
                print("탈퇴")
            else:
                print("입력 오류.")
                break
Member.main()