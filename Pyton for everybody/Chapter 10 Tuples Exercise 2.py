
file_name = input("Enter a file name: ")
line_list = [line.strip("\n") for line in open(file_name, 'r')
if line.startswith("From ")]

hour_histogram = {}
tuple_list = []

for line in line_list:
    time = line.split()[5]
    hour = time.split(":")[0]
    hour_histogram[hour] = hour_histogram.get(hour, 0) + 1

for key in hour_histogram:
    tuple_list.append((key, hour_histogram[key]))

sorted_tuple_list = sorted(tuple_list)

for item in sorted_tuple_list:
  print (item[0], item[1])
