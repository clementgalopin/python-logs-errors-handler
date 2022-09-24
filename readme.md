## Error and logs handler

This lib is a basic errors  and logs handler.
It basically catches everything that is printed by the program and adds a runtime id + timestamp to it.

If the execution ends or any print starting by `Error` is detected, it will gracefully shut down and write logs to a file in a `logs` subfolder.

All you need to do is to add those few lines at the beginning of your script
```python
import time
import atexit
import sys

from logs import Logs

# Rewrite stdout to handle logs and errors
sys.stdout = Logs()
# Send logs at exit
atexit.register(sys.stdout.end_process)
```

See [main.py](main.py) for an example.