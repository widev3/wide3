import json


class Config:
    def __default_config(self):
        self.data = {}

    def __init__(self):
        configs = ["config.json", "config.jsonc"]
        for config in configs:
            lines = []
            try:
                with open(config, "r") as file:
                    for line in file:
                        line = line.strip()
                        if line.startswith("//"):
                            continue
                        lines.append(line)
                if len(lines) > 0:
                    self.data = json.loads("".join(lines))
                    break
            except:
                pass

        if not self.data:
            self.__default_config()
            print(f"File {config} not found. Fallback to default config")
            print(self.data)
