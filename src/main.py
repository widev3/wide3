import argparse
import os
import json
import traceback
import PackageViewer
import basic_view


parser = argparse.ArgumentParser(description="Whistle of Wind command line")
parser.add_argument("conf", type=str, nargs="?", help="Path to the configuration file")

args = parser.parse_args()

config_file = "config.json"
if args.conf:
    if os.path.isfile(args.conf):
        config_file = args.conf
    else:
        basic_view.show_message(
            "Whistle of Wind",
            f"Please, provide a valid configuration file {config_file}",
            3,
        )
elif not os.path.isfile(config_file):
    basic_view.show_message(
        "Whistle of Wind",
        f"Please, provide a valid configuration file {config_file}",
        3,
    )

if config_file:
    conf = []
    with open(config_file) as f:
        conf = json.load(f)

    try:
        viewer = PackageViewer.PackageViewer(conf)
        viewer.instance().packages["viewer"].view()
    except:
        basic_view.show_message(
            "Whistle of Wind",
            f"Oops! Unhandled error during execution:\n{traceback.format_exc()}",
            3,
        )
