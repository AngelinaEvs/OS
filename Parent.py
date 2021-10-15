import os
import sys
import random
import time

# Ангелина Евсикова, 11-902

n = int(sys.argv[1])
for i in range(0, n):
	t = os.fork()
	if (t > 0):
		if (i == 0):
			print("Parent pid=%d" % (os.getpid()))
		else:
			os.execl("./Child.py", "Child.py", str(n))
			break
for i in range(0, n):
	ans = os.wait()
	print("Child pid=%d was completed. Status: %d" % (ans[0], ans[1]))