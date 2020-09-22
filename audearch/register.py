import audearch.analyzer as aa


def register(id: int, path: str, size: int, imongodb):

    list_landmark = aa.analyzer(path, size)

    for landmark in list_landmark:
        imongodb.insert_music(id, landmark[0], int(landmark[1]))

    return id
