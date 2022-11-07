total = input('Enter the number of total items: ')
sample = input('Enter the number of items sampled: ')

result = sample / (total / 100.0)

print "The sample is", "{:2f}".format(result), "% of the total."
