import json


class Config:
    def __init__(self, folder):
        self.data = {}
        configs = ["config.json", "config.jsonc"]
        for config in configs:
            lines = []
            try:
                with open(f"{folder}/{config}", "r") as file:
                    for line in file:
                        line = line.strip()
                        if line.startswith("//"):
                            continue
                        lines.append(line)
                if len(lines) > 0:
                    self.data = json.loads("".join(lines))
                    break
                else:
                    raise Exception()
            except:
                pass
