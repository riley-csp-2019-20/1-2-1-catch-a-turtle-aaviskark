# a121_catch_a_turtle.py

#-----import statements-----
import turtle as trtl 
import random 

#-----game configuration----
shape = "turtle"
color= ["darkorange", "white","green", "red", "blue", "yellow", "black", "brown", "purple", "indigo", "pink", "silver"]
    #list of the random color choices
size= 4
score=0

font_setup = ("Arial", 20, "normal")
timer = 10
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
turt = trtl.Turtle(shape = shape)
turt.color(random.choice(color))
turt.shapesize(size)
turt.speed(8)

scoretrl= trtl.Turtle()
scoretrl.ht()
scoretrl.up()
scoretrl.goto(-370,270)
font= ("Arial", 30, "bold")
scoretrl.pencolor("white")
scoretrl.write(score, font= font)

counter =  trtl.Turtle()
counter.pencolor("white")
counter.speed(0)
counter.up()
counter.goto(350,300)
counter.ht()
#-----game functions--------
def turtle_click(x,y):
    print("bruh")
    change_position()
    add_score()
    scoretrl.clear()
    scoretrl.write(score, font= font)
    change_color()
    
def change_position():
    turt.up()
    turt.ht()
    new_xpos= random.randint(-400,400)
    new_ypos= random.randint(-300,300)
    turt.goto(new_xpos, new_ypos)
    turt.st()

def add_score():
    global score
    score+=1
    print(score)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    game_end()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def change_color():               #function for the random color change
  turt.color(random.choice(color))

def game_end():
    turt.ht()
    wn.bgcolor("gray")
    turt.goto(-1000,1000)
    counter.goto(0,0)

    
#-----events----------------
turt.onclick(turtle_click)
wn= trtl.Screen() 
wn.ontimer(countdown, counter_interval) 
wn.bgcolor("black") #changes bg color
wn.mainloop()