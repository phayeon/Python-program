'''
이름, 전화번호, 이메일, 주소를 받아서 연락처를
입력, 출력, 삭제하는 프로그램을 개발하시오.
단, 인명은  여러명 저장 가능합니다.
'''

class Contact(object):
    def __init__(self, name, number, mail, address):
        self.name = name
        self.number = number
        self.mail = mail
        self.address = address
        self.information = ""

    def print(self):
        print(f"### information ###")
        print(f"{self.name}, {self.number}, {self.mail}, {self.address}")

    @staticmethod   # 화면에 보이는 것들은 @staticmethod 에 처리
    def new_contacts():
        name = input("이름 : ")
        number = input("전화번호 : ")
        mail = input("메일 : ")
        address = input("주소 : ")
        return Contact(name, number, mail, address)    # 생성자

    def print_info(self):
        return f"{self.name}, {self.number}, {self.mail}, {self.address}"

    @staticmethod   # 화면에 보이는 것들은 @staticmethod 에 처리
    def get_contacts(ls):
        for i in ls:
            print(Contact.print_info(i))
    
    @staticmethod
    def print_menu():
        print("1. 연락처 등록\n2. 연락처 출력\n3. 연락처 삭제\n4. 종료")
        menu = input("메뉴 선택 : ")
        return int(menu)

    @staticmethod
    def delete_contact(ls, name):
        del ls[[i for i, j in enumerate(ls) if j.name == name]]
    @staticmethod
    def main(): # 1회 출력(반복 X)
        ls = []
        while True:
            menu = Contact.print_menu()
            # @staticmethod 안에 있어서 con(소문자)이 아니라 Con(대문자)
            if menu == 1:
                print("### 연락처 등록 ###")
                contact = Contact.new_contacts()
                ls.append(contact) # ls 리스트에 contact 값을 추가
            elif menu == 2:
                print("### 연락처 출력 ###")
                Contact.get_contacts(ls)
            elif menu == 3:
                print("### 연락처 삭제 ###")
                Contact.delete_contact(ls, input("삭제할 이름 : "))
            elif menu == 4:
                print("주소록 어플을 종료합니다.")
                break
Contact.main()