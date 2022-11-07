import string

def temp(s,units):
	if (units.upper()=="F"):
		r = str(round((s-32.) * 5/9,2)) + " C"
	elif (units.upper()=="C"):
		r = str(round((s*(9/5)+32.),2)) + " F"
	else:
			r = "Error"
	return r

intAns = temp(12,"c")
print(intAns)