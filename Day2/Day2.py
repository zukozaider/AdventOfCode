# Part 1
input_data = open('input.txt')
input_list = []
for item in input_data.read().split("\n"):
    input_list.append((item.split(' ')[0].split('-')[0], item.split(' ')[0].split('-')[1], item.split(' ')[1].replace(':', ''), item.split(' ')[2]))

valid_password = []
for item in input_list:
    min = int(item[0])
    max = int(item[1])
    char = str(item[2])
    password = str(item[3])

    if password.count(char) >= min and password.count(char) <= max:
        valid_password.append(password)

len(valid_password)


# Part 2

input_list = []
for item in input_data.read().split("\n"):
    input_list.append((item.split(' ')[0].split('-')[0], item.split(' ')[0].split('-')[1], item.split(' ')[1].replace(':', ''), item.split(' ')[2]))

valid_password = []

for item in input_list:
    pos_1 = int(item[0])
    pos_2 = int(item[1])
    char = str(item[2])
    password = str(item[3])
    if password[pos_1-1] == char and password[pos_2-1] != char:
        valid_password.append(password)
    
    elif password[pos_1-1] != char and password[pos_2-1] == char:
        valid_password.append(password)

len(valid_password)
