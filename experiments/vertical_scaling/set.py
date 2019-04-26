import redis
import random
import string
import time
import csv

def randString(n):
	''' Returns a random string of length n'''
	s = ''.join(random.choice(string.ascii_uppercase + string.digits \
				+ string.ascii_lowercase) for _ in range(n))
	return s

keys = []
values = []

with open('keyVal.txt') as f:
	lines = f.readlines()
n = len(lines)
m = 256

for i in range(n):
	x, y = lines[i].strip().split(',')
	keys.append(x)
	values.append(y)
client = redis.Redis(host='localhost', port=6379, db=0)

# delete existing keys, if any
client.flushall()

start = time.time()

num_queries = int(n/2)

for i in range(num_queries):
    client.set(keys[i], values[i])
for i in range(num_queries):
    idx = random.randint(0, num_queries-1)
    client.get(keys[idx])
end = time.time()

print(end-start)
