import json

songs_list = {}
for i in range(0, 104):
    with open("json_files/page_" + str(i) + ".json") as f:
        data = json.load(f)
    for j in data:
        song_id = j["songName"]
        level_id= j["id"]
        level_name = j["name"]
        if song_id == "Clubstep":
            song_id = "{dj-N} Club Step"
        if song_id == "Time Machine":
            song_id = "-Time Machine-"
        if song_id == "Electroman Adventures":
            song_id = "-Electroman adventures-"
        if song_id in songs_list:
            songs_list[song_id].append({level_id: level_name})
        else:
            songs_list[song_id] = [{level_id: level_name}]

for key, value in songs_list.items():
    songs_list[key] = [len(value), value]
sorted_dict = dict(sorted(songs_list.items(), 
                          key=lambda item: item[1][0], reverse=True))
with open("popular_songs.json", "w") as f:
    f.write(json.dumps(sorted_dict, indent=2))
