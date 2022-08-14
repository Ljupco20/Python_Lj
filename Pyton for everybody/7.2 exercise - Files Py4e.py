#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form: 
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines 
#and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution. 

count = 0
tot = 0
avg = 0

fname = input('Enter file name: ')
fhand = open(fname)

for line in fhand:
  if not line.startswith('X-DSPAM-Confidence:'): continue
  count = count + 1
  num = line.find(':')+1
  n = float(line[num:])  
  tot = tot + n
avg = tot/count

print("Average spam confidence: ",avg)
