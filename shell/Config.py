import sys
import json

path = sys.argv[0]
root = path[0:path.rfind("/", 0, path.rfind("/"))]

with open(root + "/config.json") as raw_data:
    config = json.load(raw_data)
