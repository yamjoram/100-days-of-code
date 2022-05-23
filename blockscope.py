#block scope
#we are in the game level 3

game_level = 3

#and we got enemies
def create_enemy():
    enemies = ["skeleton", "zombie", "alien"]

    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)
create_enemy()