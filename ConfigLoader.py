### Author: Roholt
### 10-2020

import yaml

class ConfigLoader:
  def __init__(self, path):
    self.loadedConfig = [{}]
    self.load(path)
    self.verify(self.loadedConfig)

  def load(self, path):
    with open(path) as file:
        self.loadedConfig = yaml.load(file, Loader=yaml.FullLoader)
    print("Loaded config: %s" % path)

  def verify(self, config):
    keys = ["shortcut", "suppress", "script"]
    for c in config:
      if len(c) != len(keys):
        print("More settings found than supported in the config. Required are: %s" % keys)
        exit(1)

      for key in c.keys():
        if key not in keys:
          print("Key: %s, missing in config.")
          exit(1)

  @property
  def config(self):
    return self.loadedConfig