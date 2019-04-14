# RPG game project

- 1v1, Good guy vs Bad guy
- Create a class Person with attributes:
  * name - string
  * hp - int
  * max_hp - int( = hp)
  * mp - int
  * max_mp - int (= mp)
  * atk_high = atk + 10
  * atk_low = atk - 10
  * action - list of string: at this level, only ["Attack"]
- class Person has method:
  * get_stat() to print out name, HP/MaxHP, MP/MaxMP
  * generate_dmg() return a attack damage value, randomly between atk_high and atk_low
  * take_dmg() take into a damage value and calculate the HP loss and return new HP points
  * choose_action() print out all the action options in the action list, at this stage is to print out from ["Attack"]
- Game Play:
  * import class Person
  * instantiate(create) new instance of Person, one is player, one is enemy
  * The game starts with a instruction printed out, says "This game is ....."
  * After that is the stats of the player and enemy
  * Player plays first, start choosing action
  * At this point, only attack, after choose attack, call generate_dmg() method from player
  * Call take_dmg() from enenmy
  * Print out the result of this turn, how many damages has been caused by player to enemy
  * Enemy's turn
  * Call generate damage from enemy
  * Call take_dmg() from player
  * Print out the result of this turn, how many damages has been caused by enemy to player
  * Print out the new stats of player and enemy
  * Check hp of player and enemy, whose hp == 0, lost
  *  If hp != 0, start the loop again
