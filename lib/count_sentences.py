#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    self._value = value
  
  def get_value(self):
    return self._value

  def set_value(self, value):
    if type(value) is str:
      self._value = value
    else:
      print("The value must be a string.")
  
  value = property(get_value, set_value)
  
  def is_sentence(self):
    return self._value.endswith(".")
  
  def is_question(self):
    return self._value.endswith("?")

  def is_exclamation(self):
    return self._value.endswith("!")
  
  def count_sentences(self):
    delimiters = [".", "?", "!"]
    count = 0
    for delimiter in delimiters:
      count += self.value.count(delimiter + ' ')
      count += self.value.endswith(delimiter)
    return count