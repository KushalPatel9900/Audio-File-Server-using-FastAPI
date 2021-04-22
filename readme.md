<h1 align="center">Audio File Server using FastAPI</h1>

A web API that simulates the behavior of an audio file server while using a mySQL database made with FastAPI.
## Steps to follow
1. Clone the repository to specific folder in your computer.
2. Create Virtual environment in the project folder of the computer.
- **Windows**
   - Firstly, open command prompt window in your project folder.
   - Run`python -m venv example_env` in cmd window. (*example_env* is the name of the virtual environment. you can replace it with the name you want.)
   - To activate the virtual environment you created, run:
		`example_env\Scripts\activate.bat`
	- Now, its time to install the libraries mentioned in the __requirements.txt__ file that are used to build this project. Run
	`pip install -r requirements.txt`
3. Before starting the server, please install **mysql workbench** and set up the connection to the database. Replace with your userID, password, host and database name in <br>`SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://userID:password@host/dbName"` of __audioAPI/database.py__ file.
4.  To run the server, run `uvicorn audioAPI.main:app --reload` in terminal. In most of the cases, you can access the API on [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
	For better results, run the above code on VS Code terminal to start the uvicorn server.

## Structure of Create and Update API

__Song__ - {"Name" : "name", "Duration": 123}

__Podcast__ - {"Name": "name", "Duration": 123, "Host": "host", "Participants": "participants" }

__Audiobook__ - {"Title": "title", "Author": "anchor", "Narrator": "narrator", "Duration": 123}
 
(Paste the above dictionary in place of value of audioFileMetadata key.) <br><br>
*For Example:*
> { <br>
  "audioFileType": "Song", <br>
  "audioFileMetadata": {“Name” : “name”, “Duration”: 123}<br>
}
 
## Task Question

**Write a Flask / FastAPI / Django Web API that simulates the behavior of an audio file server while using a MongoDB / SQL database.**

Requirements: You have one of three audio files which structures are defined below  

Audio file type can be one of the following:  
1) Song
2) Podcast
3) Audiobook

**Song file fields:**  
- ID – (mandatory, integer, unique)
- Name of the song – (mandatory, string, cannot be larger than 100 characters)
- Duration in number of seconds – (mandatory, integer, positive)
- Uploaded time – (mandatory, Datetime, cannot be in the past)

**Podcast file fields:**
- ID – (mandatory, integer, unique)
- Name of the podcast – (mandatory, string, cannot be larger than 100 characters)
- Duration in number of seconds – (mandatory, integer, positive)
- Uploaded time – (mandatory, Datetime, cannot be in the past)
- Host – (mandatory, string, cannot be larger than 100 characters)
- Participants – (optional, list of strings, each string cannot be larger than 100 characters, maximum of 10 participants possible)

**Audiobook file fields:**
- ID – (mandatory, integer, unique)
- Title of the audiobook – (mandatory, string, cannot be larger than 100 characters)
- Author of the title (mandatory, string, cannot be larger than 100 characters)
- Narrator - (mandatory, string, cannot be larger than 100 characters)
- Duration in number of seconds – (mandatory, integer, positive)
- Uploaded time – (mandatory, Datetime, cannot be in the past)

Implement create, read, upload, and delete endpoints for an audio file as defined below:

**Create API:**
The request will have the following fields:
- audioFileType – mandatory, one of the 3 audio types possible.
- audioFileMetadata – mandatory, dictionary, contains the metadata for one of the three audio files (song, podcast, audiobook).

**Delete API:**
- The route will be in the following format:
“\<audioFileType>/\<audioFileID>”

**Update API:**
- The route be in the following format: “\<audioFileType>/\<audioFileID>”
- The request body will be the same as the upload.

**Get API:**
- The route “\<audioFileType>/\<audioFileID>” will return the specific audio file.
- The route “\<audioFileType>” will return all the audio files of that type.

**The response of these methods should be one of the following:**
- Action is successful: 200 OK
- The request is invalid: 400 bad request
- Any error: 500 internal server error

**Recommendations:** 
- Create only four endpoints (make them generic and usable for all audio file types, do not create four endpoints for each of them).
- The classes should be written in such a way that they are easy to test.  
- Write as many tests as you think is enough to be certain about your solution works  .
- Use SOLID principles.  
- Use design patterns where you find it suitable.