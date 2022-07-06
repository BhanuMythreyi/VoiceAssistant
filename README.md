# VoiceAssistant

It is basically used for automation (Python is used)

This is a virtual assistant that works on our voice commands. It can Send Emails, Open applications on our local system like Zoom,VS Code Editor. And Web pages like Linkedin or google. And can also search for queries on wikipedia.

Email:
	To send an email the sender's mail id and password are already stored in a function. Now we do have a dictionary containing all the mail id’s for which we will be communicating. In the dictionary we actually map the receiver's name with the mail id so once we tell the system the name of the recipient it confirms the email id with us and proceeds further to take the subject and the content of the email.
  
Other Applications:
	For the other applications in the conversation with the assistant we just have to say open and the application’s or website’s name.

installed packages:
pyttsx3;  Python Text To Speech, used by the system to convert the text and speak to us; syntax: pip install pyttsx3

Speech_recognition; To recognize the users voice; syntax: pip install speechRecognition

wikipedia; To search on the web for queries; syntax: pip install wikipedia

PyAudio; syntax: pip install pipwin --> pipwin install pyaudio

Smtplib ## Simple mail transfer protocol

os  is imported to open the applications present in the local system

Webbrowser is imported to open web sites like linkedin and google
