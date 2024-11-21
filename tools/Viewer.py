import radio_camera.View as rcv
import mount_control.View as mcv


class Viewer:
    _instance = None

    def __new__(cls, conf=None):
        if cls._instance is None:
            if conf:
                cls._instance = super(Viewer, cls).__new__(cls)
            else:
                raise Exception("Cannot instance Viewer without a configuration file")
        elif conf:
            raise Exception("Dynamic configuration file is not implemented")

        return cls._instance

    def __init__(self, conf=None):
        if not hasattr(self, "initialized"):
            if not conf:
                raise Exception("Cannot instance Viewer without a configuration file")
            
            self.packages = {}
            self.initialized = True

            name = "radio_camera"
            pack = list(filter(lambda x: x["package"] == name, conf))
            if len(pack) == 0:
                raise Exception(f"No configurations for package {name}")
            if len(pack) > 1:
                raise Exception(f"More than one configuration for {name}")
            self.packages[name] = rcv.View(pack[0])

            name = "mount_control"
            pack = list(filter(lambda x: x["package"] == name, conf))
            if len(pack) == 0:
                raise Exception(f"No configurations for package {name}")
            if len(pack) > 1:
                raise Exception(f"More than one configuration for {name}")
            self.packages[name] = mcv.View(pack[0])

    def instance(self):
        return self._instance
