import audearch.analyzer as aa
from pathlib import Path


def register_one(path, imongodb):
    print("Please enter a unique song ID as an integer")
    id = int(input())

    list_landmark = aa.analyzer(path)

    for landmark in list_landmark:
        imongodb.insert(id, int(landmark[0]), int(landmark[1]))


def register_directory(imongodb):
    print("Please enter the path to the directory where the wave file you want to register is located.")

    dirpath = input()

    p = Path(dirpath)

    for filepath in p.glob("*.wav"):
        register_one(filepath, imongodb)
