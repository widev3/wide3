import argparse
import os
import json
import Viewer


parser = argparse.ArgumentParser(description="Whistle of Wind command line")
parser.add_argument("conf", type=str, nargs="?", help="Path to the configuration file")

args = parser.parse_args()

config_file = "config.json"
if args.conf:
    if os.path.isfile(args.conf):
        config_file = args.conf
elif not os.path.isfile(config_file):
    config_file = ""

conf = []
if config_file:
    with open(config_file) as f:
        conf = json.load(f)

viewer = Viewer.Viewer(conf)
viewer.instance().packages["radio_camera"].view()
