from single_include import Qt
import ux.Dashboard.dashboard_view as dashboard_view
import ux.Dashboard.dashboard_instr as dashboard_instr
from kernel.QtMger import get_icon, icon_types


class Dashboard:
    def __init__(self, ui, dialog, args=None):
        self.ui = ui
        self.dialog = dialog
        self.args = args
        self.instr = None
        self.filename = None
        self.spec = None

        dashboard_instr.init(self)
        dashboard_view.init(self)
        self.dialog.setWindowState(Qt.WindowMaximized)
        self.ui.tabWidget.setTabIcon(0, get_icon(icon_types.WAVES))
        self.ui.tabWidget.setTabIcon(1, get_icon(icon_types.NOTE_STACK))
