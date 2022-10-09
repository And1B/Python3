from collections import UserString

str_name = 'python powered patterned products'
str_word = 'patterned '


class SubtractString(UserString):
  def __sub__(self, other):
    if other in self.data:
      self.data = self.data.replace(other, "")
subtract_string  = SubtractString(str_name)

print(subtract_string  - str_word)
