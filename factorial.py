number = int(input('Enter your numbers : ')) # ใส่ตัวเลข

def factorial(n):
    if n == 1:                            # หากเท่ากับ 1 ก็จะทำการ return
        return 1
    else:
        return (n * factorial(n-1))       # ลดค่าตัวเลข และเรียกใช้งานซ้ำตัวเอง

print("Factorial of %d is: %d"%(number,factorial(number)))