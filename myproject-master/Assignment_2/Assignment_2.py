class MyStack:
    def __init__(self):
        self.arr = []
    def push(self, val):
        self.arr.append(val)
    def pop(self):
        if self.is_empty():
            raise IndexError("stack empty")
        return self.arr.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("stack empty")
        return self.arr[-1]
    def is_empty(self):
        return len(self.arr) == 0
    def size(self):
        return len(self.arr)


class MyQueue:
    def __init__(self):
        self.inp = []
        self.out = []
    def _shift(self):
        if not self.out:
            while self.inp:
                self.out.append(self.inp.pop())
    def enqueue(self, val):
        self.inp.append(val)
    def dequeue(self):
        self._shift()
        if self.is_empty():
            raise IndexError("queue empty")
        return self.out.pop()
    def peek(self):
        self._shift()
        if self.is_empty():
            raise IndexError("queue empty")
        return self.out[-1]
    def is_empty(self):
        return not (self.inp or self.out)
    def size(self):
        return len(self.inp) + len(self.out)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
    def prepend(self, val):
        n = Node(val)
        n.next = self.head
        self.head = n
    def append(self, val):
        n = Node(val)
        if not self.head:
            self.head = n
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = n
    def delete(self, val):
        cur = self.head
        prev = None
        while cur:
            if cur.val == val:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return True
            prev, cur = cur, cur.next
        return False
    def display(self):
        vals = []
        cur = self.head
        while cur:
            vals.append(str(cur.val))
            cur = cur.next
        s = " -> " + " -> ".join(vals) if vals else ""
        print(s.strip())
        return s.strip()


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class MyBST:
    def __init__(self):
        self.root = None
    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return
        cur = self.root
        while True:
            if val == cur.val:
                return
            if val < cur.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = TreeNode(val)
                    return
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val)
                    return
    def search(self, val):
        cur = self.root
        while cur:
            if val == cur.val:
                return True
            cur = cur.left if val < cur.val else cur.right
        return False
    def inorder(self):
        res = []
        def dfs(n):
            if not n: return
            dfs(n.left)
            res.append(n.val)
            dfs(n.right)
        dfs(self.root)
        return res
    def preorder(self):
        res = []
        def dfs(n):
            if not n: return
            res.append(n.val)
            dfs(n.left)
            dfs(n.right)
        dfs(self.root)
        return res
    def postorder(self):
        res = []
        def dfs(n):
            if not n: return
            dfs(n.left)
            dfs(n.right)
            res.append(n.val)
        dfs(self.root)
        return res


class MyMap:
    def __init__(self, cap=16):
        self.buckets = [[] for _ in range(cap)]
        self.count = 0
    def _hash(self, k):
        return hash(k) % len(self.buckets)
    def put(self, k, v):
        i = self._hash(k)
        for pair in self.buckets[i]:
            if pair[0] == k:
                pair[1] = v
                return
        self.buckets[i].append([k, v])
        self.count += 1
    def get(self, k):
        i = self._hash(k)
        for pair in self.buckets[i]:
            if pair[0] == k:
                return pair[1]
        return None
    def remove(self, k):
        i = self._hash(k)
        for idx, pair in enumerate(self.buckets[i]):
            if pair[0] == k:
                self.buckets[i].pop(idx)
                self.count -= 1
                return True
        return False
    def size(self):
        return self.count


if __name__ == "__main__":
    s = MyStack()
    s.push(1); s.push(2); s.push(3)
    print(s.pop())

    q = MyQueue()
    q.enqueue("a"); q.enqueue("b")
    print(q.dequeue())

    ll = MyLinkedList()
    ll.append(10); ll.prepend(5); ll.append(15)
    ll.display()
    ll.delete(10)
    ll.display()

    bst = MyBST()
    for x in [5,3,7,2,4,6,8]:
        bst.insert(x)
    print(bst.inorder())
    print(bst.search(6))

    mp = MyMap()
    mp.put("name","Eve")
    mp.put("age",22)
    print(mp.get("name"))
    mp.remove("age")
    print(mp.size())
