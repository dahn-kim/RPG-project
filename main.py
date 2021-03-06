from game import Person
from magic import Magic

print("This is the instruction..............")


#Magic
fire = Magic("Fire", 10, 30, "dark")
wind = Magic("Wind", 15, 50, "dark")
ice = Magic("Ice", 20, 70, "dark")

magic_list = [fire, wind, ice]

player = Person("Daniel", 500, 100, 50, magic_list)
enemy = Person("Vamptire", 1000, 100, 20,magic_list)


player.stats()
enemy.stats()
print("--------------------------------------")
running = True
while running:
    #PLAYER'S TURN
    print(player.name)
    print("Choose your action: ")
    player.choose_action()
    try:
        choice = int(input(">>>: ")) #convert input to integer as input will automatically becomes string
    except ValueError:
        print("Choose a number!")
        continue
    action_index = choice - 1 #as the index begins with 0 in programming language.
    if action_index == 0:
        damage = player.generate_dmg()
        enemy.take_dmg(damage)

        print(" You attacked {} and dealt {} damage" .format(enemy.name, damage))

    if action_index == 1:
        player.choose_magic()
        magic_choice = int(input(">>>: ")) #convert input to integer as input will automatically becomes string

    else:
        print(" Choose a correct number")
        continue #contitnues the beginnign of the loop

    #ENEMY'S TURN
    enemy_choice = 0
    if enemy_choice == 0:
        enemy_damange = enemy.generate_dmg()
        player.take_dmg(enemy_damange)

        print("{} attacked {} and dealt {} damage" .format(enemy.name, player.name, enemy_damange))

    player.stats()
    enemy.stats()

    if player.hp == 0:
        print("You lost")
        running = False
    if enemy.hp == 0:
        print("You won")
        running = False
