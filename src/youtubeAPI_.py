import requests
import json



def requestPlaylistId(key, channelId):
    url = 'https://www.googleapis.com/youtube/v3/channels'

    payload = {'key'  : key             ,
               'id'   : channelId       ,
               'part' : 'status'}

    res = requests.get(url, params=payload)
    res_js = res.json()

    print(json.dumps(res_js, indent=4))
    #return res_js['items'][0]['contentDetails']['relatedPlaylists']['uploads']


if __name__ == '__main__':
    # 認証キー
    myKey = 'AIzaSyA-O0uzlqcSlHprgwhnheqvLbIK90jGPug'
    channelId = 'UCENoC6MLc4pL-vehJyzSWmg'

    requestPlaylistId(myKey, channelId)
