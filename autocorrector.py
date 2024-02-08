#!/usr/bin/python3
import keyboard
import pyautogui
from pynput.keyboard import Controller
from words import *

ignored_keys = ['ctrl', 'alt', 'shift', 'tab', 'centerentedowndowny/', 'up', 'down', 'left', 'right']
typed_string = ""

def replace_words(s):
    for word, replacement in word_replacements.items():
        s = s.replace(word, replacement)
    return s

def check_words(s):
  return s in word_replacements

def on_key_event(e):
    global typed_string

    if e.event_type == keyboard.KEY_DOWN:
        if e.name == 'space' and check_words(typed_string):
            text = replace_words(typed_string) + ' '
            pyautogui.hotkey('ctrl', 'backspace')
            Controller().type(text)
            print("overwrite", typed_string, "->", text)
            typed_string = ''
        elif e.name == 'backspace':
            typed_string = typed_string[:-1]  # Remove the last 
        elif e.name == 'space':
            typed_string = ''
        elif e.name not in ignored_keys:
            typed_string += e.name

keyboard.hook(on_key_event)
keyboard.wait()