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
	digits_number = [] # split number by their digits
	while number > 0 :
		digits_number.append(number%10)
		number = number // 10
	print(digits_number)
	# multiple number with her index with 10 = > 123 => 1*100 + 2* 10 + 3 * 1
	number = [] 
	for i in digits_number :
		digits_number = digits_number[1:]
		for j in range(len(digits_number)):
			print(j)
			i *= 10
		number.append(i)
	return -(sum(number))



def reverse_int_with_string(number):
	"""
	reverse with change number into string
	"""
	return -(int("".join(list(str(n))[::-1]))) 