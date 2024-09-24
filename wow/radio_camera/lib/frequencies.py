import pandas as pd
import io


def frequencies(file, config):
    return pd.read_csv(io.StringIO("".join(file)), sep=config.data["separator"])
