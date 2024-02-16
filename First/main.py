class Figure:
   color = 'white'
   place = ''
   name = ''
   cordinates = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], ['1', '2', '3', '4', '5', '6', '7', '8']]
   
   def set_place(self, place: str = 'A1') -> None:
      if self.color == 'white':
         self.place = place
      elif self.color == 'black':
         self.place = place
   
   def chage_color(self) -> None:
      if self.color == 'white':
         self.color = 'black'
      if self.color == 'black':
         self.color = 'white'
         
      
   def chage_place(self, new_place: str) -> None:
     
      if (self.check_moves(new_place)):  
         self.place = new_place
         print("Succses")
      else:
         print("Out of boundaries")
      
   def check_moves(self, new_place: str) -> bool:
      raise NotImplementedError
      
class Pawn(Figure):
   def check_moves(self, new_place: str) -> bool:
      position_in_vertical = self.cordinates[1].index(self.place[1])
      position_in_horizontal = self.cordinates[0].index(self.place[0])
      boundaries = len(self.cordinates[1] ) - position_in_vertical
      possible_moves = []
      for i in range(1, boundaries):
         if len(possible_moves) == 2:
            break
         else:
            possible_moves.append(self.cordinates[0][position_in_horizontal] + self.cordinates[1][position_in_vertical + i])
      print(possible_moves)
      
      if new_place not in possible_moves:
         return False
      
      return True
   
   
class Knigth(Figure):
   def check_moves(self, new_place: str) -> bool:
      
      position_in_vertical = self.cordinates[1].index(self.place[1])
      position_in_horizontal = self.cordinates[0].index(self.place[0])
      boundaries_horizontal = len(self.cordinates[0])
      boundaries_vertical = len(self.cordinates[1])

      possible_moves = []

      for i in range(-2, 3):
         for j in range(-2, 3):
            if abs(i) + abs(j) == 3: 
               new_horizontal = position_in_horizontal + i
               new_vertical = position_in_vertical + j

               if 0 <= new_horizontal < boundaries_horizontal and 0 <= new_vertical < boundaries_vertical:
                  possible_moves.append(self.cordinates[0][new_horizontal] + self.cordinates[1][new_vertical])

      print(possible_moves)
      if new_place not in possible_moves:
         return False
      return True
   
class Bishop(Figure):
   def check_moves(self, new_place: str) -> bool:
      position_in_vertical = self.cordinates[1].index(self.place[1])
      position_in_horizontal = self.cordinates[0].index(self.place[0])
      boundaries_vertical = len(self.cordinates[1])
      boundaries_horizontal = len(self.cordinates[0])
      
      possible_moves = []
      
      direcitons = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
      
      for dx, dy in direcitons:
         x, y = position_in_horizontal, position_in_vertical
         while True:
            x += dx
            y += dy
            if 0 <= x < boundaries_horizontal and 0 <= y < boundaries_vertical:
               possible_moves.append(self.cordinates[0][x] + self.cordinates[1][y])
            else:
               break
      
      print(possible_moves)
      
      if new_place not in possible_moves:
         return False
      return True
            
class Rook(Figure):
   def check_moves(self, new_place: str) -> bool:
      position_in_vertical = self.cordinates[1].index(self.place[1])
      position_in_horizontal = self.cordinates[0].index(self.place[0])
      boundaries_vertical = len(self.cordinates[1])
      boundaries_horizontal = len(self.cordinates[0])
      
      possible_moves = []
      
      direcitons = [(-1, 0), (1, 0), (0, -1), (0, 1)]
      
      for dx, dy in direcitons:
         x, y = position_in_horizontal, position_in_vertical
         while True:
            x += dx
            y += dy
            if 0 <= x < boundaries_horizontal and 0 <= y < boundaries_vertical:
               possible_moves.append(self.cordinates[0][x] + self.cordinates[1][y])
            else:
               break
      
      print(possible_moves)

      if new_place not in possible_moves:
         return False
      return True
   
class King(Figure):
   def check_moves(self, new_place: str) -> bool:
      position_in_vertical = self.cordinates[1].index(self.place[1])
      position_in_horizontal = self.cordinates[0].index(self.place[0])
      boundaries_vertical = len(self.cordinates[1])
      boundaries_horizontal = len(self.cordinates[0])
      
      possible_moves = []
      
      direcitons = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
      
      for dx, dy in direcitons:
         new_horizontal = position_in_horizontal + dx
         new_vertical = position_in_vertical + dy
         if 0 <= new_horizontal < boundaries_horizontal and 0 <= new_vertical < boundaries_vertical:
            possible_moves.append(self.cordinates[0][new_horizontal] + self.cordinates[1][new_vertical])
      
      print(possible_moves)
   
      if new_place not in possible_moves:
         return False
      return True
   
class Queen(Figure):
   def check_moves(self, new_place: str) -> bool:
      position_in_vertical = self.cordinates[1].index(self.place[1])
      position_in_horizontal = self.cordinates[0].index(self.place[0])
      boundaries_vertical = len(self.cordinates[1])
      boundaries_horizontal = len(self.cordinates[0])
      
      possible_moves = []
      
      direcitons = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
      
      for dx, dy in direcitons:
         x, y = position_in_horizontal, position_in_vertical
         while True:
            x += dx
            y += dy
            if 0 <= x < boundaries_horizontal and 0 <= y < boundaries_vertical:
               possible_moves.append(self.cordinates[0][x] + self.cordinates[1][y])
            else:
               break
      
      print(possible_moves)
   
      if new_place not in possible_moves:
         return False
      return True
      
      
dicts = [
    {"name": "Mary", "age": 30, "city": "New York"},
    {"name": "Mary", "age": 30, "city": "Prague"},
    {"name": "Vlad", "age": 30, "city": "Prague"},
    {"name": "Vlad", "age": 20, "city": "London"},
    {"name": "Kate", "age": 20, "city": "London"},
    {"name": "Kate", "age": 20, "city": "New York"}
]

names = ["name", "age"]


def remove_duplicates(list_of_dicts: list[dict], list_of_names: list[str]) -> list[dict]: 
   new_list_of_dicts = []
   unique_values = set()
   for person in list_of_dicts:
      values = tuple(person[name] for name in list_of_names)
      if values not in unique_values:
         unique_values.add(values)
         new_list_of_dicts.append(person)
   return new_list_of_dicts

print(remove_duplicates(dicts, names))