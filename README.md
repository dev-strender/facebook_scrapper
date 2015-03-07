# facebook_scrapper
a python2.x file for scrap posts/feeds from Facebook
I don't know whether the English-based country has same problem, but at least in my country(Korea), we have some difficulties in finding some posts with using facebook built-in search tool. (Maybe this is kind of encoding problem.) So, this source code is scrapping posts in group feeds and convert to html file. Then, you can easily find your searching keyword with using browser's 'Ctrl + F' method. Chinese, Japanese, and some countries which needs unicode can get help from this code. I hope it. 

#Requirements
- python2.x (not python 3)
- mechanize
- facebook account with developer registered, and an app to get access token from url

##How to Use
1. open 'config.py', and then edit values.
2. run 'facebook_post_scrapper.py' in terminal, or anywhere.
3. Finish! It would make 'document.html' . Find something from it.
