import json
from translate import Translator

translator = Translator(to_lang="de")

#Read JSON file
with open("labels_coco.json", "r") as file:
    data = json.load(file)

for key in data: 
    data[key] = translator.translate(data[key])


# Save JSON file

with open("translated.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON file updated successfully!")