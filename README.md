# AchtPI

This is a menu system for the Raspberry Pi Sense HAT. Here's how to set it up:

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)


## Installation
1. Get a Raspberry Pi set-up (it's faster if you use Pi OS Lite rather than a desktop environment).
2. Download the script using `git clone` or by downloading the zip file.
3. Get 8 Python scripts/games that work with the Sense HAT and close themselves rather than repeating.
4. (Optional) Get 8 RGB format color codes (e.g., `255, 0, 255`).

### Step-by-Step Instructions
1. Edit the code via nano: `nano AchtPI--sensehat-menu/main.py`
2. Replace `Insert_Python_file_here` with your Python file's filepath.
3. (Optional) Add colors at the bottom where there are RGB values, replace them with your own.
4. Exit the nano editor by pressing `ctrl-x`, then `y`, and `ENTER` to save.
5. Test the script by typing `python3 AchtPI--sensehat-menu/main.py`.

## Usage
- The script should first appear with a big red circle.
- Use the joystick to navigate: press and pull down to start the other Python script.
- Use the left/right arrow keys to switch between scripts/colors.

## Features
- Customizable scripts and colors.
- Easy navigation using the joystick.

