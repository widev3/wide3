import pandas as pd
import io


def properties(file, config):
    return pd.read_csv(io.StringIO("".join(file)), sep=config.data["separator"])
