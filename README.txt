How to run:
1) Run pip install virtualenv in command prompt
2) Change directory to program folder in command prompt
3) Download EmotionDetectionModel.h5 and env from link below and place into program folder
	-https://drive.google.com/file/d/1sECnCJMSMRQpz2MrYSb9wi6KbUGYTPv9/view?usp=sharing
	-https://drive.google.com/drive/folders/16BiW2ycnDkwJERuh8u_6V96q-dgDhDeF?usp=sharing 
4) Run env\Scripts\activate in command prompt
5) Run python gui.py
6) Go to https://developer.spotify.com/console/get-current-user/
	-Click get token (no scopes required).
	-Press "TRY IT".
	-Scroll down on the right side and find "id".
	-Copy the value of "id" 
	-Paste id in the "User ID" section of the programs settings.
	-Copy "OAuth Token" (CTRL + A to highlight the whole token).
	-Paste "OAuth Token" into the "Authorization Key" section of the programs settings.
	-Click "save" in settings window.
7)Click create playlist 
	-If error occurs change camera value to 0 or 1 in settings
