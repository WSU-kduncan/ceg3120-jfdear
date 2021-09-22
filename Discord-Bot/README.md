Setup  
how to get an API  
* Go to the discord developer portal
* Click new application and type the name of the application
* Then go to the bot tab and add bot
* Then go to the OAuth2 tab and make sure bot is checked and give the bot permissions that you want it to have.
* The OAuth2 tab generates an authorization URL that hits Discord’s OAuth2 API and authorizes API access using your application’s credentials.
* Then copy the URL from that tab and paste and authorize the bot to join your server
* To be able to interact with your bot you will need to copy the bot token from the bot tab
* This will be used in the code to interact with your bot, do not let this code get out!  

where to put it to work with the code  
* You will need to first put the token from the last step into a .env file to be referenced and found for the code. Make sure to put the .env file in a .gitignored file to ensure it does not get pushed onto GitHub and exposed.  
![image](https://user-images.githubusercontent.com/77360294/134280509-11395823-a341-452d-a7c1-81f63d2182b9.png)  
Putting the one from the documentation because I don’t want my token out there.  
dependencies (what packages need to be installed to run the code)  
* python3
* python3-pip
* discord.py
* python-dotenv  


Usage  
with your changes to the code in place, describe   
what commands you can type in your Discord server  
* !dnote  
what response this will provide (from your bot)  
* Gives quotes from the anime Deathnote  
![image](https://user-images.githubusercontent.com/77360294/134280752-216f8db9-a465-4c16-bd15-b42c5e31d31b.png)  

Research  
you may have realized that it is lame that it only runs when you run the program.  
In the real world, things are "always on", not waiting for Bob to turn his PC on and make sure the program is running.  
Research some possible solutions that would solve this, and discuss why you think it would work.  
* Host the python code on a webserver - the python code will be running on the server and when someone runs the command it will contact the webserver to get the response.[link to article](https://stackoverflow.com/questions/52797611/how-can-i-keep-a-python-discord-bot-running-online-without-the-command-prompt)  
  * Run the server locally
  * Run a server on a cloud/hosted provider like AWS 
  * [link to article](https://www.quora.com/How-do-I-keep-a-Python-script-running-24-7-without-leaving-my-computer-continuously-on)



