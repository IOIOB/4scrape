import os
import json
import requests
import sys

def saveImages(board, thread):
    urlHeader = 'https://a.4cdn.org/'
    url = urlHeader + board + '/thread/' + str(thread) + '.json'

    threadJson = requests.get(url)
    threadJson = json.loads(threadJson.text)

    for x in threadJson['posts']:
        directory = board + '-' + thread
        if not os.path.exists(directory):
            os.mkdir(directory)
        if 'filename' in x:
            filename = x['filename'] + x['ext']
            fileUrl = "https://i.4cdn.org/" + board + '/' + str(x['tim']) + x['ext']
            print('Saving "' + filename + '"...')
            image = requests.get(fileUrl)
            imageFile = open(directory + '/' + filename, 'wb')
            imageFile.write(image.content)
            imageFile.close()


if len(sys.argv) < 2:
    print(
        "Error: not enough arguments supplied\n"
        "Use as: python scrub.py [BOARD] [THREAD NUMBER]\n"
        "E.g. python scrub.py sci 3241234"
    )
else:
    saveImages(sys.argv[1], sys.argv[2])