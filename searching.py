def search(list,n):
    i = 0
    while i<len(list):
        if list == n:
          return True
          i = i+1
          return False
    
list = [5,8,7,6,9,2]
n = 9

if search(list,n):
  print("Found")
else:
    print("Not Found")