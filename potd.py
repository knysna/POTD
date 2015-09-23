__author__ = 'admin'
""" potd (Password of The Day)
Calculates the passwords for today based on the well known formula. The purpose is to save a few minutes work each day.
Writes the passwords into html and sets up a little http daemon for access. The listening port can be specified.
Browse to <IP>:PORT
The html page is rewritten constantly so that the information is always up to date.
"""

import datetime
import time
import http.server
import socketserver


# Obtain today's date and breakdown into components
todayp = datetime.datetime.now()
pwyear = int(todayp.year)
pwmonth = int(todayp.month)
pwday = int(todayp.day)

# Determine the passwords for today
def exitpw1gen():
    return pwyear + pwmonth + pwday
def exitpw2gen():
    return pwyear + pwmonth - pwday


def potdhtml():
    '''
    Put today's passwords into html format with some headings. Set the browser to auto refresh at an interval.
    '''
    potdContent ="<html>"
    potdContent += "<head><meta http-equiv='refresh' content='60'><h2>Password Of The Day</h2></head><body><h4>Today's Date Is: "
    potdContent += str(datetime.datetime.today().strftime("%d/%m/%Y"))
    potdContent += "</h4><p>Exit Password #1 is: "
    potdContent += str(exitpw1gen())
    potdContent += "</p><p>Exit Password #2 is: "
    potdContent += str(exitpw2gen())
    potdContent += "</p><br>"
    potdContent += "<p>Page was generated at "
    potdContent += str(datetime.datetime.now())
    potdContent +="</p></body></html>"
    return potdContent

def makefile( myfilename, mycontent ):
    '''
    Create a file with the specified name, write the content to the file then close the file.
    myfilename is the name of the file to be created including single quotes e.g. 'index.html'
    mycontent is the content to be written into the file including single quotes e.g. 'this is some content'
    '''
    f = open(myfilename,'w')
    f.write(mycontent)
    f.close()

# Make a webserver
def mini_web_server( myport=8080 ):
    '''
    A very light web server listening on the specified port number. Default port is 8080.
    Also constantly rewrite the index.html file so that the information is always up to date
    '''
    PORT = myport
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), handler)

    print("serving at port", PORT)
    while keepgoing():
        httpd.handle_request()
        makefile('index.html', potdhtml())
        time.sleep(1)


def keepgoing():
    return True

mini_web_server(8088)



