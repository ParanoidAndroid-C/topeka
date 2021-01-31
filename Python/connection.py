import pyrebase
import config

fb_config = {
  "apiKey": config.FB_API_KEY,
  "authDomain": config.FB_AUTH_DOMAIN,
  "databaseURL": config.FB_DATABASE_URL,
  "storageBucket": config.FB_STORAGE_URL
}

firebase = pyrebase.initialize_app(fb_config)
db = firebase.database()
producers = db.child("Users").get()



def event_handler(message):
  if message['event'] == 'put':
    


    db.child("Events" + message['path']).child
  print(message["event"]) # put
  print(message["path"]) # /-K7yGTTEp7O549EzTYtI
  print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

add_event_stream = db.child("Events").stream(event_handler)

