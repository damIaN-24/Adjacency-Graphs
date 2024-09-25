class Stack:
  def __init__(self, value):
    self.stack = [None]

  def push(self, value):
      self.stack.append(value)

  def pop(self):
      if self.stack:
          return self.stack.pop()
      else:
          raise IndexError('Stack is empty')

  def get_size(self):
      return len(self.stack)