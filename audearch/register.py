import audearch.analyzer as aa
from pathlib import Path
import uuid


def register_one(id, path, imongodb):

    list_landmark = aa.analyzer(path)

    for landmark in list_landmark:
        imongodb.insert(id, landmark[0], int(landmark[1]))


def register_directory(dirpath, imongodb):

    p = Path(dirpath)

    for filepath in p.glob("*.wav"):
        id = int(uuid.uuid4())
        register_one(id, filepath, imongodb)
