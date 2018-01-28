import web
from firebase import firebase
import json
import datetime

# Formart is URL, classname

urls = (
    '/', 'index',
    '/GetData/(.*)','GetData',
    '/CreateResolution/(.*)', 'CreateRes',
    '/CreateLog/(.*)', 'CreateLog'

)

class index:
    def GET(self):
        #global firebase
        myobj = firebase.FirebaseApplication('https://test-for-newyear.firebaseio.com/', None)
        result = myobj.get('/Users/', None)
        return result

class GetData:
    def GET(self,id):
        #global firebase
        print id
        myobj = firebase.FirebaseApplication('https://api-project-671542151255.firebaseio.com/', None)
        result = myobj.get('/Users/user'+id+'/', None)
        
        return result

# Class for putting Data
class CreateRes:
    def POST(self,id):
        myobj =  firebase.FirebaseApplication('https://test-for-newyear.firebaseio.com/', None)
        userID,resDescription = id.split("_")
        resolutionsData = myobj.get('/Users/'+userID+'/Resolutions/', None)
        newId = 1+len(resolutionsData)
        res_id = userID+'_'+ str(newId)
        data = {res_id: {'Description': resDescription}}
        print data
        result = myobj.patch('/Users/'+userID+'/Resolutions/',data)
        raise web.seeother('/')

class CreateLog:
    def POST(self,id):
        myobj =  firebase.FirebaseApplication('https://test-for-newyear.firebaseio.com/', None)
        print id
        userID,resId,status = id.split("_")
        #newId = 2
        res_id = userID+'_'+ resId
        sysTime = datetime.datetime.now().strftime("%Y_%m_%d");

        data = {sysTime: {'Status': status}}
        print data
        result = myobj.patch('/Users/'+userID+'/Resolutions/'+res_id+'/Logs/',data)
        raise web.seeother('/')

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
