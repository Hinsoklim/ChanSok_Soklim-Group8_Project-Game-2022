# Creat function tkinter for game =====================================
from tkinter import *
import random
from typing import get_origin

# Create Canvas in frame =============================================
window = Tk()
canvas = Canvas(window)

# All Variable in the game ===============================================

SCREEN_HEIGHT = 650 # Variable height screen ============

SCREEN_WIDTH = 720  # Variable width screen =============

time_game = 0  # Variable time game ============

score_game = 0  # Vairable score's Player =========

num_0f_succeed_enermy = 0  # Variable enermy hero not kill =======

# num_of_bullets_of_hero = 5000     # Variable bullet of player hero ===========

hero_plane_X = 360   # Variable position hero X =======

hero_plane_Y = 555   # Variable position hero Y ========

list_of_enermy = []   # Variable list all enermy =========

store_bullets_hero = []
store_bullet_enermy = []

paused = False
 
#=================================== Window Scenario 1 =======================================================


# ================================== Window Scenario 2 =======================================================





# ================================================================================================================================================================
#=================================== Function Create ==================================================
# Function Create nermy fight with hero =============================
def create_enermy():
    enermy  = canvas.create_image(random.randrange(35,600),0,image = enermyimage)
    list_of_enermy.append(enermy)

# Function Create bullet hero plane for fight enermy  ===============================
def create_bullet_hero(event):
    # Condition check to create bullet for hero =====================
    if (num_0f_succeed_enermy < 15)  and (score_game < 60) :
        hero_bullet_position = canvas.coords(hero_plane)
        bullet_hero = canvas.create_image(hero_bullet_position[0] + 3,hero_bullet_position[1] - 60,image = gun_hero)
        store_bullets_hero.append(bullet_hero)


# Function Create bullet enermy for fight hero plane =================================

def create_bullet_enermy():
    if len(list_of_enermy) > 0:
        position_enermy_have_bullet = random.choice(list_of_enermy)
        position_bullet_enermy = canvas.coords(position_enermy_have_bullet)
        bullet_enermy = canvas.create_image(position_bullet_enermy[0],position_bullet_enermy[1] + 50,image = enermy_gun)
        store_bullet_enermy.append(bullet_enermy)



# =========================================================================================================================================================================================


# ==================================== Function move ===================================
# Function move enermy =========================
def move_enermy():
    global num_0f_succeed_enermy
    to_delete_enermy = []
    for index in range(len(list_of_enermy)):
        other_enemy = list_of_enermy[index]
        position = canvas.coords(other_enemy)
        if position[1] > SCREEN_HEIGHT:
            num_0f_succeed_enermy += 1
            canvas.delete(list_of_enermy[index])
            to_delete_enermy.append(index)
        canvas.move(other_enemy, 0, 5)
    for delete_index in to_delete_enermy:
        list_of_enermy.pop(delete_index)

# Function move hero's bullets to fight enermy ========================================================
def move_hero_bullet():
    to_delet_hero_bullet = []
    for bullet in store_bullets_hero:
        canvas.move(bullet,0,-30)
    for i in range(len(store_bullets_hero)):
        bullet_hero = store_bullets_hero[i]
        bullet_hero_position = canvas.coords(bullet_hero)
        if bullet_hero_position[1] < - SCREEN_HEIGHT :
            canvas.delete(bullet_hero)
            to_delet_hero_bullet.append(i)
    for j in to_delet_hero_bullet:
        store_bullets_hero.pop(j)
    
        

# Function move enermy's bullets to fight plane =========================================================
def move_enermy_bullet():
    to_delete_enermy_bullet = []
    for bullet in store_bullet_enermy:
        canvas.move(bullet, 0, 60)
    for i in range(len(store_bullet_enermy)):
        bullet_enermy = store_bullet_enermy[i]
        bullet_position = canvas.coords(bullet_enermy)
        if bullet_position[1] >= SCREEN_HEIGHT:
            canvas.delete(bullet_enermy)
            to_delete_enermy_bullet.append(i)
    for j in to_delete_enermy_bullet:
        store_bullet_enermy.pop(j)


# Function bullet hero meet enermy =========================================

