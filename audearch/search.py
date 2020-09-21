import audearch.analyzer as aa
import statistics


def search(path: str, size: int, imongodb):
    ids = []

    list_landamrk = aa.analyzer(path, size)

    for i, landmark in enumerate(list_landamrk):
        id1, id2, id3 = [], [], []

        cur1 = imongodb.find_music(filter={'music_hash': int(landmark[0])})
        cur2 = imongodb.find_music(filter={'music_hash': int(list_landamrk[i+1][0])})
        cur3 = imongodb.find_music(filter={'music_hash': int(list_landamrk[i+2][0])})

        for doc1, doc2, doc3 in zip(cur1, cur2, cur3):

            id1.append(doc1['music_id'])
            id2.append(doc2['music_id'])
            id3.append(doc3['music_id'])

        id_common_123 = list(set(id1) & set(id2) & set(id3))
        ids.extend(id_common_123)

    ans = statistics.mode(ids)

    return ans
