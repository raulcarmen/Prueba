import machine, time, random 
led = machine.Pin(2, machine.Pin.OUT)

r = int(random.randrange(l000000))
cont = 0
print()
print("{0} es divisible por".format(r), end=": ")
for n in range(1, r+1):
  if r % n == 0:
    print(n, end=" - ")
    cont += 1
print("Fin")
if cont == 2:
  print("El numero ingresado si es primo, tiene {0} divisores".format(cont))
  led.off()
else:
  print("El numero ingresado no es primo, tiene {0} divisores".format(cont))
  led.on()	
		
