import importlib
import argparse
import traceback
from BasicView import BasicView


def start_a_module(module):
    class_name = "View"
    module = f"{module}.{class_name}"

    try:
        dynamic_module = importlib.import_module(module)
        try:
            dynamic_function = getattr(dynamic_module, class_name)
            if hasattr(dynamic_function, "view"):
                try:
                    dynamic_function().view()
                except Exception as e:
                    BasicView.basic_view_show_message(
                        "WOW",
                        f"Error during the execution of {module}:\n{traceback.format_exc()}",
                        3,
                    )
            else:
                BasicView.basic_view_show_message(
                    "WOW",
                    f"Cannot load method view() in class {class_name} from module {module}",
                    3,
                )
        except:
            BasicView.basic_view_show_message(
                "WOW", f"Cannot load class {class_name} from module {module}", 3
            )
    except:
        BasicView.basic_view_show_message("WOW", f"Cannot load module {module}", 3)


parser = argparse.ArgumentParser(description="wow command line")
parser.add_argument("tool", type=str, help="The name of the tool you want to use.")
args = parser.parse_args()
if args.tool:
    start_a_module(args.tool)