def bullet_hero_meet_enermy():
    global score_game
    for hero_bullet in store_bullets_hero:
        position_hero_bullet = canvas.coords(hero_bullet)
        for enermy in list_of_enermy:
            position_enermy = canvas.coords(enermy)
            if (position_hero_bullet[1] <= position_enermy[1] - 55) and (((position_hero_bullet[0] >= position_enermy[0]) and (position_hero_bullet[0] <= position_enermy[0]- 50)) or ((position_hero_bullet[0] - 15 >= position_enermy[0]) and (position_hero_bullet[0] -15 <= position_enermy[0] - 50))):
                score_game += 1
                canvas.itemconfig(display_score,text = "Your score : " + str(score_game))

#  Function Move Left of the hero plane ==================================
def move_left(event):
    global hero_plane_X 
    if hero_plane_X > 5:
        hero_plane_X -= 5
    canvas.moveto(hero_plane,hero_plane_X,hero_plane_Y)

# Function Move right of the hero plane =================================
def move_right(event):
    global hero_plane_X
    if hero_plane_X < 620:
        hero_plane_X += 5
    canvas.moveto(hero_plane,hero_plane_X,hero_plane_Y)

# ======================= Enermy meet hero or bullet's enermy meet hero or bullet's hero meet enermy =========================================================
#  enermy meet with hero plane ====================================

def ennemy_meet_hero():
    global life_hero
    position_hero = canvas.coords(hero_plane)
    for enemy in list_of_enermy:
        position_enermy = canvas.coords(enemy)
        if (position_enermy[1]  >= position_hero[1] - 55) and (((position_enermy[0] >= position_hero[0] -55) and (position_enermy[0]  <= position_hero[0] + 90)) or ((position_enermy[0] + 90 >= position_hero[0] ) and (position_enermy[0] + 90 <= position_hero[0] + 90 ))):
            return enemy
    return None




# draw Plane hero and enermy in the game =============================================================
# backgroundimage = PhotoImage(file='image/background.png')
# canvas.create_image(0,0,image = backgroundimage)

heroimage = PhotoImage(file='image/hero.png')

gun_hero = PhotoImage(file='image/herobullet.gif')

hero_plane = canvas.create_image(hero_plane_X,hero_plane_Y, image = heroimage)

enermy_gun = PhotoImage(file='image/enermybullet.gif')

enermyimage = PhotoImage(file='image/enermy-small.png')

# Display all feature  ======================================================

display_score =canvas.create_text(45,15,text="Score : "+ str(score_game),font=("",15),fill="red")

# Function process game ============================================================
def process_game():

    global time_game

    time_game += 1
    endGame = False
    if not paused:
        move_hero_bullet() 
        if time_game % 5 == 0:
            move_enermy()
            move_enermy_bullet()
            t = ennemy_meet_hero()
            if t != None :
                endGame = True
                message = 'Emmemy killed hero'
        if score_game == 60:
            endGame = True
            message = 'Congratulation'
        # Create Enermy ============================
        if time_game % 160 == 1:
            create_enermy()
            create_bullet_enermy()
        elif num_0f_succeed_enermy == 15:
            endGame = True
            message  = 'Enemy passed 15 times.\n Scores: ' + str(score_game)
        if endGame== True:
            end_game(message)
        else:
            canvas.after(17, process_game)      

# Function paused game ========================================


# Process game when play the game  ===========================================
process_game()

#  Function End game when hero plane lost or win =========================

def end_game(message):
    canvas.create_text(360,330,text=message,font=("",30),fill='red')


# Create Window For Game =============================================

window.geometry(str(SCREEN_WIDTH) + 'x' + str(SCREEN_HEIGHT))

# Window Not resizable ===============

window.resizable(False,False)

# Create frame and Title frame =======================================

window.title("Project Game Web 2022")


# Draw the Canvas in the Window =======================================

canvas.pack(expand=True,fill='both')

# Function Arrow Key Move Hero ===================================================

window.bind_all('<Left>',move_left)

window.bind_all('<Right>', move_right)

window.bind_all('<f>',create_bullet_hero)

# Display window =====================================================

window.mainloop()