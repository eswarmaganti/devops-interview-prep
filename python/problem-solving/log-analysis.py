'''
Analyse the logs and output the count of each error type

Logs format:
INFO Service started
ERROR Database connection failed
INFO Retrying connection
ERROR Timeout occurred
WARNING Disk space low
ERROR Database connection failed

Output: 
Total ERROR count: 3

Top errors:
Database connection failed -> 2
Timeout occurred -> 1
'''

import re
import traceback
from pathlib import Path

# read the file line by line and analyse
filepath = Path.cwd() / "app.log"

print(f"Reading the file: {filepath}")

result = {}
try:
  with open(filepath) as f:
    for line in f:
      # search for ERROR log matches
      matches = re.search('^ERROR (.*?) ', line)

      # if match found, process it
      if matches:
        error_type = matches.group(1)

        # updating the counters
        if error_type in result:
          result[error_type] += 1
        else:
          result[error_type] = 1

except FileNotFoundError as e:
  traceback.print_exc()

# sorting the results for top 3 errors
result = {key: value for key, value in sorted(result.items(), key = lambda item: item[1]  ,reverse=True)}

print(f"Total ERROR count: {sum(result.values())} ")

for error in list(result)[:3]:
  print(f"{error} Errors: {result[error]}")
