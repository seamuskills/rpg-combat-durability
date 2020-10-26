def ec(string):
	news = ""
	for i in range(len(string)):
		news += chr(ord(string[i])+1)
	return news
def dc(string):
	news = ""
	for i in range(len(string)):
		news += chr(ord(string[i])-1)
	return news