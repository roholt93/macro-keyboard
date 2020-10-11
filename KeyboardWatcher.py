### Author: Roholt
### 10-2020

import keyboard
from Executioner import Executioner

class KeyboardWatcher:
  def __init__(self):
    pass

  def run(self):
    keyboard.wait()

  def addShortcut(self, shortcut, script, suppress=False):
    keyboard.add_hotkey(shortcut, self.cb, args=(shortcut, script), suppress=suppress)

  def cb(self, shortcut, script):
    Executioner(script)


