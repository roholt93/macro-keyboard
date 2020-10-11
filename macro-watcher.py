### Author: Roholt
### 10-2020

from ConfigLoader import ConfigLoader
from KeyboardWatcher import KeyboardWatcher

def main():
  settings = ConfigLoader("./config.yml").config

  keyboardWatcher = KeyboardWatcher()
  for setting in settings:
    keyboardWatcher.addShortcut(setting["shortcut"], setting["script"], setting["suppress"])

  keyboardWatcher.run()

if __name__ == "__main__":
  main()

