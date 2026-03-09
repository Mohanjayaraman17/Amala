class StackUsingList:
    def __init__(self):
        self.stack = []

    def push(self, item):
        # Add item to the end of the list
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        # Remove and return the last item
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")
            return None

    def peek(self):
        # View the last item
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")
            return None

    def is_empty(self):
        return len(self.stack) == 0

# Example Usage:
my_stack_list = StackUsingList()
my_stack_list.push(10)
my_stack_list.push(20)
print(f"Peek: {my_stack_list.peek()}")
print(f"Popped: {my_stack_list.pop()}")
print(f"Is empty: {my_stack_list.is_empty()}")
