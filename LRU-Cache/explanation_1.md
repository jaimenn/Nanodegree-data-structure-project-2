#Runtime complexity;
# I created a class object as LRU_Cache and created
# methods in it
# I used a dictionary as cache. This stores
# keys and values that we want.
# And I used another dictionary as lru_key_cache.
# This stores keys and use_rates of keys.
# get(key) method returns the value of key and updates the 
# use_rate of key. This method runs in a constant time.
# Big O is O(1).
# set(key, value) method controls if capacity is full. if
# full removes the last recently used item.  
# Then sets key and value in cache dictionary Big O if this
# This code runs in constant time. Big O is O(1)


# Space complexity of this algorithm is O(n) 
#because we keep  n values which is given us with "capacity" variable