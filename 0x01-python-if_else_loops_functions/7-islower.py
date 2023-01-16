#!/usr/bin/python3
def islower(c):
	lowercase = ord(c)
	if lowercase > 96 and lowercase < 123:
		return True
	else:
		return False
