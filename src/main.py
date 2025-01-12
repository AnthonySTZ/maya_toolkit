import os
import sys

plugin_path = os.path.join(os.environ["MAYA_TOOLKIT"], "src")

sys.path.insert(0, plugin_path)

from importlib import reload
import interface

reload(interface)

interface.create_window()
