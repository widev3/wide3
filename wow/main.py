import importlib
import argparse


def start_a_module(module):
    dynamic_module = importlib.import_module(f"{module}.view")
    dynamic_function = getattr(dynamic_module, "view")
    dynamic_function()


parser = argparse.ArgumentParser(description="wow command line")
parser.add_argument("tool", type=str, help="The name of the tool you want to use.")
args = parser.parse_args()
if args.tool:
    start_a_module(args.tool)
