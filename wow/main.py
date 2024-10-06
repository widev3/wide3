import sys
import importlib
import argparse
import traceback
from BasicView import BasicView

sys.dont_write_bytecode = True


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


# import numpy as np
# import matplotlib.pyplot as plt
# import astropy.units as u
# from astropy.time import Time, TimeDelta
# from astropy.coordinates import AltAz, EarthLocation, SkyCoord
# import matplotlib.animation as animation

# # Number of stars (points)
# n_stars = 100

# # Set up initial observation time and location
# global initial_time
# initial_time = Time("2024-10-05T23:00:00")
# location = EarthLocation(lat=52.0 * u.deg, lon=0.0 * u.deg, height=100 * u.m)

# # Generate random AltAz coordinates for stars
# np.random.seed(0)
# initial_azimuths = np.random.uniform(0, 360, n_stars) * u.deg
# initial_altitudes = np.random.uniform(10, 80, n_stars) * u.deg

# # Create a list of SkyCoord objects in the AltAz frame for the initial time
# altaz_coords_list = [
#     SkyCoord(az=az, alt=alt, frame=AltAz(obstime=initial_time, location=location))
#     for az, alt in zip(initial_azimuths, initial_altitudes)
# ]

# # Set up the figure and axis for plotting
# fig, ax = plt.subplots(figsize=(6, 6))
# ax.set_xlim(0, 360)  # Azimuth range
# ax.set_ylim(0, 90)  # Altitude range
# ax.set_xlabel("Azimuth (deg)")
# ax.set_ylabel("Altitude (deg)")
# scat = ax.scatter(
#     [coord.az.deg for coord in altaz_coords_list],
#     [coord.alt.deg for coord in altaz_coords_list],
#     s=50,
#     c="black",
#     marker="*",
# )  # Stars (points)


# def update(frame):
#     delta = TimeDelta(100, format="sec")
#     global initial_time
#     initial_time += delta

#     new_altaz_frame = AltAz(obstime=initial_time, location=location)

#     updated_altaz_coords = [
#         coord.transform_to(new_altaz_frame) for coord in altaz_coords_list
#     ]

#     scat.set_offsets(
#         np.c_[
#             [coord.az.deg for coord in updated_altaz_coords],
#             [coord.alt.deg for coord in updated_altaz_coords],
#         ]
#     )

#     ax.set_title(f"Time: {initial_time.iso}")

#     return (scat,)


# # Create the animation, updating every 10 seconds
# ani = animation.FuncAnimation(fig, update, interval=100, blit=True)

# plt.show(block=True)
