### Author: Roholt
### 10-2020

import yaml


class ConfigLoader:
    def __init__(self, path):
        self.loaded_config = [{}]
        self.load(path)
        self.verify(self.loaded_config)

    def load(self, path):
        with open(path, encoding="utf8") as file:
            self.loaded_config = yaml.load(file, Loader=yaml.FullLoader)
        print(f"Loaded config: {path}")

    def verify(self, config):
        keys = ["shortcut", "suppress", "script"]
        for c in config:
            if len(c) != len(keys):
                raise RuntimeError(
                    f"More settings found than supported in the config. Required are: {keys}"
                )

            for key in c.keys():
                if key not in keys:
                    raise RuntimeError(f"Key: {key}, missing in config.")

    @property
    def config(self):
        return self.loaded_config
