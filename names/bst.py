
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # case 1: value is less than self.value
        if value < self.value:
            # if there is no left child, insert value here
            if self.left is None:
                self.left = BSTNode(value)
            # else: 
            else:
                # repeat the process on left subtree (recursive?)
                self.left.insert(value)
        # case 2: value is greater than self.value
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        # case 3: value is equal to self.value
        # return true if the tree contains the value
        # false if it does not
        # duplicates are okay and should go to the right for the solution

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Case 1: if self.value is = to target
        if self.value == target:
            return True
        # Case 2: target is less than self.value
        if target < self.value:
            # if self.left is None, it isn't in tree
            if self.left is None:
                return False
            else: # you return because you are asking to RETURN a boolean back
                return self.left.contains(target)
        # Case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
           
    # Return the maximum value found in the tree
    def get_max(self):
        # forget about the left subtree
        # iterate through the nodes using a loop construct
        if self.right is not None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # recursive solution
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal (deepest node is visited and then backtracks to it’s parent node if no sibling of that node exist. )
    def in_order_print(self, node):
        # first recur on left child
        if node.left is not None:
            self.in_order_print(node.left)
            # then print node
        print(node.value)    
        # now recure on the right child
        if node.right is not None:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # level by level traversal
    def bft_print(self, node):
        # most important
        # use a queure to form a line
        # for the nodes to get in
        # start by placing the root in the queue
        # need a while loop to iterate through
        # what are we checking in the while statement
        # while length of queue is greater than 0
            # dequeue item from front of queue
            # print that item
            # place current item's left node in queue if not None
            # place current item's right node in queue if not None
        queue = []
        queue.append(node)
        while len(queue) > 0:
            print(queue[0].value)
            if queue[0].left is not None:
                queue.append(queue[0].left)
            if queue[0].right is not None:
                queue.append(queue[0].right)
            queue.pop(0)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # most important
        # initialize an empty stack
        # push the root node onto the stack
        # need a while loop to manager our iteration
        # if stack is not empty entrer the while loop
            # pop top item off the stack
            # print that item's value
            # if there is a right subtree
                # push right item onto the stack
            # if there is a left subtree
                # push left item onto the stack
        stack = []
        stack.append(node)
        curr_node = node
        while len(stack) > 0:
            # switch to 0 for breadth first
            curr_node = stack.pop(len(stack)-1)
            if curr_node.right is not None:
                stack.append(curr_node.right)

            if curr_node.left is not None:
                stack.append(curr_node.left)

            print(curr_node.value)