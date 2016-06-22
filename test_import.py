class Node:
    def __init__(self):
        self.number = 0
        self.date = None


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
    userfile = open('user.txt')
    i = 0
    userprofilelist = []
    for line in userfile:
        line = line[0:-1]
        if ((i%4) ==0): #i starts with 0, which is the starting point of each user's information.
            user = User()
        elif ((i%4)==1):
            user.number = line
        elif ((i%4)==2):
            user.date = line
        elif ((i%4)==3):
            user.id = line
            userprofilelist.append(user)
        i = i+1

    friendfile = open ('friend.txt')
    j = 0
    userfriendship = []
    for line in friendfile:
        line = line [0:-1]
        if ((j%3) ==0):
            user = Friend()
        elif ((j%3) == 1):
            user.number = line
        elif ((j%3) == 2):
            user.following =line
            userfriendship.append(user)
        j = j+1

    wordfile = open ('word.txt')
    k = 0
    tweets = []
    for line in wordfile:
        line = line [0:-1]
        if ((k%4)==0):
            user = Word()
        elif ((k%4)==1):
            user.number = line
        elif ((k%4)==2):
            user.date = line
        elif ((k%4)==3):
            user.tweet = line
        k = k+1
    print("Total users:", i)
    print("Total friendship records:", j)
    print("Total tweets:", k)







""
def main():
    word = open('word.txt')
    friend = open('friend.txt')
    user = open('user.txt')

    for line in word:
        line = line[0:-1]
        print (line)

""




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