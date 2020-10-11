### Author: Roholt
### 10-2020

import subprocess
from pathlib import Path

class Executioner:
  def __init__(self, scriptRef):
    self.execute(scriptRef)

  def execute(self, script):
    subprocess.call(script) #, shell=True)