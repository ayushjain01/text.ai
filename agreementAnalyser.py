import Legal_Analyser
import os
import json

def save_json(filename, json_list):
    with open(f"./{filename}.json", "w") as outfile:
        for json_object in json_list:
            outfile.write(json_object)


dir_path = r'.\Data\agreements'
count = 0
files = []
for path in os.listdir(dir_path):
    if os.path.isfile(os.path.join(dir_path, path)):
        files.append((os.path.join(dir_path, path),path))
all_papers =[]
for filepath in files:
    print(filepath)
    file = open(filepath[0], 'r')
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
    legal_dictionary = {}
    legal_dictionary["path"]= filepath[0]
    legal_dictionary["name"]= filepath[1].rstrip(".txt")
    legal_dictionary["points"] = Legal_Analyser.generate_points(content)
    json_object = json.dumps(legal_dictionary, indent=4)
    all_papers.append(json_object)
    file.close()
save_json("agreements",all_papers)