from collections import deque

# Create a new deque
my_deque = deque()

# Adding elements to the right end (append)
my_deque.append(1)
my_deque.append(2)
my_deque.append(3)
print("After appending 1, 2, 3:", my_deque)

# Adding elements to the left end (appendleft)
my_deque.appendleft(0)
print("After appendleft(0):", my_deque)

# Removing elements from the right end (pop)
right_element = my_deque.pop()
print(f"Popped from right: {right_element}")
print("After pop():", my_deque)

# Removing elements from the left end (popleft)
left_element = my_deque.popleft()
print(f"Popped from left: {left_element}")
print("After popleft():", my_deque)

# Check the length of deque
print("Deque length:", len(my_deque))

# Check if element exists in deque
print("Is 2 in deque?", 2 in my_deque)

# Create a deque with maximum size (maxlen)
limited_deque = deque(maxlen=3)
for i in range(5):
    limited_deque.append(i)
    print(f"After appending {i}:", limited_deque)