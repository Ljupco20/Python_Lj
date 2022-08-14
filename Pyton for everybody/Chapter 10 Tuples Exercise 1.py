
fname = input("Enter a file name: ")
line_list = [line.strip("\n") for line in open(fname, 'r')
             if line.startswith("From ")]
email_dict = {}

for line in line_list:
    email = line.split()[1]
    email_dict[email] = email_dict.get(email, 0) + 1

tulple_list = []
for email in email_dict:
    tulple_list.append((email_dict[email], email))

winner = sorted(tulple_list, reverse=True)[0]
print (winner[1], winner[0])