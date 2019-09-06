import time
from bbio import *

buttonState = 0
lastButtonState = 0
# Create a setup function:
def setup():
  # Set the GPIO pins:
  #pinMode(USR3, OUTPUT)
  pinMode(GPIO1_6, INPUT)

# Create a main function:
def loop():
  global lastButtonState
  buttonState = digitalRead(GPIO1_6)
  if (buttonState != lastButtonState):
      if (buttonState == HIGH):
          print("Uploading...")
          #digitalWrite(USR3, state)
      else:
          print("Didn't Press Button...Exit upload mode")
  time.sleep(50)
  lastButtonState = buttonState

# Start the loop:
run(setup, loop)
