from pokemon import Pokemon
from dragon_pokemon import DragonType
from water_pokemon import WaterType  # WaterType class by Weihua Jiang
import random

class PokeGame:
    def __init__(self):
        self.game_master = []
        self.setup()

    def setup(self):
        """Creates a list of Pokemon instances to represent opps cards"""
        self.game_master.append(Pokemon("Pikachu", "Ash"))
        self.game_master.append(DragonType("Garchomp",
                                           "Cynthia", 108))
        self.game_master.append(DragonType("Dragonite",
                                           "Lance", 91))
        self.game_master.append(WaterType("Milotic",
                                          "Wallace", 95))
        self.game_master.append(WaterType("Greninja",
                                          "Ash", 72))
        self.game_master.append(Pokemon("Charizard", "Leon"))
        self.game_master.append(DragonType("Hydreigon",
                                           "Ghetsis", 92))

    def drawPokemon(self):
        """Pulls an instance from the list of Pokemon"""
        if self.game_master:
            opp_card = random.choice(self.game_master)
            self.game_master.remove(opp_card)
            print("Opponent's Pokemon card:", opp_card.name)
            return opp_card
        else:
            # No more instances in the list
            print("Game Over.")

# Client method to test program
def main():
    game = PokeGame()
    game.setup()
    opponent = game.drawPokemon()

    if opponent:
        print("\nChoose your Pokemon Type:")
        print("1. DragonType")
        print("2. WaterType")
        print("3. Basic Pokemon")
        choice = input("Enter choice (1, 2, 3): ")
        name = input("Enter your Pokemon's name: ")
        hp = int(input("Enter your Pokemon's HP: "))

        if choice == '1':
            player = DragonType(name, "Player", hp)
        elif choice == '2':
            player = WaterType(name, "Player", hp)
        elif choice == '3':
            player = Pokemon(name, "Player")
        else:
            print("Invalid choice. Using basic Pokemon.")
            player = Pokemon(name, "Player")

        print("\nPokemon Battle begins!")
        player.attack(opponent)

if __name__ == "__main__":
    main()
