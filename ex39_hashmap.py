def new(num_buckets=256):
	"""Initialize a Map with the given number of buckets."""
	
	#create aMap var that has a list
	aMap = []

	#put num_buckets lists inside aMap
	#used to hold the contents of the hashmap
	for i in range(0, num_buckets):
		aMap.append([])

	return aMap

def hash_key(aMap, key):
	"""Given a key this will create a number and then convert
	it to an index for the aMap's buckets."""
	#ues hash function to convert string to number
	#then use mod and len(aMap) to get a bucket where
	#the key can go
	return hash(key) % len(aMap)

def get_bucket(aMap, key):
	"""Given a key, find the bucket where it would go"""
	#call hash_key to find bucket key could be in
	bucket_id = hash_key(aMap, key)
	return aMap[bucket_id]

def get_slot(aMap, key, default=None):
	"""
	Return the index, key, and value of a slot found in a bucket.
	Returns -1, key, and default (None if not set) when not found.
	"""
	#use get_bucket to get the bucket the key could be in
	bucket = get_bucket(aMap, key)
	
	#go through every element in the bucket the key 
	#could be in until it finds a match
	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			# returns index the key was found in, the key 
			#itself, and the value
			return i, k, v

	return -1, key, default

def get(aMap, key, default = None):
	"""Gets the value in a bucket for the given key, or the 
	default."""
	#use get slot to get i k and v
	i, k, v = get_slot(aMap, key, default=default)

	#returns v
	return v

def set(aMap, key, value):
	"""Sets the key to the value, replacing any existing value"""
	bucket = get_bucket(aMap, key)
	i, k, v = get_slot(aMap, key)

	if i >= 0:
		#the key exists, replace it
		bucket[i] = (key, value)
	else:
		#the key does not, append to create it
		bucket.append((key, value))

def delete(aMap, key):
	"""Deletes the given key from the Map"""
	#get bucket
	bucket = get_bucket(aMap, key)

	#find key in bucket
	for i in xrange(len(bucket)):
		k, v = bucket[i]
		if key == k:
			#delete key
			del bucket[i]
			break

def list(aMap):
	"""Prints out what's in the Map."""
	for bucket in aMap:
		if bucket:
			for k, v in bucket:
				print k, v