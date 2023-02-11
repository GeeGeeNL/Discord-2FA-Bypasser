try:
	import pyotp
	import os
except:
	import os
	os.system('pip install pyotp')
	import pyotp
os.system('cls')
totp = pyotp.TOTP('CODE HERE')
print ("\n  > Current code: " + totp.now())