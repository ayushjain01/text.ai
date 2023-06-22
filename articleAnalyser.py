import News_Analyser
import os
import json

def save_json(filename, json_list):
    with open(f"./{filename}.json", "w") as outfile:
        for json_object in json_list:
            outfile.write(json_object)


dir_path = r'.\Data\news'
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
    meta = content[0]
    content = content[1:]
    meta = meta.split(", ")
    content = " ".join(content)
    print(content)
    article_dictionary = {}
    article_dictionary["source"] = meta[0]
    article_dictionary["date"] = meta[1]
    article_dictionary["journalist"] = meta[2]
    article_dictionary["path"]= filepath[0]
    article_dictionary["points"] = News_Analyser.generate_points(content)
    json_object = json.dumps(article_dictionary, indent=4)
    all_papers.append(json_object)
    file.close()
save_json("news",all_papers)