def digits(number):
    if number == 0:
        return 1  

    number = abs(number) 

    cont = 0

    while number > 0:
        number = number// 10  
        cont += 1

    return cont

def palitos(number):
    digit = digits(number)
    text=""
    while digit > 0:
        last = number %10
        number //=10
        if last ==0:
            text = "-"+text
        elif last ==1:
            text = "-|"+text
        elif last ==2:
            text = "-||"+text
        elif last ==3:
            text = "-|||"+text
        elif last ==4:
            text = "-||||"+text
        elif last ==5:
            text = "-|||||"+text
        elif last ==6:
            text = "-||||||"+text
        elif last ==7:
            text = "-|||||||"+text
        elif last ==8:
            text = "-||||||||"+text
        elif last ==9:
            text = "-|||||||||"+text
        digit -=1
    text=text[1:]
    return text

number=1234
result=palitos(number)
print(result)
