#영수증 기능 구현을 위한 빈 리스트 선언
receipts = []

#balance : 통장에 들어있는 기본 금액을 담는 변수

#3000원 입금
balance = 3000 

while True:
    #원하는 기능을 입력후 정수 형태로 변환.(입급:1, 출금:2, 영수증보기:3, 종료:0)
    mode = int(input("원하는 기능의 번호를 입력하세요.(입금:1, 출금:2, 영수증보기:3, 종료:0) : "))

    if mode == 0:
        print("서비스를 종료합니다.")
        break
    if mode == 1:
        deposit_amount = input("입금 금액 입력: ")
        # .isdigit() => 문자열 안에 숫자만 존재하는지 확인하는 메소드. 맞으면 True 반환
        if deposit_amount.isdigit() and int(deposit_amount) > 0:
            balance += int(deposit_amount)
            print(f'{deposit_amount}원 입금되었습니다. 현재 잔고는 {balance}원 입니다.')

            #영수증에 데이터 넣기 / 영수증 정보가 바뀌지 않도록 튜플형태로 저장
            receipts.append(("입금", deposit_amount, balance))

        else:
            print("숫자 형태가 아닙니다.")

    if mode == 2:
        withdraw_amount = input("출금 금액 입력: ")
        if withdraw_amount.isdigit() and int(withdraw_amount) > 0:
            if int(withdraw_amount) <= balance:
                balance -= int(withdraw_amount)
                print(f'{withdraw_amount}원 출금되었습니다. 현재 잔고는 {balance}원 입니다.')

                #영수증에 데이터 넣기 / 영수증 정보가 바뀌지 않도록 튜플형태로 저장
                receipts.append(("출금", withdraw_amount, balance))
            else:
                print("잔액이 부족합니다.")
        else:
            print("숫자 형태가 아닙니다.")
    if mode == 3:
        if receipts:
            print("=====영수증=====")
            for content in receipts:
                print(f'{content[0]} : {content[1]}원 | 잔액 : {content[2]}원')
        
        else:
            print("영수증이 비었습니다.")
