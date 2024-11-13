import radio_camera.View as rcv
import mount_control.View as mcv


class Viewer:
    _instance = None

    def __new__(cls, conf=None):
        if cls._instance is None:
            cls._instance = super(Viewer, cls).__new__(cls)
        return cls._instance

    def __init__(self, conf=None):
        if not hasattr(self, "initialized"):
            self.packages = {}
            self.initialized = True

            name = "radio_camera"
            pack = list(filter(lambda x: x["package"] == name, conf))
            self.packages[name] = rcv.View(pack[0] if len(pack) > 0 else None)

            name = "mount_control"
            pack = list(filter(lambda x: x["package"] == name, conf))
            self.packages[name] = mcv.View(pack[0] if len(pack) > 0 else None)

    def instance(self):
        return self._instance
