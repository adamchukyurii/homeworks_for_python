from game.game import Game
from game.models import Player, Enemy
from game.settings import PLAYER_LIVES
from game.usfullfunctions import clear_terminal, print_info



def main():
   user_choice = input("\n✨Rock✊ Paper🫱  Scissors✌️ ✨\n\n\n          Play⚔️\n\n      See Scoreboard🏅\n\n          Exit🫨\n\n")
   if user_choice.lower() == "play":
      play_game()
   elif user_choice.lower() == "see scoreboard":
      show_scoreboard()
   elif user_choice.lower() == "exit":
      exit()
   
def play_game():
   user_name = input("\n     ⬇️ Enter your name⬇️\n")
   name, mode = create_player(user_name)
   game = Game(name, mode)
   game.play_game()
   
def create_player(name: str) -> None:
   mode = input("\n     ⬇️ Choose a mode⬇️\n         Normal(1)😊\n            or\n          Hard(2)😈\n")
   player = Player(name, PLAYER_LIVES, 0)
   return player, "Normal" if mode == "1" else "Hard"
   
      
def show_scoreboard():
   
   pass
if __name__ == "__main__":
   main()
   
