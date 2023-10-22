#create a base class Player
class Player:
	#Include an __init__ method that initializes the player with a name, health, and energy, and also allows for custom values.
	def __init__(self, name, health=100, energy=100):
			self.name = name 
			self.health = health
			self.energy = energy 



#Create two subclasses, Wizard and Archer:

#Inherit from the Player class.
#Implement specific attack and defend methods for each subclass.
	
#Inherit the Player class: class Wizard(Player):
class Wizard(Player):	
	#Define the attack method for the Wizard class, implementing the attack logic for the wizard's moves.
	def attack(self, other_player):
		print(f'{self.name} is attacking {other_player.name}')
		self.energy -= 30 
		other_player.health -= 20 
	#Define the defend method for the Wizard class, implementing the defend logic for the wizard's defensive moves.
	def defend(self, other_player):
		print(f'{self.name} is defending from {other_player.name}')
		self.energy += 25 
		self.health -= 5 


#Inherit the Player class: class Archer(Player):
class Archer(Player):
	#Define the attack method for the Archer class, implementing the attack logic for the archer's moves.
	def attack(self, other_player):
			print(f'{self.name} is attacking {other_player.name}')
			self.energy -= 30 
			other_player.health -= 20 

	#Define the defend method for the Archer class, implementing the defend logic for the archer's defensive moves.
	def defend(self, other_player):
			print(f'{self.name} is defending from {other_player.name}')
			self.energy += 25 
			self.health -= 5 


#Write a function combat_game
def combat():
	# Take input for player names and types (Wizard or Archer).
	p1_name = input("Please enter Player1 Name: ")
	p2_name = input("Please enter Player2 Name: ")

	p1_type = input("Please enter Player1 Type: ")
	p2_type = input("Please enter Player2 Type: ")

	# Instantiate the corresponding Wizard or Archer objects based on user input.
	if p1_type.lower() == "wizard":
		player1 = Wizard(p1_name)

	else:
		player1 = Archer(p1_name)

	if p2_type.lower() == "wizard":
		player2 = Wizard(p2_name)

	else:
		player2 = Archer(p2_name)

	# Set up a while loop that runs as long as both players have health remaining.
	while player1.health > 0 and player2.health > 0:
	# Display player stats (health and energy) at the beginning of each iteration.
		print(f"{player1.name} Health: {player1.health}, Energy: {player1.energy}")
		print(f"{player2.name} Health: {player2.health}, Energy: {player2.energy}")

	# Prompt each player for their move (attack or defend) and adjust health and energy accordingly based on the selected actions.
		player1_turn = input(f'{player1.name} Do you want to attack or defend? ')
		player2_turn = input(f'{player2.name}Do you want to attack or defend? ')

		if player1_turn.lower() == "attack":
					player1.attack(player2)
		else:
			player1.defend(player2)

		if player2_turn.lower() == "attack":
			player2.attack(player1)
		else:
			player2.defend(player1)

	# Print the winner's name based on the player with non-zero health after the loop ends
	if player1.health <=0:
		print(f"{player2.name} wins")
	else:
		print(f"{player1.name} wins")


#run the function
combat()

