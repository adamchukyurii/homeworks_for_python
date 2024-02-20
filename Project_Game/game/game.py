from game.models import Player, Enemy
from game.exceptions import GameOver, EnemyLost
from game.settings import ATTACK_PAIRS_OUTCOME, MODES, HARD_MODE_MULTIPLIER, WIN, DRAW, LOSE, POINTS_FOR_FIGHT, POINTS_FOR_KILLING
from game.usfullfunctions import print_info



class Game:
   player: Player
   enemy: Enemy
   mode: str
   def __init__(self, player: Player, mode: str) -> None:
      self.player = player
      self.mode = mode   
      self.enemy = self.create_enemy(1)     
   def create_enemy(self, level) -> Enemy:
      if self.mode == MODES['2']:
         enemy = Enemy(level * HARD_MODE_MULTIPLIER, level)
      elif self.mode == MODES['1']:
         enemy = Enemy(level, level)
      return enemy
   
   def play_game(self) -> None:
      while True:
         self.handle_fight_result(self.fight())
         print_info(self.player, self.enemy, self.player.choice(), self.enemy.choice())
            
   def handle_fight_result(self, result: int): 
      try:  
         if result == WIN:
            self.enemy.decreas_lives()
            self.player.add_score(POINTS_FOR_KILLING)
            return
         elif result == LOSE:
            self.player.decreas_lives()
            print("You have lost one live, be carefull!")
            return
         else:
            self.player.add_score(POINTS_FOR_FIGHT)
      except GameOver:
         print("\n          You lost the game\n")
         # save scores 
         exit()
      except EnemyLost:
         print("\n       Congratulations, you won the game\n")
         self.play_again()
         self.enemy.increase_level()
         
   def play_again(self) -> None:
      user_choice = input("\nWould you like to play again? (y/n)\n")
      if user_choice.lower() == "y":
         self.play_game()
      else:
         # save scores 
         exit()
            
   def fight(self) -> None:
      player_choice = self.player.choice()
      enemy_choice = self.enemy.choice()
      if ATTACK_PAIRS_OUTCOME[(player_choice, enemy_choice)] ==  WIN:
         print((player_choice, enemy_choice), WIN)
         return WIN
      elif ATTACK_PAIRS_OUTCOME[(player_choice, enemy_choice)] == LOSE:
         print((player_choice, enemy_choice), LOSE)
         return LOSE
      else:
         print((player_choice, enemy_choice), DRAW)
         return DRAW
      
      
      
