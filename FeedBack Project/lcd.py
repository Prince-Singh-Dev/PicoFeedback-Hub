from machine import Pin
from gpio_lcd import GpioLcd
import time 
RS = 0
En = 1
D4 = 2
D5 = 3
D6 = 4
D7 = 5
Button1 = machine.Pin(6 , machine.Pin.IN , machine.Pin.PULL_UP)
Button2 = machine.Pin(7 , machine.Pin.IN , machine.Pin.PULL_UP)
Button3 = machine.Pin(8 , machine.Pin.IN , machine.Pin.PULL_UP)
BJP = 0
CONG = 0
AAP = 0
lcd = GpioLcd(rs_pin=Pin(RS),
              enable_pin=Pin(En),
              d4_pin=Pin(D4),
              d5_pin=Pin(D5),
              d6_pin=Pin(D6),
              d7_pin=Pin(D7),
              num_lines=2,
              num_columns=16)
lcd.move_to(0,0)
lcd.putstr("Good")
lcd.move_to(6 , 0)
lcd.putstr("Modr")
lcd.move_to(13,0)
lcd.putstr("Bad")
while True :
    if Button1.value() == 0:
        BJP += 1
        bjp = str(BJP)
        lcd.move_to(0,1)
        lcd.putstr(bjp)

    elif Button2.value() == 0:
        CONG += 1
        cong = str(CONG)
        lcd.move_to(7,1)
        lcd.putstr(cong)

    elif Button3.value() == 0:
        AAP += 1
        aap = str(AAP)
        lcd.move_to(14 ,1)
        lcd.putstr(aap)
    time.cleep(0.20)