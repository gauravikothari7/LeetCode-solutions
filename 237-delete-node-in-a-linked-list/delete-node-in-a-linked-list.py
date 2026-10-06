class Solution:
    def deleteNode(self, node):
        node.val = node.next.val        # Step 1: copy next number
        node.next = node.next.next      # Step 2: skip the next box