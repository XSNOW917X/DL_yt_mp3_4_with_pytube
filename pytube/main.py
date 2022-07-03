from asyncio import streams
from pytube import YouTube
from pytube import Playlist
import os
import time

#test
# audio 251; mp4 22;

#playlist download
p = Playlist(
    'https://www.youtube.com/playlist?list=PLhy8TB5U6n17R78U7usaLQfCC8nbnG8Nc')
print(f'Downloading playlist: {p.title}')
for video in p.videos:
    # print video title of playlist
    print(f'Downloading video: {video.title}')
    try:
        yt = video.streams.get_by_itag(251)  # set itag
        yt.download(filename=f'{video.title}.mp3',
                    output_path=f'downloads/{p.title}/')
    except:
        pass
    time.sleep(1)
    
time.sleep(3)
# delete filename isn't mp3
dir_name = f"downloads/{p.title}"
test = os.listdir(dir_name)
for item in test:
    if item.endswith('.mp3') == False:
        os.remove(os.path.join(dir_name, item))


# playlist下載有bug，確認是否有標題.mp3的那邊，
# 用true的話會有一些重複(不確定有沒有少載(有，少False的==))，用False的話，
# 會少一堆==。single那邊還沒測。刪除檔案的部分我很滿意。

# playlist download
# p = Playlist('https://www.youtube.com/playlist?list=PLFBiO80681rRBTydvOuqTDOn34uhn-y2s')
# print(f'Downloading playlist: {p.title}')
# count = 1
# for video in p.videos:
#     print(f'{count}:Downloading video: {video.title}')  #print video title of playlist
#     try:
#         yt = video.streams.get_by_itag(251) #set itag
#          #下載標題.mp3
#         yt.download(filename=f'{video.title}.mp3', output_path=f'downloads/{p.title}/')
#     except:
#         pass
#     #確認是否有其標題.mp3檔，沒有的話標題以序號建立
#     if os.path.isfile(f'downloads/{p.title}/{video.title}.mp3') == True:
#         print(f'無標題.mp3，開始下載序號.mp3。此檔序號為{count}')
#         yt.download(filename=f'{count}.mp3', output_path=f'downloads/{p.title}/')
#     count +=1
#     time.sleep(1)   #良好爬蟲:D

# time.sleep(3)
# #delete filename isn't mp3
# dir_name = f"downloads/{p.title}"
# test = os.listdir(dir_name)
# for item in test:
#     if item.endswith('.mp3') == False:
#         os.remove(os.path.join(dir_name, item))


# single video download
# try:
#     #yt = YouTube('https://www.youtube.com/watch?v=UstE6yTlwcU')    #鹿乃
#     yt = YouTube('https://www.youtube.com/watch?v=p07NIMrcCjs')    #error
#     stream = yt.streams.get_by_itag(251)
#     stream.download(filename=f'{yt.title}.mp3', output_path='downloads')
# except:
#     pass

# if os.path.isfile(f'downloads/{yt.title}.mp3') == False:
#     stream.download(filename=f'errorS.mp3', output_path='downloads')

# dir_name = "downloads/"
# test = os.listdir(dir_name)
# for item in test:
#     if item.endswith('.mp3') == False:
#         os.remove(os.path.join(dir_name, item))


# for i in yt.streams.filter(file_extension='mp4'):
#     print(i)
