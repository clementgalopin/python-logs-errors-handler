import time
import atexit
import sys

from logs import Logs

# Rewrite stdout to handle logs and errors
sys.stdout = Logs()
# Send logs at exit
atexit.register(sys.stdout.end_process)

print("--- Starting ---")

start_time = time.time()    

try:
    a = 1 / 0
except:
    print('Warning: pay attention')

try:
    a = 1 / 0
except:
    print('Error: sth wrong')

print("--- %s seconds ---" % (time.time() - start_time))