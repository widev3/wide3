import radio_camera.View
import mount_control.View


class Viewer:
    _instance = None

    def __new__(cls, conf=None):
        if cls._instance is None:
            cls._instance = super(Viewer, cls).__new__(cls)
        return cls._instance

    def __init__(self, conf=None):
        if not hasattr(self, "initialized"):
            self.packages = {}
            pack_conf = list(filter(lambda x: x["package"] == "radio_camera", conf))
            self.packages["radio_camera"] = radio_camera.View.View(
                pack_conf[0] if len(pack_conf) > 0 else None
            )

            pack_conf = list(filter(lambda x: x["package"] == "mount_control", conf))
            self.packages["mount_control"] = mount_control.View.View(
                pack_conf[0] if len(pack_conf) > 0 else None
            )
            self.initialized = True

    def instance(self):
        return self._instance
