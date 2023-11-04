def turn(number):
    number_final = 0
    while number > 0:
        digit = number % 10
        number_final = number_final * 10 + digit
        number //= 10
    return number_final
number = 1234
resultado=turn(number)
print(resultado)
def is_palindromic(number):
    invested=turn(number)
    if invested == number:
        return True
    else:
        return False
resultado=is_palindromic(number)
print(resultado)    
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True
resultado=is_prime(number)
print(resultado)  
def next_prime(number):
    number += 1
    while True:
        if is_prime(number):
            return number
        number += 1
resultado=next_prime(number)
print(resultado)  
def digits(number):
    if number == 0:
        return 1  

    number = abs(number) 

    cont = 0

    while number > 0:
        number = number// 10  
        cont += 1

    return cont
resultado=digits(number)
print(resultado)  
def digits_n(number, position):
    if number < 0:
        number = abs(number)  
    # Lo elevo para hacer la potencia a el numero de la posicion porque seria el equivalente a la posicion
    divisor = 10 ** position  
    digit = (number // divisor) % 10  

    return digit
position=2
resultado=digits_n(number, position)
print(resultado)  
def digit_position(number, digit):
    if number < 0:
        number = abs(number)  

    position = 0  
    while number > 0:
        digito = number % 10  
        if digito == digit:
            return position  
        number //= 10  
        position += 1  

    return -1  
resultado=digit_position(number,position)
print(resultado)  
def remove_behind(number, nun):
    if nun <= 0:
        return number  

    divisor = 10 ** nun
    numb = number // divisor

    return numb
resultado=remove_behind(number,position)
print(resultado)  
def remove_ahead(number, nun):
    turn(number)
    if nun <= 0:
        return number  

    divisor = 10 ** nun
    numb = number // divisor
    turn(numb)
    return numb
resultado=remove_ahead(number,position)
print(resultado)  
def paste_behind(number, digit):
    number=number*10
    number=number+digit
    return number
resultado=remove_ahead(number,position)
print(resultado)  
def paste_ahead(number, digit):
    turn(number)
    number=number*10
    number=number+digit
    turn(number)
    return number
resultado=paste_ahead(number,position)
print(resultado)  
def piece_of_number(number, digit_i, digit_f):
    number1=remove_ahead(number,digit_i)
    number2=digits(number1)
    digitf=number2-(digit_f+digit_i)
    number3=remove_behind(number1,digitf)
    return number3 
position2=4
resultado=piece_of_number(number,position,position2)
print(resultado)  
def put_numbers_together(number1, number2):
    cont = digits(number2)
    number1=number1*(10*cont)
    number1=number1+number2 
    return number1
resultado=put_numbers_together(number,position)
print(resultado)  
        