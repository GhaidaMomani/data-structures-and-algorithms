
list = [1, 2 ,3, 4, 5]  

def reverse_lst(arr):
  new_list = []
  for i in range(1, len(list)+1):
    new_list.append(list[-i])
    
  print(new_list)

reverse_lst(list)