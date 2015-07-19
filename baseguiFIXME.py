	# convert any base number to another base

	
while True:

	yes = 0
	while yes < 2:
		x = input("original integer?\n>")
		
		
		if x.isdigit():
			yes += 1
			print_x = x
			
		base_x = input("original base?\n>")
		
		
		if base_x.isdigit():
			yes += 1
			print_orig_base = base_x
			base_x = eval(base_x)	
		
			x = list(x)
		
			xlist = []

			for item in x:
				xlist.append(eval(item))
		
			for item in xlist:
				if item >= base_x:
					yes = 0
		
		
		
	x_dec = 0


	for y in range(len(x)):
		x_dec += ((xlist[-(y + 1)])*(base_x ** y))
		
	printlast = x_dec

	while yes == 2:
		to_base = input("destination base?\n?")
		
		if to_base.isdigit():
			yes += 1
			
		if to_base == '1':
			print ("no such thing as base 1!")
			yes = 2
			
	to_base = int(to_base)

	digits = 0
	while to_base**digits <= x_dec:
		digits += 1

	result = []


	for z in range(digits-1, -1, -1):
		this_digit = to_base**z
		bip = (x_dec/this_digit)
		x_dec -= this_digit*bip
		result.append(str(bip))

		
	print ("\n\n\n     %s (base %s)" % (print_x, print_orig_base))
	
	print_result = []
	
	for num in result:
		if len(num) > 1:
			print_result.append("(" + num + ")")
		else:
			print_result.append(num)
	
			
	print ("     in base %s is\n     >>>> %s" % (to_base, ''.join(print_result)))
		
	input('')
		
		
		