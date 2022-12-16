import os, pickle,json
import time

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


from read import readExcel
from services import create_service

client_secrets_file = r"C:\Users\kenley\Desktop\New folder (4)\YoutubeApi\client_secret_915153775010-3efr5vro9ig0dipt2mi2a7ne55if9i4u.apps.googleusercontent.com.json"


def createEvent(valuesToUse,x):
    title = str((valuesToUse["columnA"][x] + valuesToUse["columnB"][x] + valuesToUse["columnC"][x] + valuesToUse["columnD"][x] + valuesToUse["columnE"][x]))
    description = (str(valuesToUse["columnF"][x]) + '\n' + str(valuesToUse["columnG"][x]) + '\n' + str(valuesToUse["columnH"][x]))  
    scheduledDate = str(valuesToUse["columnI"][x])
    
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
                "scheduledStartTime": scheduledDate,
            },
        "status": {
            "selfDeclaredMadeForKids": True,
            "privacyStatus": "public"
        }
    }
    )
    response = request.execute()
    print(response)
    print("Broadcast Event Created")
    videoId = response['id']
    return videoId

def updateThumbNail(videoId):
    youtube = create_service(client_secrets_file,
        ["https://www.googleapis.com/auth/youtube.force-ssl"])
    if not youtube: return
    
    request = youtube.thumbnails().set(
        videoId=videoId,
        # TODO: For this request to work, you must replace "YOUR_FILE"
        #       with a pointer to the actual file you are uploading.
        media_body=MediaFileUpload(r"C:\Users\kenley\Desktop\New folder (4)\YoutubeApi\charlesdeluvio-pcZvxrAyYoQ-unsplash.jpg")
    )
    response = request.execute()
    print(response)
    print("Thumbnail Updated")
    return None;



def getAllVideoIds(maxResults):
    youtube = create_service(client_secrets_file,
        ["https://www.googleapis.com/auth/youtube.force-ssl"])
    if not youtube: return
    request = youtube.liveBroadcasts().list(
        part="snippet,contentDetails,status",
        broadcastStatus="all",
        broadcastType="all",
        maxResults=maxResults
    )
    videoIds = []
    videoTitle = []
    videoDescription = []
    response = request.execute();
    for x in (response['items']):
        videoIds.append(x['id'])
        videoTitle.append(x['snippet']['title']) 
        videoDescription.append(x['snippet']['description'])
    
    videoInfo = {
        "id":videoIds,
        "title":videoTitle,
        "description":videoDescription
    }
    return videoInfo
    


def deleteVideoById(videoId):
    youtube = create_service(client_secrets_file,
        ["https://www.googleapis.com/auth/youtube.force-ssl"])
    if not youtube: return
    
    request = youtube.liveBroadcasts().delete(
        id=videoId
    )
    response = request.execute()
    print(response)
    return None;

def deleteAllVideos(videoIds):
    for x in range(0,len(videoIds)):
        videoId = videoIds[x];
        youtube = create_service(client_secrets_file,
            ["https://www.googleapis.com/auth/youtube.force-ssl"])
        if not youtube: return
        
        request = youtube.liveBroadcasts().delete(
        id=videoId
        )
        request.execute();
        print("Broadcast Deleted")
        time.sleep(.5)
        
def updateByVideoId(videoId):
    youtube = create_service(client_secrets_file,
        ["https://www.googleapis.com/auth/youtube.force-ssl"])
    if not youtube: return
    
    request = youtube.liveBroadcasts().update(
        part="contentDetails,snippet",
        body={
            "contentDetails": {
            "enableClosedCaptions": True,
            "enableContentEncryption": True,
            "enableDvr": True,
            "enableEmbed": True,
            "recordFromStart": True,
            "startWithSlate": True,
            "monitorStream": {
            "enableMonitorStream": True,
            "broadcastStreamDelayMs": 5
            }
        },
        "id": videoId,
        "snippet": {
            "scheduledStartTime": "2022-12-25",
            "title": "Changed Title"
        }
        }
    )
    response = request.execute()
    print(response)    
    
    
def main():
    print("[1] Read Excel Upload To YT")
    print("[2] List All Live Broadcasts")
    print("[3] Update Broadcast By Id")
    print("[4] Delete Broadcast By Id")
    print("[5] Delete All Broadcasts")
    
    x = int(input("Enter Choice: "))
    if(x == 1):
        valuesToUse = readExcel()
        # videoId = createEvent();
        for x in range(0,valuesToUse["rows"]):
            videoId = createEvent(valuesToUse,x)
            time.sleep(1.5)
            updateThumbNail(videoId)
            time.sleep(1.5)
        print("Broadcasts Have Been Created")
        
    elif (x == 2):
        maxResults = int(input("Amount of Results Retrieved,input a number[0-50]: "))
        videoInfo = getAllVideoIds(maxResults);
        for x in range(0,len(videoInfo['id'])):
            print("Video Id:",videoInfo['id'][x])
            print("Video Title: ",videoInfo['title'][x])
            print("Video Description: ",videoInfo['description'][x])
            print("\n")
            
    elif (x == 3):
        print("Input Video Id, to update more than one video put comma in between video ids. Ex: ZbmQ7yU2h_E,uRvtlU_sdTU")
        videoId = input("video id: ")
        videoId = videoId.replace(' ','')
        videoId = videoId.split(',')
        for x in videoId:
            updateByVideoId(x)
        
        
    
    elif(x == 4):
        print("Input Video Id, to delete more than one video put comma in between video ids. Ex: ZbmQ7yU2h_E,uRvtlU_sdTU")
        videoId = input("video id: ")
        videoId = videoId.replace(' ','')
        videoId = videoId.split(',')
        for x in videoId:
            deleteVideoById(x)
        print("Broadcasts Deleted")
    
    elif(x == 5):
        choice = input("Are you sure mang?[Y][N]: ")
        if(choice == 'Y' or choice == 'y'):
            maxResults = int(input("Amount of Videos To Be Deleted,input a number[0-50]: "))
            videoInfo = getAllVideoIds(maxResults);
            videoInfo = getAllVideoIds()
            videoIds = videoInfo['id']
            deleteAllVideos(videoIds)
            

    
if __name__ == '__main__':
    main()
