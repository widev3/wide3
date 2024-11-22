class Lims:
    def __init__(self, im):
        self.im = im

    def on_xlim_changed(self, event):
        self.im["t_proj"].set_data([], [])

    def on_ylim_changed(self, event):
        self.im["f_proj"].set_data([], [])
