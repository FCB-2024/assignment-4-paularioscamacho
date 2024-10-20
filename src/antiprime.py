## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
def main(x) :
	i = 1
	comptador1 = 0
	comptador2 = 0
	y = x - 1

	while (i <= x):
		if (x % i == 0):
			comptador1 = comptador1 + 1
		i = i + 1

	while (y >= 1):
		i = 1
		while (i <= y):
			if (y % i == 0):
				comptador2 = comptador2 + 1
			i = i + 1
		if (comptador2 >= comptador1):
			return ("not anti-prime")
			y = 0
		else:
			y = y - 1
			comptador2 = 0
	if (comptador2 < comptador1):
		return ("anti-prime")


## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :
	import sys
	x = int (sys.argv [1])

	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	print(main(x))
