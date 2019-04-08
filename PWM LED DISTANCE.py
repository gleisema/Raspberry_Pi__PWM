import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

try:
    ## DISTANCE SENSOR SETUP ##
    PIN_TRIGGER = 21
    PIN_ECHO = 20

    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)
    
    ## LED SETUP ##
    GPIO.setup(18, GPIO.OUT)
    pwm = GPIO.PWM(18, 100)
    pwm.start(0)
    
    while True:
        ## SENSE DISTANCE ##
        GPIO.output(PIN_TRIGGER, GPIO.LOW)
        time.sleep(0.05)

        GPIO.output(PIN_TRIGGER, GPIO.HIGH)
        time.sleep(0.00001)

        GPIO.output(PIN_TRIGGER, GPIO.LOW)
            
        ## CALCULATE DISTANCE ##
        while GPIO.input(PIN_ECHO)==0:
            pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO)==1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)
        print(distance)
                
        if distance > 50:
            pwm.ChangeDutyCycle(0)
        else:
            dc = 50-distance
            pwm.ChangeDutyCycle(dc)

finally:
      GPIO.cleanup()
      pwm.stop()

