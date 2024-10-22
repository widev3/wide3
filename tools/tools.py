import argparse
import os
import json


def start_a_module(module):
    from radio_camera import View as radio_camera_view

    radio_camera_view.View().view()


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

start_a_module(config)
