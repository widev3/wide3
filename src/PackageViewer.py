import viewer.View as vv
import controller.View as cv


class PackageViewer:
    _instance = None

    def __new__(cls, conf=None):
        if cls._instance is None:
            if conf:
                cls._instance = super(PackageViewer, cls).__new__(cls)
            else:
                raise Exception("Cannot instance Viewer without a configuration file")
        elif conf:
            raise Exception("Dynamic configuration file is not implemented")

        return cls._instance

    def __init__(self, conf=None):
        if not hasattr(self, "initialized"):
            if not conf:
                raise Exception("Cannot instance Viewer without a configuration file")

            views_dict = {}
            views_dict["viewer"] = lambda x: vv.View(x)
            views_dict["controller"] = lambda x: cv.View(x)

            self.packages = {}
            self.initialized = True
            for el in views_dict:
                pack = list(
                    filter(
                        lambda x: (x["package"] if "package" in x else None) == el, conf
                    )
                )
                if len(pack) == 0:
                    raise Exception(f"No configurations for package {el}")
                if len(pack) > 1:
                    raise Exception(f"More than one configuration for {el}")
                self.packages[el] = views_dict[el](pack[0])

    def instance(self):
        return self._instance
