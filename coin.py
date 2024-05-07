# วิธีทอนเงิน โดยใช้ แบงค์ แหละ เหรียญให้น้อยที่สุด
# 

def coninchange() :
    totalprice = 10533
    changelist = [1000,500,100,50,20,10,5,2,1]
    change = []

    if totalprice == 0 :
        return 0 , print("0")
    
    for i in changelist :
        while totalprice >= i :
            totalprice -= i
            change.append(i)
            
    print(change)

def coninchangev2() :
    totalprice = 10533
    changelist = [1000,500,100,50,20,10,5,2,1]
    change = []
    tul = 0
    fivehun = 0
    hun = 0
    fif = 0
    twen = 0
    ten = 0
    five = 0
    two = 0
    one = 0

    if totalprice == 0 :
        return 0 , print("0")
    
    for i in changelist :
        while totalprice >= i :
            totalprice -= i
            change.append(i)
            

    for i in change :
        if i == 1000 :
            tul += 1
        elif i == 500 :
            fivehun += 1
        elif i == 100 :
            hun += 1
        elif i == 50 :
            fif += 1
        elif i == 20 :
            twen += 1
        elif i == 10 :
            ten += 1
        elif i == 5 :
            five += 1
        elif i == 2 :
            two += 1
        elif i == 1 :
            one += 1
    
    print("Type:1000 Amount%d\n Type:500:%d\n Type:100:%d\n Type:50:%d\n Type:20:%d\n Type:10:%d\n Type:5:%d\n Type:2:%d\n Type:1:%d"%(tul,fivehun,hun,fif,twen,ten,five,two,one))
coninchange()

coninchangev2()
