import math
"""
reverse integer


for example :

reverse_int(50) ==> -5
reverse_int(-50) ==> 5
reverse_int(41) ==> -14

"""

def reverse_int_without_string(number):
	"""
	reverse without change number into string
	"""
	number_copy = abs(number)
	digits_number = [] # split number by their digits
	while number_copy > 0 :
		digits_number.append(number_copy%10)
		number_copy = number_copy // 10
	# multiple number with her index with 10 = > 123 => 1*100 + 2* 10 + 3 * 1
	number_copy = [] 
	for i in digits_number :
		digits_number = digits_number[1:]
		for j in range(len(digits_number)):
			print(j)
			i *= 10
		number_copy.append(i)
	number_copy = sum(number_copy)
	return int(math.copysign(number_copy,number)*-1)
print(reverse_int_without_string(-10))


def reverse_int_with_string(number):
	"""
	reverse with change number into string
	"""
	return -(int("".join(list(str(n))[::-1]))) 