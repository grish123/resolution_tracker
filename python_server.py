import web
from firebase import firebase
import json


urls = (
    '/', 'index',
    '/GetData/(.*)','GetData',
    '/PostData/(.*)', 'PostData'
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
class PostData:
    def POST(self,id):
        myobj =  firebase.FirebaseApplication('https://api-project-671542151255.firebaseio.com/', None)
        data = {'url': 't1', 'address': 't4', 'name': 't3'}
        print  'my id is = ' + id
        result = myobj.patch('/Users/users'+id, data)
        raise web.seeother('/')

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()