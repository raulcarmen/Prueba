import machine, time 
led = machine.Pin(2, machine.Pin.OUT)
n = 1
while n <= 100:
	c = 1
	x = 0
	while c <= n:
		if n%c == 0:
			x = x + 1
			led.off()
		c = c + 1
	if x==2:
		print (n)
	n = n + 1		
		
