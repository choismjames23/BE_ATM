#balance : 통장에 들어있는 기본 금액을 담는 변수

#3000원 입금
balance = 3000 

while True:
    #원하는 기능을 입력후 정수 형태로 변환.(입급:1, 출금:2, 영수증보기:3, 종료:0)
    mode = int(input("원하는 기능의 번호를 입력하세요.(입급:1, 출금:2, 영수증보기:3, 종료:0) : "))

    if mode == 0:
        break
    if mode == 1:
        pass
    if mode == 2:
        pass
    if mode == 3:
        pass

print(mode)
