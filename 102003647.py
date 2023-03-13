import urllib.request
import re
import pandas as pd
import random
from pytube import YouTube
from pydub import AudioSegment
import sys
import os



# X=(input("Singer Name :"))
# N=int(input("Number of Youtube Videos whose audio is to be extracted : "))
# Y=int(input("Duration(in sec) for which audio is to cut : "))
def fun(singer_name,yt_vids,sec_shot,final_file):
  singer_name=singer_name.lower()
  singer_name=singer_name.replace(" ", "")+"videosongs"

  html=urllib.request.urlopen("https://www.youtube.com/results?search_query="+singer_name)
  vid_ids=re.findall(r"watch\?v=(\S{11})" , html.read().decode())

  n=len(vid_ids)
  url = []
  for i in range(yt_vids):
      url.append("https://www.youtube.com/watch?v=" + vid_ids[random.randint(0,n-1)])

  finall = AudioSegment.empty()
  for i in range(yt_vids):   
    audio_file = YouTube(url[i]).streams.filter(only_audio=True).first()
    audio_file.download(filename='Audio-'+str(i+1)+'.mp3')
    print("\nAudio_file "+str(i+1)+" has been downloaded successfully !!😎")
    audio_file = str(os.getcwd()) + '/Audio-'+str(i+1)+'.mp3'
    file1 = AudioSegment.from_file(audio_file)
    file2 = file1[:sec_shot*1000]
    finall = finall + file2
    finall.export(final_file, format="mp3")


  for i in range(yt_vids):
      file3=audio_file = str(os.getcwd()) + '/Audio-'+str(i+1)+'.mp3'
      print("\nAudio_file "+str(i+1)+" has been removed successfully !!😎")
      os.remove(file3)

  print("\n Mashup By Cherish has been created !! 🔊🎙")

if len(sys.argv) == 5:
  singer_name = sys.argv[1]
  yt_vids = int(sys.argv[2])
  final_file = sys.argv[4]
  sec_shot = int(sys.argv[3])

else :
	print("Incorrect number of arguments ❗")


fun(singer_name,yt_vids,sec_shot,final_file)