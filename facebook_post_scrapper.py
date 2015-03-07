#-*- coding: utf-8 -*-

#from datetime import datetime
#import facebook
import urllib2
import mechanize
import json
import sys, os

from config import fb_email, fb_pass, app_id, group_id, limit

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

facebook_app_link='https://www.facebook.com/dialog/oauth?scope=manage_pages,status_update,publish_stream&redirect_uri=http://strender.tistory.com&response_type=token&client_id='+str(app_id)

br_mech = mechanize.Browser()
br_mech.set_handle_robots(False)

br_mech.open(facebook_app_link)

br_mech.form = list(br_mech.forms())[0]
control = br_mech.form.find_control("email")
control.value=fb_email
control = br_mech.form.find_control("pass")
control.value=fb_pass

br_mech.submit()

access_token = br_mech.geturl().split("token=")[1].split("&expires")[0]

group_post_link = 'https://graph.facebook.com/'+str(group_id)+'/feed?access_token='+access_token+'&limit='+str(limit)

saveFile = open('document.html', 'w')

start_str = "<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'><meta http-equiv='X-UA-Compatible' content='IE=edge'><meta name='viewport'content='width=device-width, initial-scale=1'><title>facebook group feed</title><link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css'></head><body>"
end_str = "<script src='https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js'></script><script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js'></script></body></html>"

saveFile.write(start_str)


j = urllib2.urlopen(group_post_link)
j = json.loads(j.read())

#print j
for x in j['data']:
	try:
		if (x['message'] and x['comments']):
			saveFile.write("<div class='well'><h5>Post</h5><p>Date: %s Time: %s  by %s </p>" % (x['created_time'].split('T')[0], x['created_time'].split('T')[1].split('+')[0], x['from']['name'].encode('utf-8')))
			saveFile.write("<p>%s</p><br />" % x['message'].encode('utf-8'))

			if x['comments']:
				saveFile.write("<h5>Comment</h5>")
				for y in x['comments']['data']:
					saveFile.write("<p>%s</p>" % y['from']['name'].encode('utf-8'))
					saveFile.write("<p>%s</p>" % y['message'].encode('utf-8'))
				saveFile.write("</div>")	
			else:
				pass
			#	saveFile.write("</div>")
		else:
			pass
			saveFile.write("</div>")
	except Exception, e:
		pass

saveFile.write(end_str)
saveFile.close()
