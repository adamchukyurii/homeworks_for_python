from game.settings import *
from game.exceptions import GameOver, EnemyLost
from random import randint

class Player:
   name: str
   lives: int
   score: int
   
   
   def __init__(self, name: str) -> None:
      self.name = name
      self.lives = PLAYER_LIVES
      self.score = 0
      
      
   def choice(self) -> str:
      while True:
         user_choice = input("\nChoose a Paper(1), Rock(2) or Scissors(3):\n\n")
            
         if user_choice == "1":
            return PAPER
         elif user_choice == "2":
            return ROCK
         elif user_choice == "3":
            return SCISSORS

   
   def decreas_lives(self) -> None:
      self.lives -= 1
      if self.lives == 0:
         raise GameOver("\n     You lost the game\n")
      
      
      
   def add_score(self, score: int) -> None:
      self.score += score
      
      
class Enemy: 
   lives: int 
   level: int
   
   def __init__(self, lives: int, level: int) -> None:
      self.lives = lives
      self.level = level
      
      
      
   def choice(self) -> str:
      enemy_choice = str(randint(1, 3))
      if enemy_choice == "1":
         return PAPER 
      elif enemy_choice == "2":
         return ROCK
      elif enemy_choice == "3":
         return SCISSORS
   
   
   def decreas_lives(self) -> None:  
      self.lives -= 1
      if self.lives == 0:
         raise EnemyLost("\n   Congratulations, you defeated enemy\n")