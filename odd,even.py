n = int(input())
if n%2!= 0:
  print("weird")
elif n in range (2,6):
  print("not weird")
elif n in range(6,21):
  print("weird")
else:
  print("not weird")  