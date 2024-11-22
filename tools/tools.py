import argparse
import os
import json
import traceback
import Viewer
from BasicView import BasicView


parser = argparse.ArgumentParser(description="Whistle of Wind command line")
parser.add_argument("conf", type=str, nargs="?", help="Path to the configuration file")

args = parser.parse_args()

config_file = "config.json"
if args.conf:
    if os.path.isfile(args.conf):
        config_file = args.conf
elif not os.path.isfile(config_file):
    BasicView.show_message(
        "Whistle of Wind",
        f"Please, provide a valid configuration file {config_file}",
        3,
    )

conf = []
with open(config_file) as f:
    conf = json.load(f)

try:
    viewer = Viewer.Viewer(conf)
    viewer.instance().packages["viewer"].view()
except:
    BasicView.show_message(
        "Whistle of Wind",
        f"Oops! Unhandled error during execution:\n{traceback.format_exc()}",
        3,
    )
