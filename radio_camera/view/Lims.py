class Lims:
    def __init__(self, ax):
        self.ax = ax

    def on_xlim_changed(self, event):
        self.ax["t_proj"].set_xlim(event.get_xlim())

    def on_ylim_changed(self, event):
        self.ax["f_proj"].set_ylim(event.get_ylim())
