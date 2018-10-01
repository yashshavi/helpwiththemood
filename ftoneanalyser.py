def option2(feel):
    query_string = urllib.parse.urlencode({"search_query" : feel})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    v=webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0])
    
def option(ff):
    consumer_key="hDTDGGBofjEwow9CPHa1AgBop" 
    consumer_secret="tjMtAVQWY6sVU0MzLW3vbAx22S2hJWZP0JdkXgkQl632OxtqqJ" 
    token="1044867739838554112-OQQpIvViWsXWqQCDXJy1PwflSqxwdt"
    token_secret="okJROYaykdfE7IQCHsbZ9e7dA7TISkfUyXEJqbDy2v0Q6" 
    t = Twitter(
                 auth=OAuth(token, token_secret, consumer_key, consumer_secret))
    tweets=t.statuses.user_timeline(screen_name=ff)
    te=tweets
    def split_count(text):
        total_emoji = []
        data = regex.findall(r'\X',text)
        flag = False
        for word in data:
            if any(char in emoji.UNICODE_EMOJI for char in word):  
                total_emoji += [word] # total_emoji is a list of all emojis
         # Remove from the given text the emojis
        for current in total_emoji:
                text = text.replace(current, '') 
        return text
    final_text=''
    for i in range(1,len(te)):
        final_text = final_text+split_count(te[i]['text'])
    thestring =final_text
    URLless_string = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', thestring)
    dd=re.sub(r'@', '',URLless_string )
    toneanalyzer=ToneAnalyzerV3(version='2018-10-04',
                                 username='704949b8-97aa-455c-9cd0-dfa7e497b290',
                                 password='1AKlN62B3VNx',
                                 )
    toneanalyzer.set_url('https://gateway.watsonplatform.net/tone-analyzer/api')
    text=dd
    tone_analysis = toneanalyzer.tone(
                                        {'text': text},
                                         'application/json'
                                      ).get_result()
    s2=json.dumps(tone_analysis,indent=2)
    s3=s2.lower()
    #word_count(s3)
    #anger, fear, joy, and sadness
    e_d={'sad':'sadness','ang':'anger','fer':'fear','jy':'joy'}
    s_d={'a':'analytical','c':'confident','t':'tentative'}
    count=dict()
    for x in e_d.keys():
          count[x]=(s2.count(e_d[x]))
    emotion=max(count,key=count.get)
    if emotion=='sad':
        exp='sad'
        feeling='upbeat music'
    if emotion=='ang':
        exp='anger'
        feeling='calm down music'
    if emotion=='fer':
        exp='fear'
        feeling='music for strength'
    if emotion=='jy':
        exp='joy'
        feeling='music for cheering'
    r2=Tk()
    r2.title('tone analyser')
    
    if exp=='sad':
        l1=Label(r2,text=ff+' \n\n Hmm! feealing sad.\nJust be motivated with the music.\n')
    if exp=='anger':
        l1=Label(r2,text=ff+"  \n\nAngry!!\nI hope things improve for you soon till that Calm down your self with the musicplaylist suggested for you.\n")
    if exp=='fear':
        l1=Label(r2,text=ff+'  \n\nAfraid!\nRelax here is the music palylist for you.which will help you to soothe yourself.\n')
    if exp=='joy':
        l1=Label(r2,text=ff+'  \n\nfeeling happy!\nNice, celebrate yoursellf with the music.\n')
        
    
    l1.grid(row=0,column=0)
    e1.grid(row=0,column=1)
    b1=Button(r2,text='Play',command=lambda:option2(feeling))
    b1.grid(row=2,column=0)
    r2.mainloop()
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
from twitter import *
import emoji
import regex
import re
from watson_developer_cloud import ToneAnalyzerV3
import urllib.request
import urllib.parse
import re
import webbrowser
import json
import urllib.request
import urllib.parse
import re
import webbrowser
from tkinter import *
r=Tk()
r.title('my application')
l1=Label(r,text="enter twitter screen name")
e1=Entry(r)
l1.grid(row=0,column=0)
e1.grid(row=0,column=1)
b1=Button(r,text='submit',command=lambda:option(e1.get()))
b1.grid(row=2,column=0)
r.mainloop()
