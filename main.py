import os, pickle,json
import time

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


from read import readExcel

from LiveAPIMethods import createEvent
from LiveAPIMethods import updateThumbNail
from LiveAPIMethods import getAllVideoIds
from LiveAPIMethods import updateByVideoId
from LiveAPIMethods import deleteVideoById
from LiveAPIMethods import deleteAllVideos

    
def main():
    print("[1] Read Excel Upload To YT")
    print("[2] List All Live Broadcasts")
    print("[3] Update Broadcast By Id")
    print("[4] Delete Broadcast By Id")
    print("[5] Delete All Broadcasts")
    
    x = int(input("Enter Choice: "))
    if(x == 1):
        valuesToUse = readExcel()
        for x in range(0,2):
            videoId = createEvent(valuesToUse,x)
            time.sleep(1.5)
            updateThumbNail(videoId)
            time.sleep(1.5)
        print("\n")
        print("Broadcast Events Have been created")
        input('Press ENTER to exit')

        
    elif (x == 2):
        maxResults = int(input("Amount of Results Retrieved,input a number[0-50]: "))
        videoInfo = getAllVideoIds(maxResults);
        for x in range(0,len(videoInfo['id'])):
            print("Video Id:",videoInfo['id'][x])
            print("Video Title: ",videoInfo['title'][x])
            print("Video Description: ",videoInfo['description'][x])
            print("Video Schedule: ",videoInfo['schedule'][x])
            print("\n")
        print("All Broacasts Retrieved")
        input('Press ENTER to exit')

            
    elif (x == 3):
        print("Input Video Id, to update more than one video put comma in between video ids. Ex: ZbmQ7yU2h_E,uRvtlU_sdTU")
        videoId = input("video id: ")
        videoId = videoId.replace(' ','')
        videoId = videoId.split(',')
        for x in videoId:
            updateByVideoId(x)
        print("Broadcast Updated")
        input('Press ENTER to exit')

        
        
    
    elif(x == 4):
        print("Input Video Id, to delete more than one video put comma in between video ids. Ex: ZbmQ7yU2h_E,uRvtlU_sdTU")
        videoId = input("video id: ")
        videoId = videoId.replace(' ','')
        videoId = videoId.split(',')
        for x in videoId:
            deleteVideoById(x)
            time.sleep(.5)
        print("Broadcasts Deleted")
        input('Press ENTER to exit')

    
    elif(x == 5):
        choice = input("Are you sure mang?[Y][N]: ")
        if(choice == 'Y' or choice == 'y'):
            maxResults = int(input("Amount of Videos To Be Deleted,input a number[0-50]: "))
            videoInfo = getAllVideoIds(maxResults);
            videoIds = videoInfo['id']
            deleteAllVideos(videoIds)
            print("All Broadcasts Deleted")
        input('Press ENTER to exit')

            
if __name__ == '__main__':
    main()
