from game.settings import *
from game.exceptions import GameOver, EnemyLost
from random import randint

class Player:
   name: str
   lives: int
   score: int = 0
   
   def __init__(self, name: str, lives: int, score: int) -> None:
      self.name = name
      self.lives = lives
      self.score = score
      
   def choice(self) -> str:
      while True:
         user_choice = input("\nChoose a Paper(1), Rock(2) or Scissors(3):\n")
            
         if user_choice == "1":
            return PAPER
         elif user_choice == "2":
            return ROCK
         elif user_choice == "3":
            return SCISSORS

   
   def decreas_lives(self) -> None:
      self.lives -= 1
      if self.lives == 0:
         raise GameOver()
      
   def add_score(self, score: int) -> None:
      self.score += score
      
   def __str__(self) -> str:
      return f"{self.name} has {self.lives} lives and {self.score} points"
      
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
         raise EnemyLost()
      
   def increase_level(self) -> None:
      self.level += 1