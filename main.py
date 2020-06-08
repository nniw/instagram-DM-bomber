from InstagramAPI import InstagramAPI
import webbrowser
import time
import requests
import json


print("""             **          **                  **  **
            ****        /**                 /** /**
 **   **   **//**       /**  *****   *****  /** /**
//** **   **  //**   ****** **///** **///** /** /**
 //***   ********** **///**/*******/******* /** /**
  **/** /**//////**/**  /**/**//// /**////  /** /**
 ** //**/**     /**//******//******//****** *** ***
//   // //      //  //////  //////  ////// /// ///

instagram: @xAdeell\n """)

webbrowser.open('https://instagram.com/xAdeell')

nostop = 0

accounts = input("import your account text file (if you don't have one press Enter to continue :")

if not accounts:
    username = input("Your username : ")
    password = input("Your Password : ")
    api = InstagramAPI(username, password)
    api.login()
    istimes = 0
else:
    f = open(accounts, 'r')
    NumberOfLine = 0
    for line in f:
        NumberOfLine += 1
    username, password = line.split(':')
    print ("Username found: ", username)
    print ("Password found: ", password)
    api = InstagramAPI(username, password)
    api.login()
    istimes = 1

user = input("Victim's username :")

url = "https://www.instagram.com/web/search/topsearch/?context=blended&query="+user+"&rank_token=0.3953592318270893&count=1"
response = requests.get(url)
respJSON = response.json()
user_id = str( respJSON['users'][0].get("user").get("pk") )

message = input("The message you wanna send :")

if istimes == 0:
    times = int(input("The amount of messages you wanna send "))
elif istimes == 1:
    times = NumberOfLine

print("You are gonna STRESS", times,"times", user_id, "with the message: ", message, ".")
input("Are you sure you wanna continue :")

while times > nostop:
    nostop = nostop + 1
    api.sendMessage(user_id,message)
    print(nostop, ">> Sent to", user, ": ", message)



