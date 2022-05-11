num = input()
num = int(num)
s = input()
start = len(s) - num 
s = s[start:len(s)]
numa = 0
numb = 0
numc = 0
x = 0 

while True:
  x += 1
  for i in s:
    if i == 'a':
      numa += 1
    if i == 'b':
      numb += 1
    if i == 'c':
      numc += 1
  if(numa >= 3 and numb >=2 and numc >= 1):
  
    print(x)
    break
  else:
    s = s+s
 
