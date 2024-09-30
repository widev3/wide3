import json


class Config:
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
            self.data = {}
