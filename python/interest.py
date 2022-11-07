monthly = 100
interest = 0.12
durYears = 40
savings = 0

interMonth = interest/12
durMonths = (durYears * 12)


for calendar in range(0,durMonths+1):
	savings = savings + (savings*interMonth)
	if (calendar < (durMonths)):
		savings = savings + monthly
print ("${:.2f}".format(savings))


savingsCalc = 101 * ((1-pow(1.01,480))/(1-1.01))
print ("${:.2f}".format(savingsCalc))