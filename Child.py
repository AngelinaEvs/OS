import os
import sys
import random
import time

# Ангелина Евсикова, 11-902

print("Child pid = %d. Sleep = %d s" % (os.getpid(), int(sys.argv[1])))
time.sleep(int(sys.argv[1]))
print("Child (pid  = %d) finished" % (os.getpid()))
os._exit(random.randint(0, 1))