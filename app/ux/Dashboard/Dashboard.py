import globals
from single_include import Qt
from ux.Dashboard.DashboardView import DashboardView
from ux.Dashboard.DashboardInstr import DashboardInstr
from kernel.QtMger import get_icon, icon_name


class Dashboard:
    def __init__(self, ui, dialog, args=None):
        self.ui = ui
        self.dialog = dialog
        self.args = args
        self.bands = list(map(lambda x: f"{x["band"]}: {x["value"]}", self.args["lo"]))

        self.dashboard_instr = DashboardInstr(self)
        self.dashboard_view = DashboardView(self)
        self.dialog.setWindowState(Qt.WindowMaximized)
        self.ui.tabWidget.setTabIcon(0, get_icon(icon_name.WAVES, globals.theme))
        self.ui.tabWidget.setTabIcon(1, get_icon(icon_name.NOTE_STACK, globals.theme))
