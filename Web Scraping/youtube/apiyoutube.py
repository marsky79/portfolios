from requests_html import HTMLSession
import pandas as pd

s = HTMLSession()

url = 'https://www.youtube.com/results?search_query=gaming&sp=EgIQAg%253D%253D'

data = []

r = s.get(url)

#awal r.html.render(sleep=3, timeout=100, keep_page=True, scrolldown=10000)
r.html.render(sleep=3, timeout=100, keep_page=True, scrolldown=1000)

container = r.html.find('ytd-channel-renderer.style-scope.ytd-item-section-renderer')

#use for loop scraping all data
for elem in container:
    #channelname= elem.find('a.channel-link.yt-simple-endpoint.style-scope.ytd-channel-renderer', first=True).text
    channelurl = 'https://www.youtube.com' + elem.find('a.channel-link.yt-simple-endpoint.style-scope.ytd-channel-renderer', first=True).attrs['href']

    data.append([channelurl])

df = pd.DataFrame(data, columns=['channel url']) 
#awal nama file yt_dataset.csv
df.to_csv('yt6_dataset.csv', index=False)

