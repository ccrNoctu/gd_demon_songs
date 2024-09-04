import urllib.request
from urllib.request import urlretrieve

MAX_PAGE = 104
page_current = 0
for i in range(0, 105):
    url = "https://gdbrowser.com/api/search/*?page=" + str(i) + "&count=10&type=mostliked&diff=-2&demonFilter=5"
    filename = "json_files/page_" + str(i) + ".json"
    urlretrieve(url, filename)
    print("Finished page " + str(i) + ".")
print("All done!")

