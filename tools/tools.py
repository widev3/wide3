import argparse
import os
import json
import Viewer


parser = argparse.ArgumentParser(description="Whistle of Wind command line")
parser.add_argument(
    "config", type=str, nargs="?", help="Path to the configuration file."
)
parser.add_argument(
    "tool", type=str, nargs="?", help="Name of the tool to load at startup."
)

args = parser.parse_args()

config_file = "config.json"
if args.config:
    if os.path.isfile(args.config):
        config_file = args.config
elif not os.path.isfile(config_file):
    config_file = ""

config = []
if config_file:
    with open(config_file) as f:
        config = json.load(f)

viewer = Viewer.Viewer(config)
viewer.instance()._radio_camera.view()
