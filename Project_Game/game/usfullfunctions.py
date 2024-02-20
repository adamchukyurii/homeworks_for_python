import os
from game.models import Player, Enemy
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def print_info(player: Player, enemy: Enemy, player_choice, enemy_choice) -> None:
   # clear_terminal()
   
   if player_choice == "Scissors":
      player_choice = "✌️"
   elif player_choice == "Paper":
      player_choice = "🫱"
   elif player_choice == "Rock":
      player_choice = "✊"
      
   if enemy_choice == "Scissors":
      enemy_choice = "✌️"
   elif enemy_choice == "Paper":
      enemy_choice = "🫱"
   elif enemy_choice == "Rock":
      enemy_choice = "✊"
      
   lives = "❤️ "
   player_lives = lives  * player.lives
   enemy_lives = lives * enemy.lives
   spaces = " " * 19
   space_lives = " " * (18 + (player.lives + enemy.lives))
   space_choice = " " * 24
   print(f"{player.name}{spaces}Enemy\n{player_lives}{space_lives}{enemy_lives}\n\n{player_choice}{space_choice}{enemy_choice}\n")