import requests


def requestPlaylistId(key, channelId):
    url = 'https://www.googleapis.com/youtube/v3/channels'

    payload = {'key'  : key             ,
               'id'   : channelId       ,
               'part' : 'contentDetails'}

    res = requests.get(url, params=payload)
    res_js = res.json()

    return res_js['items'][0]['contentDetails']['relatedPlaylists']['uploads']



def requestVideos(key, playlistId, n_video):
    url = 'https://www.googleapis.com/youtube/v3/playlistItems'

    payload = {'key'        : key       ,
               'playlistId' : playlistId,
               'part'       : 'snippet' ,
               'maxResults' : n_video   }

    # コメント数が５０を超える場合はリクエストを複数回にする
    max_result = 50
    n_max = n_video // max_result
    n_results = [max_result] * n_max
    n_results.append(n_video - max_result * n_max)

    videos = []
    titles = []
    pageToken = None

    for n_rslt in n_results:
        payload['maxResults'] = n_rslt
        payload['pageToken' ] = pageToken

        res = requests.get(url, params=payload)
        res_js = res.json()

        for i in res_js['items']:
            videos.append(i['snippet']['resourceId']['videoId'])
            titles.append(i['snippet']['title'])
            pageToken = res_js['nextPageToken']

    return videos, titles



def requestVideoInfo(key, videoId):
    url = 'https://www.googleapis.com/youtube/v3/videos'

    payload = {'key'  : key         ,
               'id'   : videoId     ,
               'part' : 'statistics'}

    res = requests.get(url, params=payload)
    res_js = res.json()

    return int(res_js['items'][0]['statistics']['commentCount'])



def requestComments(key, videoId, n_comment):
    url = 'https://www.googleapis.com/youtube/v3/commentThreads'

    payload = {'key'       : key        ,
               'videoId'   : videoId    ,
               'part'      : 'snippet'  ,
               'textFormat': 'plainText',
               'order'     : 'relevance'}

    # コメント数が１００件を超える場合はリクエストを複数回にする
    max_result = 100
    n_max = n_comment // max_result
    n_results = [max_result] * n_max
    n_results.append(n_comment - max_result * n_max)

    comments = ''
    pageToken = None

    for n_rslt in n_results:
        payload['maxResults'] = n_rslt
        payload['pageToken' ] = pageToken

        res = requests.get(url, params=payload)
        res_js = res.json()

        for item in res_js['items']:
            topComment = item['snippet']['topLevelComment']
            comments += topComment['snippet']['textDisplay'] +'\n'
            print(topComment['snippet']['textDisplay'])

        if 'nextPageToken' in res_js:
            pageToken = res_js['nextPageToken']

    return comments
