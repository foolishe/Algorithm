import random
import functools,math,operator

class binary_tree_element:
    def __init__(self,e):
        self.key = e
        self.left = None
        self.right = None
        self.p = None

    def __repr__(self):
        fmt = 'key: {},left: {},right: {},p: {}'
        return fmt.format(self.key,self.left.key,self.right.key,self.p.key)

    def __eq__(self,other):
        return bool(self.key == other)

    def __hash__(self):
        hashes = (hash(x) for x in [self.key,self.p.key,
            self.left.key,self.right.key])
        return functools.reduce(operator.xor,hashes,0)


class binary_tree:
    def __init__(self):
        self.Nil = binary_tree_element(None)
        self.root = None
        self.res = []

    def insert(self,e):
        z = binary_tree_element(e)
        y = self.Nil
        x = self.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == None:
            self.root = z
        elif z.key >= y.key:
            y.right = z
        else:
            y.left = z
        z.left = self.Nil
        z.right = self.Nil

    def Inorder_tree_walk(self,x):
        if x != None:
            self.Inorder_tree_walk(x.left)
            self.res.append(x.key)
            self.Inorder_tree_walk(x.right)
        return self.res

    def search_key(self,root,k):

        if root == None or k == root.key:
            try:
                return root ,'index: '+str(self.res.index(root.key))
            except:
                return None
        if k < root.key:
            return self.search_key(root.left,k)
        else:
            return self.search_key(root.right,k)

    def __len__(self):
        return len(self.res)

    def __getitem__(self,index):
        return self.res[index]

    def __iter__(self):
        return (i for i in self.res)

view_T = []
def get_tree(L):
    global view_T
    new = []
    for i in L:
        if i.left != None:
            new.append(i.left)
            view_T.append(i.left)
        else:
            view_T.append(None)
        if i.right != None:
            new.append(i.right)
            view_T.append(i.right)
        else:
            view_T.append(None)
    return new

def view_tree(T):
    global view_T
    view_T.append(T.root)
    L = [T.root]
    new = get_tree(L)
    while new:
        new = get_tree(new)





L = [random.randrange(i) for i in range(10,3000)]
key = random.choice(L)
T = binary_tree()
while L:
    random.shuffle(L)
    T.insert(L.pop())

print(T.Inorder_tree_walk(T.root))
print(T.search_key(T.root,key))

print(T.root)
view_tree(T)
for i in view_T:
    print(i)

def longest_single_path(key):
    x = 1
    while key.p != None:
        key = key.p
        x += 1
    return x+1

while None in view_T:
    view_T.remove(None)

print(longest_single_path(view_T[-1]),math.log2(len(T)))
