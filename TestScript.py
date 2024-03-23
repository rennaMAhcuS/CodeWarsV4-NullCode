class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def build_balanced_bst(start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    root = TreeNode(mid + 1)
    root.left = build_balanced_bst(start, mid - 1)
    root.right = build_balanced_bst(mid + 1, end)
    return root


def level_order_traversal(root):
    if not root:
        return []
    queue = [root]
    result = []
    while queue:
        current = queue.pop(0)
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result


def generate_sequence(Num):
    bst_root = build_balanced_bst(0, Num - 1)
    return level_order_traversal(bst_root)