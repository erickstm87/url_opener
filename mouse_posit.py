import pyautogui

pyautogui.position()
print ('press ctrl-c to end program')
try:
	while True:
		print (pyautogui.position())
except KeyboardInterrupt:
	print('\ndone')
