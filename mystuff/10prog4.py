#Random string generator
import random
import string
def randomString(d):
	str=string.ascii_uppercase+string.ascii_lowercase
	return "".join(random.choice(str) for _ in range(d))







print randomString(10)