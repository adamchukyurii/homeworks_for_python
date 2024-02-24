from game.models import Player, Enemy
from game.exceptions import GameOver, EnemyLost
from game.settings import ATTACK_PAIRS_OUTCOME, MODES, HARD_MODE_MULTIPLIER, WIN, DRAW, LOSE, POINTS_FOR_FIGHT, POINTS_FOR_KILLING, SCORE_FILE
from game.usfullfunctions import print_info
from game.scores import ScoreHandler, PlayerRecord, GameRecord

class Game:
   player: Player
   enemy: Enemy
   mode: str
   
   
   def __init__(self, player: Player, mode: str) -> None:
      self.player = player
      self.mode = mode   
      self.create_enemy(1) 
      
          
   def create_enemy(self, level) -> Enemy:
      if self.mode == MODES['2']:
         self.enemy = Enemy(level * HARD_MODE_MULTIPLIER, level)
      elif self.mode == MODES['1']:
         self.enemy = Enemy(level, level)
   
   
   def play_game(self) -> None:
      while True:
         self.handle_fight_result(self.fight())
            
            
   def handle_fight_result(self, result: int) -> None: 
      try:  
         if result == WIN:
            self.enemy.decreas_lives()
            self.player.add_score(POINTS_FOR_KILLING * HARD_MODE_MULTIPLIER)
            return
         elif result == LOSE:
            self.player.decreas_lives()
            print("\n   You have lost one live, be carefull!\n")
            return
         else:
            self.player.add_score(POINTS_FOR_FIGHT * HARD_MODE_MULTIPLIER)
      except GameOver:
         self.save_score()
         exit()
      except EnemyLost:
         self.create_enemy(self.enemy.level + 1)
         
         
   def save_score(self) -> None:
      player_record = PlayerRecord(self.player.name, self.mode, self.player.score)
      
      game_record = GameRecord()
      game_record.add_record(player_record)
      
      score_handler = ScoreHandler(SCORE_FILE)
      score_handler.save(game_record)

            
   def fight(self) -> None:
      player_choice = self.player.choice()
      enemy_choice = self.enemy.choice()
      fight_outcome = ATTACK_PAIRS_OUTCOME[(player_choice, enemy_choice)]
      
      if fight_outcome ==  WIN:
         print(f"\n   {self.player.name} won the fight\n")
         return WIN
      elif fight_outcome == LOSE:
         print(f"\n   {self.player.name} lost the fight\n")
         return LOSE
      else:
         print(f"\n   {self.player.name} drawn the fight\n")
         return DRAW
      
      
      
