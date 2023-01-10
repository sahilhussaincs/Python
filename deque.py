from collections import deque
stack = deque()
stack.append('https://edition.cnn.com/')
stack.append('https://edition.cnn.com/world')
stack.append('https://edition.cnn.com/americas')
print(stack.pop())