# helpmewiththemood
     helpmewiththemood is a desktop application that detects 7 tones which are most commonly used to detect the tone of written text. These are: anger, fear, joy, sadness, confident, analytical, and tentative using IBM WATSON tone analyser services and tweeter API. Then play the music playlist on YOUTUBE apt for the person.

# Prerequisites
1.	Sign up for an IBM Cloud account.
2.	Download the IBM Cloud CLI.
3.	Create an instance of the Tone Analyzer service and get your credentials:
o	Go to the Tone Analyzer page in the IBM Cloud Catalog.
o	Log in to your IBM Cloud account.
o	Click Create.
o	Click Show to view the service credentials.
o	Copy the apikey value, or copy the username and password values if your service instance doesn't provide an apikey.
o	Copy the url value.
4.	Getting Twitter API key:
        To start with, you will need to have a Twitter account and obtain credentials (i.e. API key, API secret, Access token and Access token secret) on the Twitter developer site to access the Twitter API, following these steps:

•	Create a Twitter user account if you do not already have one.
•	Go to https://apps.twitter.com/ and log in with your Twitter user account. This step gives you a Twitter dev account under the same name as your user account.
•	Click “Create New App” 
•	Fill out the form, agree to the terms, and click “Create your Twitter application”
•	In the next page, click on “Keys and Access Tokens” tab, and copy your “API key” and “API secret”. Scroll down and click “Create my access token”, and copy your “Access token” and “Access token secret”.

# Creating .exe file from .py file:-

1. After creating the files you need to run and compile them that you can done simply by executing the command used to run any python program in cmd that is
          python.exe [python filename]
2.   To convert the .py file .exe file you need to build the file that has code for setup.Here this file is saved as setup.py which uses cx_Freeze for the setup .
3. You need to go to your project folder where the main code file i.e here ftoneanalyser.py and setup file i.e setup.py and open cmd there by pressing shift key  with right click and typing the command:
           python [setup filename] build
4.	This will build your executable file .Now this is a software that can be shared with your friends as it is now cross platform  software and need not to have all the libraries that are imported in the code in order to run on another system and hence become a standalone desktop application.

# Files and folders

•	Ftoneanalyser.py: 
            A file that contain the main program for the desktop application-All functions required to build front end and the code for the backend i . e api for tone analyser ,for retrieving tweets from twitter ,analysing the sentiments and getting prominent  emotion and for taking proper action according to emotions i.e showing the person name with a massage name showing feeling and suggesting him to click on play button to play on the you tube playlist. As the user click play the you tube with apt music playlist will be open in the default web browser .   

•	License.txt: Contains placeholder text that you replace with the license that you distribute your app with.

•	README.md: The file that you are reading at this moment.

•	requirements.txt: A file for listing the Python libraries that you need for desktop app code, with each library on a new line. Replace the libraries in this file with whatever you need for your application. 
