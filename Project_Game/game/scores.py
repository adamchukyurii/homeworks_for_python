from game.settings import MAX_RECORDS_NUMBER

class PlayerRecord:
   name: str
   mode: int
   score: int
   
   def __init__(self, name: str, mode: int, score: int) -> None:
      self.name = name
      self.mode = mode
      self.score = score
      
   def __str__(self) -> str:
      return f"|{self.name}|{self.mode}|{self.score}|"
   def __gt__(self, other) -> bool:
      return self.score > other.score
   
   def __eq__(self, other) -> bool:
      return self.name == other.name and self.mode == other.mode

class GameRecord:
   records: list[PlayerRecord]
   
   def __init__(self) -> None:
      self.records = []
   
   def add_record(self, record: PlayerRecord) -> None:
      if record in self.records:
         self.records[self.records.index(record)] = record
      else:
         self.records.append(record)
   def prepare_record(self) -> None:
      self.records.sort(reverse=True)
      self.records = self.records[:MAX_RECORDS_NUMBER]

class ScoreHandler:
   game_record: GameRecord
   file_name: str
   
   def __init__(self, file_name: str) -> None:
      self.file_name = file_name
      self.game_record = GameRecord()
   def read(self) -> None:
      with open(self.file_name, "r") as file:
         for line in file:
            components = line.strip().split("|")
            components = [component for component in components if component] 
            name, mode, score = components
            record = PlayerRecord(name, mode, int(score))
            self.game_record.add_record(record)
      
   def save(self, game_record_player) -> None:
      game_record_player.prepare_record()
      with open(self.file_name, "a") as file:
         for record in game_record_player.records:
            file.write(str(record) + "\n")
            
   def display(self) -> None:
      for record in self.game_record.records:
         print(record)
