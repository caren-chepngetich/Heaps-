import heapq

values = [6,8,1,9,7,2]
heapq.heapify(values)
print(values)

# Inserting a Heap
heapq.heappush(values,21)
print(values)

# Removing from heap
heapq.heappop([3])
print(values)

# Replacing in a Heap
heapq.heapreplace(values,45)
print(values)