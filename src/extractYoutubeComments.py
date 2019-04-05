from youtubeAPI import *

# 認証キー
myKey = 'AIzaSyA-O0uzlqcSlHprgwhnheqvLbIK90jGPug'
channelId = 'UCENoC6MLc4pL-vehJyzSWmg'

dir = './data/youtube_comments'

playlistId = requestPlaylistId(myKey, channelId)
videos, titles = requestVideos(myKey, playlistId, 1)

for video, title, count in zip(videos, titles, range(len(videos))):
    try:
        comment = requestComments(myKey, video, requestVideoInfo(myKey, video))
        with open(dir + '/' + title + '.txt', 'w') as f:
            f.write(comment)

        print('{:>3} | O | {}'.format(count, title))

    except Exception:
        print('{:>3} | X | {}'.format(count, title))
