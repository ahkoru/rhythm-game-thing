from tkinter import filedialog
import os
# import json
# import map_parser

filename = filedialog.askopenfilename()
# beatmap = map_parser.read_osu_map(filename, True)

# with open('output.json', 'w', encoding='utf-8') as f:
#     json.dump(beatmap, f)

# with open('output.json', 'r', encoding='utf-8') as file:
#     beatmap = json.load(file)
    
# print(isinstance(beatmap, dict))

# a = []
# for num in range(1,11):
#     a.append(num*100 + 225)
    
# print(a[::-1])

# beatmap_name = os.path.relpath(filedialog.askopenfilename())
# beatmap_directory = beatmap_name.rsplit('/')[1]
# print(beatmap_directory, beatmap_name)
os.makedirs('maps/amongus', exist_ok=True)
