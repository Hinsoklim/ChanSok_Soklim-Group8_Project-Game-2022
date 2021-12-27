# Creat function tkinter for game =====================================
from tkinter import *
import random
import os


# Create Window For Game =============================================
window = Tk()
window.geometry('720x660')

# Create frame and Title frame =======================================
window.title("Project Game Web 2022")
window.resizable(False,False)
# Create Canvas in frame =============================================
canvas = Canvas(window)


# All constant ====================================================
SCREEEN_HEIGHT = 650

# All Variable ====================================================
time_game = 0 
score_game = 0
life_hero = 0
num_0f_succeed_enermy = 0
num_of_bullets = 1000
hero_plane_X = 313
hero_plane_Y = 515
list_of_enermy = []
 


# Window Scenario 2 =======================================================

    
#  Function End game when hero plane lost or win =========================
def end_game(message):
    canvas.create_text(360,100,text=message,font=("",25),fill='green')
        
 

#  enermy meet with hero plane ====================================

def get_ennemy_on_hero( ):
    position_hero = canvas.coords(hero_plane)

    for enemy in list_of_enermy:
        position_enermy = canvas.coords(enemy)

        if (position_enermy[1] >= position_hero[1]) and (((position_enermy[0] >= position_hero[0]) and (position_enermy[0] <= position_hero[0]+80)) or ((position_enermy[0]+55 >= position_hero[0]) and (position_enermy[0]+55 <= position_hero[0]+80))):
            return enemy

    return None

    


# Function move enermy ===================================
def move_enermy():
    global num_0f_succeed_enermy
    to_delete_enermy = []
    for index in range(len(list_of_enermy)):
        other_enemy = list_of_enermy[index]
        position = canvas.coords(other_enemy)
        if position[1] > SCREEEN_HEIGHT:
            num_0f_succeed_enermy += 1
            canvas.delete(list_of_enermy[index])
            to_delete_enermy.append(index)
        canvas.move(other_enemy, 0, 7)

    for i in to_delete_enermy:
        list_of_enermy.pop(i)

# Function Create Enermy ==================================================

def create_enermy():
    enermy  = canvas.create_image(random.randrange(10,540),-40,image = enermyimage)
    list_of_enermy.append(enermy)

# Function move the Plane​ hero ==================================================
def move_left(event):
    global hero_plane_X
    if hero_plane_X > 10:
        hero_plane_X -= 10
    canvas.moveto(hero_plane,hero_plane_X,hero_plane_Y)

def move_right(event):
    global hero_plane_X
    if hero_plane_X < 620:
        hero_plane_X += 10
    canvas.moveto(hero_plane,hero_plane_X,hero_plane_Y)



# draw Plane Player and enermy in the game =============================================================
heroimage = PhotoImage(file='image/hero.png')
gun_hero = PhotoImage(file='image/herobullet.gif')
hero_plane = canvas.create_image(hero_plane_X,hero_plane_Y, image = heroimage)

enermy_gun = PhotoImage(file='image/enermybullet.gif')
enermyimage = PhotoImage(file='image/enermy-small.png')

# Display all ======================================================

display_score = canvas.create_text(45,15,text="Score : "+ str(score_game),font=("",15),fill="red")
display_life = canvas.create_text(655,15,text="Your Life : " + str(life_hero),font=("",15),fill="red")

 
# Function process game ============================================================

def process_game():
    # global variable ==============================================
    global time_game

    # time game =========================================
    time_game += 1
    endGame = False


    if time_game % 6 == 0:
        move_enermy()

        ennemyOnHero = get_ennemy_on_hero()
        if ennemyOnHero != None:
            endGame = True
            message = 'Emmemy killed hero'
    
    if score_game == 60:
        endGame = True
        message = 'Congratulation'
     
    if num_of_bullets == -1:
        endGame = True
        message  = '\nYou have no bullets.\nScores: ' + str(score_game)
      
    elif life_hero == 6:
        endGame = True
        message  = '\nYou have no LIVE.\nScores: ' + str(score_game)
      
    elif (num_0f_succeed_enermy == 20):
        endGame = True
        message  = '\nEnemies passed 20 times.\nScores: ' + str(score_game)


    if endGame== True:
        end_game(message)
    else:
        canvas.after(15, process_game)        





 
#    test   only 1 enny and start process
create_enermy()

process_game()





# Draw the Canvas in the Window =======================================
canvas.pack(expand=True,fill='both')



# Function Arrow Key Move Hero ===================================================
window.bind_all('<Left>',move_left)
window.bind_all('<Right>', move_right)


# window.bind_all('<p>',paused_game)
# window.bind_all('<c>',un_paused_game)
# window.bind('<f>',create_bullet)



# Display window =====================================================
window.mainloop()