import statistics

from tqdm import tqdm

import audearch.analyzer as aa


def search_music(list_landmark, imongodb, progress=None):
    ids = []

    if progress is None:
        pass
    else:
        progress[0] = len(list_landmark)
        progress[1] = 3

    for i, landmark in enumerate(tqdm(list_landmark)):
        id1, id2, id3 = [], [], []

        if i == len(list_landmark) - 3:
            break
        else:
            cur1 = imongodb.find_music(filter={'music_hash': landmark[0]})
            cur2 = imongodb.find_music(filter={'music_hash': list_landmark[i + 1][0]})
            cur3 = imongodb.find_music(filter={'music_hash': list_landmark[i + 2][0]})

        for doc1, doc2, doc3 in zip(cur1, cur2, cur3):

            id1.append(doc1['music_id'])
            id2.append(doc2['music_id'])
            id3.append(doc3['music_id'])

        if progress is None:
            pass
        else:
            progress[1] = int(progress[1]) + 1

        id_common_123 = list(set(id1) & set(id2) & set(id3))
        ids.extend(id_common_123)

    ans = statistics.mode(ids)

    return ans


def search(path: str, size: int, imongodb):

    list_landmark = aa.analyzer(path, size)

    ans = search_music(list_landmark, imongodb)

    return ans


def librosa_search(path: str, size: int, imongodb):

    list_landmark = aa.librosa_analyzer(path, size)

    ans = search_music(list_landmark, imongodb)

    return ans
