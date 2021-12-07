from star import Star
from time import sleep

star = Star(pwm=True)

# Twinkle Pattern
leds = star.leds

twinkle_loop=300
while twinkle_loop<0:
    for led in leds:
        led.pulse()
        sleep(.2)
        twinkle_loop-=1

# Slow Walk
while True:
    if(count%26!=0):
        leds[count%26].on()
        sleep(step)
        leds[count%26].off()
            
    count += 1
    step = step*0.99
        
    if(step <= 0.0001):
        star.inner.blink(on_time=0.5,off_time=0.5,n=5)
        sleep(5)
        count = 0
        step = 2

 #In Out
in_out_loop=120
star.inner.on()
while in_out_loop<0:
    star.toggle()
    sleep(.5)
    in_out_loop-=1