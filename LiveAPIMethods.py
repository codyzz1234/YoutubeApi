
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from services import create_service


client_secrets_file = r"client_secret_915153775010-3efr5vro9ig0dipt2mi2a7ne55if9i4u.apps.googleusercontent.com.json"

def createEvent(valuesToUse,x):
    # title = str(valuesToUse["colA"][x] + valuesToUse["colB"][x] + valuesToUse["colC"][x] + valuesToUse["colD"][x] + valuesToUse["colE"][x])
    # description = str(valuesToUse["colF"][x] + '\n' + valuesToUse["colG"][x] + '\n' + valuesToUse["colH"][x])  
    # scheduledDate = str(valuesToUse["colI"][x])
    
    title = str(''.join(valuesToUse["titles"][x])) ## removes the '[]' brackets
    description = str('\n'.join(valuesToUse["descriptions"][x])) ## adds new line after each element
    scheduledDate = str(valuesToUse["dates"][x])
    
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
        media_body=MediaFileUpload(r"Billy.png")
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
    videoSchedule = []
    response = request.execute();
    for x in (response['items']):
        videoIds.append(x['id'])
        videoTitle.append(x['snippet']['title']) 
        videoDescription.append(x['snippet']['description'])
        videoSchedule.append(x['snippet']['scheduledStartTime'])
        
    
    videoInfo = {
        "id":videoIds,
        "title":videoTitle,
        "description":videoDescription,
        "schedule":videoSchedule
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
        
        request = youtube.liveBroadcasts().delete( #Request body, see documentation to edit it to your liking
        id=videoId
        )
        request.execute();
        print("Broadcast Deleted")
        
def updateByVideoId(videoId):
    youtube = create_service(client_secrets_file,
        ["https://www.googleapis.com/auth/youtube.force-ssl"])
    if not youtube: return
    
    request = youtube.liveBroadcasts().update( #Request body, see documentation to edit it to your liking.
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
    
