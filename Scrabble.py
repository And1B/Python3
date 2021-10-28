letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_points = {letters:points for letters, points in zip(letters, points)}

letters_to_points[""] = 0

def score_word(word):
  point_total = 0
  for letters in word.upper():
      point_total += letters_to_points.get(letters, 0)
  return point_total
brownie_points = score_word("Brownie")
print(brownie_points)
player_to_words = {
  "player1": ["BLUE", "TENNIS", "EXIT"],
  "wordNerd": ["EARTH", "EYES", "MACHINE"],
  "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
  "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}
player_to_points = {}
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

def play_word(player, word):
  empty_list = []
  if player in player_to_words.keys():
    empty_list = (player_to_words.get(player))
    empty_list.append(word.upper())
    player_to_words.update({player: empty_list})
  else:
    player_to_words.update({player: word})

play_word("player2", "Hello")
print(player_to_words)
