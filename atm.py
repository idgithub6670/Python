# วิธีทอนเงิน โดยใช้ แบงค์ ให้น้อยที่สุด
# ยังไม่สามารถกำหนดจำนวนแบงค์ที่มีจำกัดได้

def atm() :
    balance = 28000
    cash = [1000,500,100]
    bankList = []
    
    while balance > 0 :
        withdraw = int(input("Please enter number: ")) 
        if withdraw <= balance :
            for i in cash :
                while i <= withdraw:
                    balance -= i
                    withdraw -= i
                    bankList.append(i)
            
        else:
            print("ATM Balance not enough!!!")
            break

        print(bankList)
        balance -= withdraw
        bankList.clear()


atm()