#手続き型プログラミング#
x = 2
y = 4
z = 5
xyz = x + y + z
print(xyz)

pop = []
jpop = []


#def collect_songs():
#    song = "曲名を入力してください"
#    ask = "pかjのどちらかを入力してください。qで終了します。"
#
#    while True:
#        genre = input(ask)
#        if genre == "q":
#            break
#        elif genre == "p":
#            p = input(song)
#            pop.append(p)
#
#        elif genre == "j":
#            j == input(song)
#             jpop.append(j)
#
#        else:
#            print("不正な値です")

#        print("pop songs: ", pop)
#        print("jpop songs: ", jpop)


#collect_songs()


#関数型プログラミング#

a = 0

def increment():#グローバル変数を変える#
    global a
    a += 1
    print (a)

increment()

def increment(a):#関数の変数を利用する#
    return a + 1
    
print(increment(5))

#オブジェクト指向プログラミング#
    
class Orange:
    def __init__(self, w, c, s):
        self.weight = w
        self.color = c
        self.size = s
        print ("Created!")

or1 = Orange(10, "dark orange", "large")

or1.color = "light orange"
or1.weight = 200


print (or1.weight)
print(or1.color)
print(or1.size)

or2 = Orange(15, "dark Orange", "small")
or3 = Orange(60, "yellow", "big")

class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        self.mold = days * temp

orange = Orange(200, "dark orange")
print(orange.mold)
orange.rot(10, 40)
print(orange.mold)

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l

rectangle = Rectangle(10, 5)
print(rectangle.area())
rectangle.change_size(20, 4)
print(rectangle.area())

