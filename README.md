AchtPI
This is a menu system for the raspberry pi sense hat. Here's how to set it up:

step 1:
  get a raspberry pi set-up (its faster if you use pi os lite rather than a desktop environment)
  download the script using git clone or downloading the zip
  get 8 python scripts/games that work with the sense hat and closes itself rather than repeating
  Optional: get 8 rgb format color codes ex. (255, 0, 255)
  
step 2:
  edit the code via nano. nano AchtPI--sensehat-menu/main.py
  replace Insert_Python_file_here with your python files's filepath
  Optional: add colors at the bottom where there are rgb values, replace them with your own
  
step 3:
  exit the nano editor by ctrl-x y ENTER to save
  test the script by typing python3 AchtPI--sensehat-menu/main.py
  It shoud first apper with a big red cicrcle. 
  If the joystick is pressed and then pulled down it will start the other python script. 
  left/right arrow keys to switch between scripts/colors
  
step 4:
  enjoy it!
Here's how to take it further:
  1. Make the script run on boot using crontab or something else
  2. add more/less scripts
  3. change or delete scrolling text at the top. (It can only be acht when there's eight scripts)
  4. change button colors
  5. change joystick inputs to your liking (instead of left/right to change button you can do up/down)
  6. have fun
