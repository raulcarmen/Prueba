import machine, time 
led = machine.Pin(2, machine.Pin.OUT)
n = 1
while n <= 1000000:
	led.on()
	time.sleep(0.5)
	c = 1
	x = 0
	while c <= n:
		if n%c == 0:
			x = x + 1

		c = c + 1
	if x==2:
		print (n)
		print("Es un numero primo")
		led.off()
		time.sleep(0.5)
	n = n + 1	
		
