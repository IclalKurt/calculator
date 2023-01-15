print('please input numbers :')

number1 = float(input())
number2 = float(input())

print('please chose operation :')

#1-addition
addiction = number1 + number2

#2-subtraction
subtraction = number1 - number2

#3-multiplication
multiplication = number1 * number2

#4-division
division = number1 / number2

print('1-addition \n2-subtraction \n3-multiplication \n4-division')

chose = (input())

if chose == '1' :
    print(addiction)

elif chose == '2' :
    print(subtraction)

elif chose == '3' :
    print(multiplication)

elif chose == '4' :
    print(division)

else :
    print( 'incorrect chose')          