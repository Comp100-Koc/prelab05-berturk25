def remove_adjacent_duplicates(s):
  my_str = ""
  
  for cha in s:
      my_str += cha
      
      if len(my_str) >= 2 and my_str[-1] == my_str[-2]:
          my_str = my_str[:-2]
    
  return my_str