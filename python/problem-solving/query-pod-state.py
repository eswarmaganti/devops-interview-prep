'''
Using this JSON file, write a Python script that prints:
Total Pods: X
Running Pods: X
Pending Pods: X
Failed Pods: X
CrashLoopBackOff Pods: X
Top failing namespace: <namespace>
'''

from pathlib import Path
import traceback
import json
import jmespath
from collections import defaultdict

data_file = Path.cwd() / "pod.json"

try:
  with open(data_file) as f:
    data = json.load(f)
except FileExistsError as e:
  traceback.print_exc()

pod_states = jmespath.search("items[].status.phase", data)
clbf = jmespath.search("items[?status.phase == 'Running'].status.containerStatuses[].state.waiting", data)
failed_namespaces = jmespath.search("items[?status.phase == 'Failed'].metadata.namespace", data)

# pod state map
result_states = defaultdict(int)
for state in pod_states:
  result_states[state] += 1

# failed namespace map
result_namespaces = defaultdict(int)
for n in failed_namespaces:
  result_namespaces[n] += 1


print(result_states)
print(clbf)
print(failed_namespaces)