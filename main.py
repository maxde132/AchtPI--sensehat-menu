from sense_hat import SenseHat
import time
sense = SenseHat()
red = (255, 0, 0)
sense.clear()
import os
sense.show_message("AchtPI", 0.1)
screen = 1
already_done = False
circle_pattern = [ [False, False, True, True, True, True, False, False], [False, True, True, True, True, True, True, False], [True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True], [False, True, True, True, True, True, True, False], [False, False, True, True, True, True, False, False] ] # Define colors
background_color = (0, 0, 0)
circle_color = (255, 0, 0) 
pixels = []
for row in circle_pattern:
  for pixel in row:
    if pixel: pixels.append(circle_color)
    else: pixels.append(background_color)

def change_color(color, color2, color3):
  sense.clear()
  circle_color = (color, color2, color3)
  pixels = []
  for row in circle_pattern:
    for pixel in row:
      if pixel: pixels.append(circle_color)
      else: pixels.append(background_color) 
  sense.set_pixels(pixels)

def clickerflicker():
  for event in sense.stick.get_events():
    if event.action == "pressed":
      if event.direction == "down":
        if screen == 1:
          os.system("INSERT_YOUR_PYTHON_FILE_HERE")
        if screen == 2:
          os.system("INSERT_YOUR_PYTHON_FILE_HERE")
        if screen == 3:
          os.system("INSERT_YOUR_PYTHON_FILE_HERE")
        if screen == 4:
          os.system("INSERT_YOUR_PYTHON_FILE_HERE")
        if screen == 5:
          os.system("INSERT_YOUR_PYTHON_FILE_HERE")
        if screen == 6:
          os.system("INSERT_YOUR_PYTHON_FILE_HERE")
        if screen == 7:
          os.system("INSERT_YOUR_PYTHON_FILE_HERE")
        if screen == 8:
          os.system("INSERT_YOUR_PYTHON_FILE_HERE")
while True:
  clickerflicker()


  if screen == 1:
    if not already_done:
       change_color(255, 0, 0)
       already_done = True


  if screen == 2:
    if not already_done:
       change_color(255, 165, 0)
       already_done = True


  if screen == 3:
    if not already_done:
       change_color(255, 255, 0)
       already_done = True


  if screen == 4:
   if not already_done:
       change_color(0, 128, 0)
       already_done = True


  if screen == 5:
    if not already_done:
       change_color(0, 255, 255)
       already_done = True
  if screen == 6:
   if not already_done:
       change_color(0, 0, 255)
       already_done = True


  if screen == 7:
    if not already_done:
       change_color(75, 0, 130)
       already_done = True

  if screen == 8:
    if not already_done:
       change_color(238, 130, 238)
       already_done = True

  for event in sense.stick.get_events():
    print(str(screen))

    if event.direction == "left":
      if screen == 8:
        screen = 0
        time.sleep(0.2)
      else:
        screen = screen + 1
        time.sleep(0.2)
      already_done = False
    if event.direction == "right":
      if screen == 0:
        screen = 8
        time.sleep(0.2)
      else:
        screen = screen - 1
        time.sleep(0.2)
      already_done = False
