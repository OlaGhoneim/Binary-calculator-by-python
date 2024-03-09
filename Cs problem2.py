#Zyad Mohamed Ahmed 20230159
#Abdelrahman Essam Abdelrahman 20230210
#Ola Ghoneim Hammad 20231232


# Function for one's complement operation
def ones_complement(binary):
    ones = ''
    for digit in binary: #Switch every one to zero and every zero to one
        if digit == '1':
            ones += '0'
        else:
            ones += '1'
    return ones

# Function for two's complement operation
def twos_complement(binary):
    ones = ones_complement(binary) #First get one's complement of the number
    twos = ''
    carry = 1
    for bit in ones[::-1]: #Adding one to the one's complement
        if bit == '1' and carry == 1:
            twos = '0' + twos
        elif bit == '0' and carry == 1:
            twos = '1' + twos
            carry = 0
        else:
            twos = bit + twos
    if carry == 1:
        twos = '1' + twos
    return twos

# Function for equalizing the two input binary numbers
def equalize(num1, num2):
    if len(num1) > len(num2): #ensure that two numbers num1 and num2 have the same length
        difference = len(num1) - len(num2)
        for i in range(difference):
            num2 = '0' + num2          #adding leading zeros to the shorter number.
    elif len(num1) < len(num2):
        difference = len(num2) - len(num1)
        for i in range(difference):
            num1 = '0' + num1
    return num1, num2

# Function for binary addition
def binary_addition(num1, num2):
    num1, num2 = equalize(num1, num2) #call equalize() function
    carry = 0    #intialize value for the carry in addition
    result = ''
    for i in range(len(num1) - 1, -1, -1): #loop in the number in a reversed way
        bit_sum = int(num1[i]) + int(num2[i]) + carry
        result = str(bit_sum % 2) + result
        carry = bit_sum // 2 #calculate the value of the carry in the next loop
    if carry:         #in case carry not equal 0
        result = '1' + result

    return result

# Function for binary subtraction
def binary_subtraction(num1, num2):
    num1, num2 = equalize(num1, num2)
    result = ''
    borrow = 0 # intialize borrow of the subtraction
    for i in range(len(num1) - 1, -1, -1):
        digit1 = int(num1[i])
        digit2 = int(num2[i])
        subtract = digit1 - digit2 - borrow
        if subtract < 0:
            subtract += 2  # adding 2 to perform the two's complement operation in binary subtraction
            borrow = 1
        else:
            borrow = 0

        result = str(subtract) + result

    return result

#Program
while True:
    print("**binary calculator**")
    program=input("A)Insert new numbers\nB)Exit\n")
    if program.upper()=='A':
        user_num=input("Enter a binary number:\n")
        valid=1
        for i in user_num: #Check if binary number is valid
            if i!='0' and i!='1':
                print("please insert a valid binary number")
                valid=0
                break
        if valid==0:
            continue
        print("** please select the operation **")
        operation=input("A)Compute one's complement\nB)Compute two's complement\nC)Addition\nD)Subtraction\n")
        if operation.upper()=='A':
            print(ones_complement(user_num))
        elif operation.upper()=='B':
            print(twos_complement(user_num))
        elif operation.upper()=='C':
            user_num2 = input("please insert the second number\n")
            for i in user_num2: #Check if binary number is valid
             if i!='0' and i!='1':
                print("please insert a valid binary number")
                valid=0
                break
            if valid==0:
                continue
            print(binary_addition(user_num,user_num2))
        elif operation.upper() == 'D':
            user_num2 = input("please insert the second number\n")
            for i in user_num2:  # Check if binary number is valid
                if i != '0' and i != '1':
                    print("please insert a valid binary number")
                    valid = 0
                    break
            if valid == 0:
                continue
            print (binary_subtraction(user_num,user_num2))

        else:
            print("please select a valid choice")
            continue
    elif program.upper() == 'B':
        break
    else:
        print("please select a valid choice")
        continue

