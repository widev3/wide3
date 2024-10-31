import radio_camera.View
import mount_control.View


class Viewer:
    _instance = None

    def __new__(cls, config=None):
        if cls._instance is None:
            cls._instance = super(Viewer, cls).__new__(cls)
        return cls._instance

    def __init__(self, config=None):
        if not hasattr(self, "initialized"):
            package_config = list(
                filter(lambda x: x["package"] == "radio_camera", config)
            )
            self._radio_camera = radio_camera.View.View(
                package_config[0] if len(package_config) > 0 else None
            )

            package_config = list(
                filter(lambda x: x["package"] == "mount_control", config)
            )
            self._mount_control = mount_control.View.View(
                package_config[0] if len(package_config) > 0 else None
            )
            self.initialized = True

    def instance(self):
        return self._instance
