### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

# Note that we are only looking for errors here.

# **Not** any issues with, i.e.: 
# Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

# These aren't errors but rather standards that vary from developer to developer. 

# Only comment on errors that would stop the tests running.

# ```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:
          # "=" is assignment not comparison "==" required
      return True
    else
    # missing colon
      return False
   

  dif highest_card(self, card1 card2):
  # typo dif, should be def
  # missing "," in argument list
  if card1.value > card2.value:
    return card
    # card not declared here should pressumably be card1
  else:
    return card2

#  if/else block missing indentation
  


def cards_total(self, cards):
#indentation
  total
  #total not declared correctly
  for card in cards:
    total += card.value
    return "You have a total of" + total
    #return inside for block will return after first iteration. Cant concatenate a str and int, also probably want a whitespace between of and "
  
```
