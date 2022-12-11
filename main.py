import os, pickle,json
import time

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


from read import readExcel
from services import create_service

    
def createEvent(valuesToUse,x):
    title = (valuesToUse["columnA"][x] + valuesToUse["columnB"][x] + valuesToUse["columnC"][x] + valuesToUse["columnD"][x] + valuesToUse["columnE"][x])
    description = (str(valuesToUse["columnF"][x]) + '\n' + str(valuesToUse["columnG"][x]) + '\n' + str(valuesToUse["columnH"][x]))  
    
    client_secrets_file = r"C:\Users\kenley\Desktop\Youtube API\client_secret_915153775010-vplo5g8u3c4cqhg4msbi9s61utgc81tu.apps.googleusercontent.com.json"
    youtube = create_service(client_secrets_file,
        ["https://www.googleapis.com/auth/youtube.force-ssl"])
    if not youtube: return
    
    request = youtube.liveBroadcasts().insert(
        part="snippet,contentDetails,status",
        body={
            "contentDetails": {
            "enableClosedCaptions": True,
            "enableContentEncryption": True,
            "enableDvr": True,
            "enableEmbed": True,
            "recordFromStart": True,
            "startWithSlate": True
            },
            "snippet":{
                "title": title,
                "description":description,
                "scheduledStartTime": "2022-12-15",
                "scheduledEndTime": "2022-12-18"
            },
            
        "status": {
            "privacyStatus": "unlisted"
        }
    }
    )
    response = request.execute()
    print("Response here: ")
    print(response)
    print("Video id:",response['id'])
    videoId = response['id']
    return videoId

def updateThumbNail(videoId):
    client_secrets_file = r"C:\Users\kenley\Desktop\Youtube API\client_secret_915153775010-vplo5g8u3c4cqhg4msbi9s61utgc81tu.apps.googleusercontent.com.json"
    youtube = create_service(client_secrets_file,
        ["https://www.googleapis.com/auth/youtube.force-ssl"])
    if not youtube: return
    
    request = youtube.thumbnails().set(
        videoId=videoId,
        # TODO: For this request to work, you must replace "YOUR_FILE"
        #       with a pointer to the actual file you are uploading.
        media_body=MediaFileUpload(r"C:\Users\kenley\Desktop\Youtube API\Images\BoykiePIC.png")
    )
    response = request.execute()
    print("Update Thumbnail Response: ",response)
    return None;
    
    
def main():
    valuesToUse = readExcel();
    print("Values to use is ",readExcel)
    # videoId = createEvent();
    for x in range(0,valuesToUse["rows"]):
        videoId = createEvent(valuesToUse,x)
        print("Video Id is ",videoId)
        time.sleep(5)
        updateThumbNail(videoId)
        time.sleep(5)
    
if __name__ == '__main__':
    main()
