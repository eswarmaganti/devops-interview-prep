'''
Validate the JSON Configuration

{
  "servers": [
    {"name": "web1", "ip": "10.0.0.1"},
    {"name": "web2", "ip": "10.0.0.2"},
    {"name": "web3"}
  ]
}

'''

import json
from pathlib import Path
import traceback

config_file = Path.cwd() / "config.json"

# read the json file
try: 
  with open(config_file) as f:
    config = json.load(f)
except FileNotFoundError as e:
  traceback.print_exc()

# filtered the invalid config
filtered = [item for item in config['servers'] if not ('name' in item and  'ip' in item) ]

# print the result
print("Invalid Configuration Found")
for item in filtered:
  print(item)
