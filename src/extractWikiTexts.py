import wikipedia

# 取り込む記事のディレクトリとタイトル
dirPass = '../../data/wiki'
print('English' in wikipedia.languages())
titles = wikipedia.random(pages=10)
print(titles)
'''
# Wikipediaのテキストデータを取り込む
texts = [wikipedia.page(t, auto_suggest=False).content for t in titles]

for (title, text) in zip(titles, texts):
    fName = dirPass + '/' + title.replace(' ', '_').lower() + '.txt'

    with open(fName, 'w') as f:
        f.write(text)
'''
