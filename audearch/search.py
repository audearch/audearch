import audearch.analyzer as aa
import statistics


def search(path: str, size: int, imongodb):
    ids = []

    list_landamrk = aa.analyzer(path, size)

    for landmark in list_landamrk:
        cur = imongodb.find_music(filter={'music_hash': int(landmark[0])})
        for doc in cur:
            ids.append(doc['music_id'])

    ans = statistics.mode(ids)

    return ans
