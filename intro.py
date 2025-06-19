print("Hello" +"World")
print("Oh no")
print("python is fun")
print("python is fun")



print (100/25)
print(3/6)


print(5==5)

user_name="Kimani"
print(f"My user name is {user_name * 2}")

dog_name = "Lucy"
print(f"Say hello to my dog {dog_name}".upper())

comp_name="mac-book"
print(f"My computer's name is {comp_name}".capitalize())

# dir("hello")
# print(dir(user_name))

my_dict={"Key1":'Anna', "Key2":"Macharia", "Value":"Jane"}
print(my_dict["Key1"]," \n", my_dict["Value"])


my_obj= { "key22": "runnig", "key42": "walking" }
print(my_obj ["key22"])


print(int(2.5+1.6))

# count = 1
# while count < 99:
#     print("%I love you" % count)

count = 1
while count <= 3:
    print("I love you")
    count+=1

def hello(name):
    return "Hello "+(name)
print(hello("kimani"))

greeting=hello 
print(greeting("macharia"))


def morining(name):
    print("Hello from the morning() function.")

    def greet():
        print("Greetings from the morning() function."+name)

    return greet
morining("Vincent")()


def decorator(fun):
    def wrapper():
        print("I am the output that lets you know the function is about to be called.")
        fun()
        print("I am the output that lets you know the function has been called.")
    return wrapper

def get_called():
    print("I am the function and I am being called.")
# decorator(wrapper())
decorator(get_called())

print("\n")
# @decorator
# def get_called():
#     print("I am the function and I am being called.")

get_called()

print("\n")
# def sweep_floors(time):
#     if 1100 < time < 2100:
#         print("Sweeping the floors...")
#     else:
#         print("I'm off duty!")

# def wash_dishes(time):
#     if 1100 < time < 2100:
#         print("Washing the dishes...")
#     else:
#         print("I'm off duty!")

# def chop_vegetables(time):
#     if 1100 < time < 2100:
#         print("Chopping the vegetables...")
#     else:
#         print("I'm off duty!")

# wash_dishes(1200)



def check_working_hours(func):
    def wrapper(time):
        if 1100 < time < 2100:
            func(time)
        else:
            print("I'm off duty!")
    return wrapper

@check_working_hours
def sweep_floors(time):
    print("Sweeping the floors...")

@check_working_hours
def wash_dishes(time):
    print("Washing the dishes...")

@check_working_hours
def chop_vegetables(time):
    print("Chopping the vegetables...")

sweep_floors(800)
wash_dishes(1000)
chop_vegetables(1400)


def chec_vowel(letter):
 
   if (letter == "a" or
      letter == "e" or
      letter == "i" or
      letter == "o" or
      letter == "u"):
    # Begin "if" block
    print("vowel.")
   else:
    # Begin "else" block
    print("not a vowel.")

chec_vowel("o")


name = "Steven"
print(f"Hi, {name}." if name == "Steven" else f"Goodbye, {name}.")

x = 0

while x < 1:
    print("so many loops")
    x+=1

# def use_truthiness(x):
#     return 7 > 8 or x
# use_truthiness()

def print_param(param):
    print(param)

string = print_param("hello")
# the code here runs 5 times
counter = 0
while counter < 5:
    print("Print HI")
    counter+=1
print("\n")
# the code here runs 4 times
counter = 0
while counter < 5:
    print("Print HI")
    counter+=1


count = 1
while count <= 50:
    print("Sana")
    count+=1

print("working on something else")

class Album:
    GENRES =["Hip-Hop", "Pop", "Jazz"]
    album_count = 0 

    def __init__(self, genre, date): 
        if self.check_genre(genre):
            self.increase_album_count()
            self.genre = genre
            self.release_date = date

    @classmethod
    def check_genre(cls, genre):
        return genre in cls.GENRES
    
    @classmethod
    def increase_album_count(cls, increment = 1):
        cls.album_count += increment


print(Album.album_count)

print("working on Songs Class")

class Song:
    all = [] #class attribute- a varriable that belongs to an object

    def __init__(self, name):
        self.name = name
        self.all.append(self)
#Adds a song to all[]
    @classmethod
    def add_song_to_all(cls, song):
        cls.all.append(song)
#This classmethod  show all the songs in all[]
    @classmethod
    def show_song_names(cls):
        print([Song.name for Song in cls.all]) 

ninety_nine_problems = Song("99 Problems")
thriller = Song("Thriller")

print(Song.show_song_names())