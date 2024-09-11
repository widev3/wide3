import matplotlib.pyplot as plt
from PyQt5.QtGui import QIcon


def basic_view(title):
    plt.ion()
    fig = plt.figure(constrained_layout=True)
    fig.canvas.manager.set_window_title(title=title)

    mng = plt.get_current_fig_manager()
    mng.window.showMaximized()
    mng.window.setWindowTitle(title)
    mng.window.setWindowIcon(
        QIcon("icon/settings_input_antenna_32dp_FFFFFF_FILL0_wght400_GRAD0_opsz40.png")
    )

    unwanted_buttons = []
    for x in mng.toolbar.actions():
        if x.text() in unwanted_buttons:
            mng.toolbar.removeAction(x)

    return fig
