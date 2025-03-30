x=7
counter = 1
found=False
while not found:
     found = x % 2003 == 0
     if not found:
          x = (x * 10) + 7
          counter +=1
print("%d" % counter)