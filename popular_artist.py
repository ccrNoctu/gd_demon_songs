import json

songs_list = {}
for i in range(0, 104):
    with open("json_files/page_" + str(i) + ".json") as f:
        data = json.load(f)
    for j in range(9):
        if j >= len(data):
            break
        artist = data[j]["songAuthor"]
        if artist == "hyperdemented":
            artist = "CreoMusic"
        if artist == "DJ-Nate":
            artist = "dj-Nate"
        level_id = data[j]["id"]
        name = data[j]["name"]
        song_name = data[j]["songName"]
        ob = { "level_name": name, 
              "song_name": song_name, 
              "level_id": level_id}
        if artist in songs_list:
            songs_list[artist].append(ob)
        else:
            songs_list[artist] = [ob]
sorted_dict = dict(sorted(songs_list.items(), 
                          key=lambda item: len(item[1]), reverse=True))
with open("popular_artist.json", "w") as f:
    f.write(json.dumps(sorted_dict, indent=2))
