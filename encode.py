def ec(string):
	news = ""
	for i in range(len(string)):
		news += chr(ord(string[i])+len(string))
	return news
def dc(string):
	news = ""
	for i in range(len(string)):
		news += chr(ord(string[i])-len(string))
	return news