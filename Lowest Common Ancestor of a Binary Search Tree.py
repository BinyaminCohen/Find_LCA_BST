# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants
#
# (where we allow a node to be a descendant of itself).”


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_LCA_BST(root, p, q):
    """
    Find the lowest common ancestor (LCA) of two given nodes in the BST.

    :param root: TreeNode, the root of the binary search tree
    :param p: TreeNode, one of the two nodes
    :param q: TreeNode, the other node
    :return: TreeNode, the LCA of nodes p and q
    """
    current_node = root
    while current_node:
        # If both p and q are greater than current_node, LCA lies in right subtree
        if p.value > current_node.value and q.value > current_node.value:
            current_node = current_node.right
        # If both p and q are less than current_node, LCA lies in left subtree
        elif p.value < current_node.value and q.value < current_node.value:
            current_node = current_node.left
        else:
            # We have found the split point, i.e., the LCA node.
            return current_node


# Example usage
# Constructing a simple BST
#         6
#        / \
#       2   8
#      / \ / \
#     0  4 7  9
#       / \
#      3   5

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4, TreeNode(3), TreeNode(5))
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

p = root.left  # Node with value 2
q = root.left.right  # Node with value 4

lca = find_LCA_BST(root, p, q)
print(f"LCA of {p.value} and {q.value} is {lca.value}")
