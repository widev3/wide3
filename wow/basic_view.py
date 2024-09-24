import matplotlib.pyplot as plt


def basic_view(title, mosaic, width_ratios, height_ratios):
    plt.ion()
    fig, ax = plt.subplot_mosaic(
        constrained_layout=True,
        mosaic=mosaic,
        empty_sentinel=None,
        width_ratios=width_ratios,
        height_ratios=height_ratios,
    )
    fig.canvas.manager.set_window_title(title=title)

    mng = plt.get_current_fig_manager()
    mng.window.showMaximized()
    mng.window.setWindowTitle(title)

    unwanted_buttons = []
    for x in mng.toolbar.actions():
        if x.text() in unwanted_buttons:
            mng.toolbar.removeAction(x)

    return fig, ax
