### Author: Roholt
### 08-2023

from ConfigLoader import ConfigLoader
from KeyboardWatcher import KeyboardWatcher
import os
import sys


def main():
    try:
        abs_path = os.path.dirname(os.path.abspath(__file__))
        settings = ConfigLoader(abs_path + "/config.yml").config

        keyboard_watcher = KeyboardWatcher()
        for setting in settings:
            keyboard_watcher.addShortcut(
                setting["shortcut"], setting["script"], setting["suppress"]
            )

        keyboard_watcher.run()
    except Exception as exception:
        print(f"Caught exception {exception}, exit!")
        sys.exit(1)


if __name__ == "__main__":
    main()
