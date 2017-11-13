import os

__version__ = "0.1.0"

CONFIG_ROOT = os.path.join(os.sep, "tmp", "pocketinternet")
if not os.path.exists(CONFIG_ROOT):
    print("[PocketInternet] Creating config_root at {}".format(CONFIG_ROOT))
    os.makedirs(CONFIG_ROOT)
