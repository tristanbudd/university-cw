# Question 1:
# Implement a Queue using an Array/List:
# Recall that a Queue ADT should support the following methods:
#  Enqueue Add an element to the tail (rear) of the queue
#  Dequeue Remove the element from the head (front) of the queue
#  Peek View the element at the head of the queue without removing it
#  Length Return the number of elements in the queue
def question_1():
    class Queue:
        def __init__(self):
            self.max_queue_size = 5
            self.queue = [None] * self.max_queue_size
            self.front = 0
            self.back = -1
            self.count = 0

        def enqueue(self, number):
            if self.count == self.max_queue_size:
                raise OverflowError("The queue is currently full.")
            else:
                self.back = (self.back + 1) % self.max_queue_size
                self.queue[self.back] = number
                self.count += 1

                print(f"Debug | Added {number} to the queue.")
                print(f"Current Queue: {self.queue}")

        def dequeue(self):
            if self.count < 1:
                raise ValueError("Nothing in the queue to remove.")
            else:
                value_to_remove = self.queue[self.front]

                self.queue[self.front] = None
                self.front = (self.front + 1) % self.max_queue_size
                self.count -= 1

                print(f"Debug | Removed {value_to_remove} from the queue.")
                print(f"Current Queue: {self.queue}")

                return value_to_remove

        def peek(self):
            if self.count < 1:
                raise ValueError("There is nothing currently in queue.")
            else:
                peek_value = self.queue[self.front]

                print(f"Debug | Peak value at the front of the queue is: {peek_value}")

                return peek_value

        def length(self):
            print(f"Debug | There are {self.count} numbers in queue.")

            return self.count

    # Test Data
    queue_test = Queue()

    queue_test.enqueue(4)
    queue_test.enqueue(2)
    queue_test.enqueue(5)
    queue_test.enqueue(7)

    queue_test.peek()
    queue_test.length()

    queue_test.dequeue()
    queue_test.dequeue()
    queue_test.dequeue()

    queue_test.peek()
    queue_test.length()

    queue_test.enqueue(9)
    queue_test.enqueue(3)

    queue_test.dequeue()


# Question #2
# Implement a Stack using an Array/List:
# Recall that a Stack ADT should support the following methods:
#  Push Add an element to the top of the stack
#  Pop Remove the element from the top of the stack
#  Peek View the element at the top of the stack without removing it
#  Length Return the number of elements in the stack
def question_2():
    class Stack:
        def __init__(self):
            self.max_stack_size = 5
            self.stack = [None] * self.max_stack_size
            self.top = -1
            self.count = 0

        def push(self, number):
            if self.count == self.max_stack_size:
                raise OverflowError("The stack is currently full.")
            else:
                self.top += 1
                self.stack[self.top] = number
                self.count += 1

                print(f"Debug | Pushed {number} onto the stack.")
                print(f"Current Stack: {self.stack}")

        def pop(self):
            if self.count == 0:
                raise ValueError("Nothing in the stack to pop.")
            else:
                value_to_remove = self.stack[self.top]
                self.stack[self.top] = None
                self.top -= 1
                self.count -= 1

                print(f"Debug | Popped {value_to_remove} from the stack.")
                print(f"Current Stack: {self.stack}")

                return value_to_remove

        def peek(self):
            if self.count == 0:
                raise ValueError("Stack is empty.")
            else:
                peek_value = self.stack[self.top]

                print(f"Debug | Top value of the stack is: {peek_value}")

                return peek_value

        def length(self):
            print(f"Debug | There are {self.count} numbers in the stack.")
            return self.count

    # Test Data
    stack_test = Stack()

    stack_test.push(4)
    stack_test.push(2)
    stack_test.push(5)
    stack_test.push(7)

    stack_test.peek()
    stack_test.length()

    stack_test.pop()
    stack_test.pop()
    stack_test.pop()

    stack_test.peek()
    stack_test.length()

    stack_test.push(9)
    stack_test.push(3)

    stack_test.pop()


# Question #3:
# Design an algorithm to reverse a Queue using Stacks and Queues.
# (Example: Convert Queue “12345” into Queue “54321”.)
def reverse_queue(queue):
    return queue[::-1]


# Question #4:
# Made the executive decision to skip this, as I already make both Question #1 and Question #2 a circular queue system.


# Question #5:
# Design an algorithm to continuously remove adjacent duplicate letters from
# a string until no adjacent duplicates remain, using a Stack or a Queue. Can
# you also implement this using the alternative ADT?
# (Example: Convert “abbccd” to “ad”, “dsallasg” to “dg”, and “abccbadd” to an
# empty string.)
def remove_adjacent_characters(data):
    stack = []

    for char in data:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return ''.join(stack)


# Question #6:
# Develop an algorithm to determine if the brackets in a string are valid, using
# a Stack or a Queue. This means open brackets must be closed by the same
# type of brackets in the correct order. Can you implement this using the other
# ADT?
# (Example: “(abc)” returns True, “ds” returns True, and “[a{b]c}” returns False.)
def brackets_validation(data):
    stack = []
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for char in data:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
            stack.pop()

    return True


def main():
    question_1()
    question_2()

    # Question #3
    print(reverse_queue([1, 2, 3, 4, 5]))

    # Question #5
    print(remove_adjacent_characters("abbccd"))
    print(remove_adjacent_characters("dsallasg"))
    print(remove_adjacent_characters("abccbadd"))

    # Question #6
    print(brackets_validation("(abc)"))
    print(brackets_validation("ds"))
    print(brackets_validation("[a{b]c}"))


if __name__ == "__main__":
    main()