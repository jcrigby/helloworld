import sys
import json

def pretty_print_json():
    buffer = ""
    for line in sys.stdin:
        buffer += line
    data = json.loads(buffer)
    print(json.dumps(data, indent=4))

pretty_print_json()
