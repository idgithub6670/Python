def decimal_to_hexadecimal(deciaml):
    hexadecimal_table = "0123456789ABCDEF"
    hexadecimal_string = ""

    while deciaml > 0:
        remainder = deciaml % 16
        hexadecimal_string = hexadecimal_table[remainder] + hexadecimal_string
        deciaml = deciaml // 16

    return hexadecimal_string

deciaml = int(input("Please enter decimal number:"))
hexadecimal = decimal_to_hexadecimal(deciaml)

print("Deciaml: ",deciaml)
print("Hexadecimal:" ,hexadecimal)
