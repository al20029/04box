import urllib.request
import time

time_start = time.time()
# 6つのうちどれか1つのコメントアウト外して実行
# https://al86-hs.github.io/DownloadTest/以降のtest~~Mがサイズと一致してる
#urllib.request.urlretrieve('https://al86-hs.github.io/DownloadTest/test10M')
urllib.request.urlretrieve('https://al86-hs.github.io/DownloadTest/test25M')
# urllib.request.urlretrieve('https://al86-hs.github.io/DownloadTest/test30M')
#urllib.request.urlretrieve('https://al86-hs.github.io/DownloadTest/test50M')
# urllib.request.urlretrieve('https://al86-hs.github.io/DownloadTest/test70M')
# urllib.request.urlretrieve('https://al86-hs.github.io/DownloadTest/test100M')
#urllib.request.urlopen('https://al86-hs.github.io/DownloadTest/test25M').read()

time_end = time.time()

print(str(25/(time_end-time_start)))