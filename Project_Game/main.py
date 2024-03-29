from game.game import Game
from game.models import Player
from game.settings import MODE_NORMAL, MODE_HARD, SCORE_FILE
from game.scores import ScoreHandler


def main():
   user_choice = input("\n✨Rock✊ Paper🫱  Scissors✌️ ✨\n\n\n          Play(1)⚔️\n\n      See Scoreboard(2)🏅\n\n          Exit(3)🫨\n\n")
   
   if user_choice == "1":
      play_game()
   elif user_choice == "2":
      show_scoreboard()
   elif user_choice == "3":
      exit()
   
def play_game():
   user_name = input("\n     ⬇️ Enter your name⬇️\n\n")
   player = create_player(user_name)
   
   while True:
      mode = input("\n     ⬇️ Choose a mode⬇️\n         Normal(1)😊\n            or\n          Hard(2)😈\n\n")
      if mode == "1":
         mode = MODE_NORMAL
         break
      elif mode == "2":
         mode = MODE_HARD
         continue
      else:
         print("\n       Invalid mode\n")
         continue
      
   game = Game(player, mode)
   game.play_game()
   
def create_player(name: str) -> Player:
   return Player(name)
   
      
def show_scoreboard():
   score_handler = ScoreHandler(SCORE_FILE)
   score_handler.display()
   
   
if __name__ == "__main__":
   main()
   
