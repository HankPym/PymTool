def is_main():
	if __name__ == '__main__':
		return("Main")
	else:
		return(__name__)

print(is_main())