import os

BASE_PATH = os.path.dirname(__file__)
CONFIG_PATH = os.path.join(BASE_PATH, "config")
CONFIG = {}

def config_env(module_name):
    config_path = os.path.join(CONFIG_PATH, module_name) + ".conf"
    with open(config_path, "r") as f:
        exec(f.read(), CONFIG)
