WHITE = 0
GRAY = 1
BLACK = 2

def parent(n):
    return (n-1)/2

def left(n):
    return 2*n+1

def right(n):
    return 2*n+2

def max_heapify(A,i,heapsize):
    l=left(i)
    r=right(i)
    if l<heapsize and A[l]<A[i]:
        largest =l
    else:
        largest=i
    if r<heapsize and A[r]<A[largest]:
        largest=r
    if largest!=i:
        A[i], A[largest]=A[largest],A[i]
        max_heapify(A,largest,heapsize)

def build_a_heap(A):
    for i in range(len(A)//2,0,-1):
        max_heapify(A,i-1,len(A))
def max_heapsort(A):
    build_a_heap(A)
    for i in range(len(A),1,-1):
        A[i-1],A[0]=A[0],A[i-1]
        max_heapify(A,0,i-1)


class Adj:
    def __init__(self):
        self.n = 0
        self.next = None


class Vertex:
    def __init__(self, name):
        self.color = WHITE
        self.parent = -1
        self.name = name
        self.n = 0
        self.first = None

    def add(self, v):
        a = Adj()
        a.n = v.n
        a.next = self.first
        self.first = a

    def copy(self, other):
        self.color = other.color
        self.parent = other.parent
        self.name = other.name
        self.n = other.n
        self.first = other.first


class DFSVertex(Vertex):
    def __init__(self, name):
        super().__init__(name)
        self.d = 0
        self.f = 0

    def copy(self, other):
        super().copy(other)
        self.d = other.d
        self.f = other.f


class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.sz = 0
        self.buf = []

    def create_queue(self, sz):
        self.sz = sz
        self.buf = list(range(sz))  # malloc(sizeof(int)*sz)

    def enqueue(self, val):
        self.buf[self.rear] = val
        self.rear = (self.rear + 1) % self.sz

    def dequeue(self):
        res = self.buf[self.front]
        self.front = (self.front + 1) % self.sz
        return res

    def is_empty(self):
        return self.front == self.rear


def print_vertex(vertices, n):
    print(vertices[n].name, end=' ')
    print(vertices[n].color, end=' ')
    print(vertices[n].parent, end=' ')
    print(vertices[n].d, end=':')
    p = vertices[n].first
    while p:
        print(vertices[p.n].name, end=' ')
        p = p.next
    print('')


def g_transpose(vertices, vertices1):
    for i in range(len(vertices1)):
        vertices1[i].first = None
    for v in vertices:
        p = v.first
        while p:
            vertices1[p.n].add(v)
            p = p.next


class DepthFirstSearch:
    def __init__(self):
        self.time = 0;
        self.vertices = None

    def set_vertices(self, vertices):
        self.vertices = vertices
        for i in range(len(self.vertices)):
            self.vertices[i].n = i

    def dfs(self):
        for u in self.vertices:
            u.color = WHITE
            u.parent = -1
        self.time = 0
        for u in self.vertices:
            if u.color == WHITE:
                self.dfs_visit(u)

    def dfs_visit(self, u):
        self.time = self.time + 1
        u.d = self.time
        u.color = GRAY
        v = u.first
        while v:
            if self.vertices[v.n].color == WHITE:
                self.vertices[v.n].parent = u.n
                self.dfs_visit(self.vertices[v.n])
            v = v.next;
        u.color = BLACK
        self.time = self.time + 1
        u.f = self.time

    def print_scc(self, u):
        print(u.name, end=" ")
        vset = self.vertices
        if u.parent >= 0:
            self.print_scc(vset[u.parent])

    def scc_find(self, u):
        u.color = GRAY
        v = u.first
        found = False
        while v:
            if self.vertices[v.n].color == WHITE:
                found = True
                self.vertices[v.n].parent = u.n
                self.scc_find(self.vertices[v.n])
            v = v.next
        if not found:
            print("SCC:", end=" ")
            self.print_scc(u)
            print("")
        u.color = BLACK

    def print_vertex(self, n):
        print(self.vertices[n].name, end=' ')
        print(self.vertices[n].color, end=' ')
        print(self.vertices[n].parent, end=' ')
        print(self.vertices[n].d, end=' ')
        print(self.vertices[n].f, end=':')
        p = self.vertices[n].first
        while p:
            print(self.vertices[p.n].name, end=' ')
            p = p.next
        print('')

    def print_vertices(self):
        for i in range(len(self.vertices)):
            self.print_vertex(i)

    def transpose(self):
        vertices1 = []
        for v in self.vertices:
            v1 = DFSVertex(v.name)
            v1.copy(v)
            vertices1.append(v1)
        g_transpose(self.vertices, vertices1)
        self.set_vertices(vertices1)

    def left(self, n):
        return 2 * n + 1

    def right(self, n):
        return 2 * n + 2

    def heapify(self, A, i, heapsize):
        vset = self.vertices
        l = self.left(i)
        r = self.right(i)
        if l < heapsize and vset[A[l]].f > vset[A[i]].f:
            largest = l
        else:
            largest = i
        if r < heapsize and vset[A[r]].f > vset[A[largest]].f:
            largest = r
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.heapify(A, largest, heapsize)

    def buildheap(self, A):
        for i in range(len(A) // 2 + 1, 0, -1):
            self.heapify(A, i - 1, len(A))

    def heapsort(self, A):
        self.buildheap(A)
        for i in range(len(A), 1, -1):
            A[i - 1], A[0] = A[0], A[i - 1]
            self.heapify(A, 0, i - 1)

    def sort_by_f(self):
        vset = self.vertices
        sorted_indices = list(range(len(vset)))
        self.heapsort(sorted_indices)
        return sorted_indices

    def scc(self):
        self.dfs()
        self.print_vertices()
        self.transpose()
        sorted = self.sort_by_f()
        vset = self.vertices
        for v in vset:
            v.color = WHITE
            v.parent = -1
        for n in sorted:
            if self.vertices[n].color == WHITE:
                self.scc_find(vset[n])


userprofilelist = []
userfriendship = []
tweets = []
class Node:
    def __init__(self):
        self.number = 0
        self.date = None
class Frequency:
    def __init__(self):
        self.frequency = 0
        self.key = None


class User:
    def __init__(self):
        super().__init__()
        self.id = None

class Word:
    def __init__(self):
        super().__init__()
        self.tweet = None

class Friend:
    def __init__(self):
        self.id = 0
        self.following = None

def menu_0 ():
    userfile = open('user_sample.txt')
    i = 0

    for line in userfile:
        line = line[0:-1]
        if ((i%4) ==0): #i starts with 0, which is the starting point of each user's information.
            user = User()
            user.number = line
        elif ((i%4)==1):
            user.date = line
        elif ((i%4)==2):
            user.id = line
        elif ((i%4)==3):
            userprofilelist.append(user)
        i = i+1
     #   print(line)
    friendfile = open('friend_sample.txt')
    j = 0
    for line in friendfile:
        line = line [0:-1]
        if ((j%3) ==0):
            user = Friend()
            user.number = line
        elif ((j%3) == 1):
            user.following = line
        elif ((j%3) == 2):
            userfriendship.append(user)
        j = j+1

    with open("word_sample.txt", "r", encoding ="utf-8") as wordfile:
        k =0
        for line in wordfile:
            line = line [0:-1]
            if ((k%4)==0):
                user = Word()
                user.number = line
            elif ((k%4)==1):
                user.date = line
            elif ((k%4)==2):
                user.tweet = line
            elif ((k%4)==3):
                tweets.append(user)
            k = k+1
    print("Total users:", len(userprofilelist))
    print("Total friendship records", len(userfriendship))
    print("Total tweets", len(tweets))

#inversing hashtable
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

#word hashing
def wordhashing():
    word_hashtable = {}
    for tw in tweets:
        #print(tw.tweet)
        if(tw.tweet in word_hashtable):
            temp = word_hashtable.get(tw.tweet)
            temp.append(tw.number)
            word_hashtable[tw.tweet] = temp
            #print(tw.tweet)
        else:
            word_hashtable[tw.tweet] = [tw.number]
 #   return word_hashtable

    #sorting from the most frequent words mentioned
    freq_list = []

    for tw_hashkey in word_hashtable:
        value = word_hashtable.get(tw_hashkey)
        if(len(value) > 2):
            set = [len(value), tw_hashkey]
            freq_list.append(set)
    max_heapsort(freq_list)
    #print(freq_list)
    print("Top 5 most tweeted words:", freq_list[0][1],freq_list[1][1],freq_list[2][1],freq_list[3][1],freq_list[4][1])

#user hashing
def userhashing():
    user_hashtable= {}
    for tw in tweets:
        if tw.number in user_hashtable:
            buffer = user_hashtable.get(tw.number)
            buffer.append(tw.tweet)
            user_hashtable[tw.number]=buffer
        else:
            user_hashtable[tw.number] = [tw.tweet]

    chatterbox = []

    for tw_hashkey in user_hashtable:
        value = user_hashtable.get(tw_hashkey)
        if(len(value) > 2):
            set = [len(value), tw_hashkey]
            chatterbox.append(set)
    max_heapsort(chatterbox)
    print("Top 5 most tweeted users:",chatterbox[0][1],chatterbox[1][1],chatterbox[2][1],chatterbox[3][1],chatterbox[4][1])



    # #top5 most tweeted users
    # inverse = invert_dict(word_hashtable)
    # chatterbox = []
    #
    # for tw_user in inverse:
    #     value = inverse.get(tw_user)
    #     if(len(value) > 2):
    #         set = [len(value), tw_user]
    #         freq_list.append(set)
    # max_heapsort(chatterbox)
    # print(chatterbox)
    # print("Top 5 most tweeted words:", chatterbox[0][1],chatterbox[1][1],chatterbox[2][1],chatterbox[3][1],chatterbox[4][1])


def menu_2():
    wordhashing()
    freq_list = []

    # for tw_hashkey in word_hashtable:
    #     value = word_hashtable.get(tw_hashkey)
    #     if(len(value) > 2):
    #         set = [len(value), tw_hashkey]
    #         freq_list.append(set)
    # max_heapsort(freq_list)
    # print("Top 5 most tweeted words:", freq_list[0][1], freq_list[1][1], freq_list[2][1], freq_list[3][1], freq_list[4][1])




def menu_3 ():
    wordhashing()



def main():
    word = open('word.txt')
    friend = open('friend.txt')
    user = open('user.txt')

    for line in word:
        line = line[0:-1]
        print (line)






def MainMenu():
    print("0: Read Data Files")
    print("1: Display Statistics")
    print("2: Top 5 most tweeted words")
    print("3: Top 5 most tweeted users")
    print("4: Find users who Tweeted a word")
    print("5: Find all people who are friends of the above users")
    print("6: Delete all mentions of a word")
    print("7: Delete all users who mentioned a word")
    print("8: Find strongly connected components")
    print("9: Find shortest path from a given user")
    print("99: Quit")
    print("Select Menu:")





#main ()
MainMenu()
menu_0()
menu_2()
userhashing()