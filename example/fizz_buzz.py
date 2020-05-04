"""
fizz buzz problem :

fizzBuzz(10) => 1,2,fizz,4,buzz,fizz,7,8,fizz,buzz
"""


def fizzBuzz(number):
    for i in range(number+1):
        if i % 3 == 0 and i % 5 == 0 :
            print("fizzbuzz")
        elif i % 5 == 0 :
            print("buzz")
        elif i % 3 == 0:
            print("fizz")
        else:
            print(i)