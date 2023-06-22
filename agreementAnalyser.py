import legal
import os

dir_path = r'.\agreements'
count = 0
files = []
for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        files.append(os.path.join(dir_path, path))

for filepath in files:
    file = open(filepath, 'r')
    content = file.readlines()
    clauses = {}
    clause = " "
    clausecontent = ""
    for i in content:
        if i[0].isdigit():
            if i[0] == clause[0]:
                clausecontent = clausecontent + i.lstrip("1234567890. ")
            else:
                clauses[clause] = clausecontent
                clause = i
                clausecontent = ""
    content = " ".join(clauses.values())
    print(legal.generate_points(content))
    #print(points)