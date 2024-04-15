
# provides implementation of the heap queue algorithm
import heapq

# listof values
values = [6,8,1,9,7,2]
heapq.heapify(values)
print(values)

# Inserting a Heap
# Push the value item onto the heap, maintaining the heap invariant.
heapq.heappush(values,21)
print(values)

# Removing from heap

# Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised
heapq.heappop([3])
print(values)

# Replacing in a Heap
# Pop and return the smallest item from the heap, and also push the new item. 
heapq.heapreplace(values,45)
print(values)

print(heapq.nlargest(2,values))
print(heapq.nsmallest(2,values))
