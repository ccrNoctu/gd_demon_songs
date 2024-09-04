import json
with open("popular_artist.json") as f:
    data = json.load(f)
for i in data:
    data[i] = len(data[i])
with open("popular_artist_numbers.json", "w") as f:
    f.write(json.dumps(data, indent=2))
