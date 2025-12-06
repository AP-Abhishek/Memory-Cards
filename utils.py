import os, sys

def get_resource_path(path):
    base_path = os.path.dirname(os.path.abspath(__file__))
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(base_path, path)
    return os.path.join(os.path.abspath("."), path)