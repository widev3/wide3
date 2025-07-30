import os
import sys
import json
import gdown
import tempfile


class Version:
    def __init__(self, major=None, minor=None, patch=None):
        self.major = major
        self.minor = minor
        self.patch = patch

    def from_string(self, v: str):
        paths = v.split(".")
        paths += [None] * (3 - len(paths))
        major = int(paths[0])
        minor = int(paths[1])
        patch = int(paths[2])
        self = Version(major=major, minor=minor, patch=patch)

        return self

    def print(self):
        print(f"major {self.major}, minor {self.minor}, patch {self.patch}")

    def timeline(self, v):
        if v.major > self.major:
            return 1

        if v.minor > self.minor:
            return 1

        if v.patch > self.patch:
            return 1

        if v.major < self.major:
            return 1

        if v.minor < self.minor:
            return 1

        if v.patch < self.patch:
            return 1

        return 0

    def control(self, gdown_id, app_id):
        new_file, output = tempfile.mkstemp()
        url = f"https://drive.google.com/uc?id={gdown_id}"
        gdown.download(url=url, output=output, quiet=True)

        d = []
        with open(output) as f:
            d = json.load(f)

        os.remove(output)

        obj = next(
            (item for item in d if item.get("n") == app_id),
            None,
        )

        if obj:
            v = Version().from_string(obj["v"])
            if self.timeline(v) == 1:
                self.__updatable = obj
                return True

        return False

    def update(self):
        new_file, output = tempfile.mkstemp()
        url = f"https://drive.google.com/uc?id={self.__updatable["u"]}"
        gdown.download(url=url, output=output, quiet=True)
        # os.execl(sys.executable, *sys.orig_argv)
