import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib # simple mail transfer protocol
from email.message import EmailMessage


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()



def ConversationStarter():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("How may I assist you, Hmmmmm.... by the way .. just say quit if you don't want me to assist")
    speak(" Also you are requested to observe the commands in the terminal to continue our conversation")
    


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening to you.........")
        r.pause_threshold = 1
        text = r.listen(source)

    try:
        print("I am recognizing your voice")
        query = r.recognize_google(text,language='en-in') # Here Iam calling the google API to convert the voice obtained through microphone to text
        print(f'You said: {query}\n')
    except Exception as e:
        print("I didn't catch you, Please come again")
        return "1"
    return query



def sendEmail(receiver_mail_id,subject,content):
    server = smtplib.SMTP('smtp.gmail.com',587) # smtp.gmail.com is used because here I am sending the mail using gmail
    server.ehlo()
    server.starttls() # tls: transport layer security
    sender_mail_id = 'mymainmailid@gmail.com' # changing the mail id is required before using the code
    password = 'secret_password' # changing the password is also required.I just added some demo password
    server.login(sender_mail_id,password)
    email = EmailMessage()
    email['From'] = sender_mail_id
    email['To'] = receiver_mail_id
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    # server.close()

#Before executing add emails in this section, I just modified the emails to demo emails
dictionary_of_EmailIDs ={'lion': 'demodemo1@gmail.com','cat':'demodemo2@gmail.com','wow':'demodemo3@gmail.com'} # The dictionary here matches the name of the recepient and their email id

count = 0
def emailDetailsCollector():
    global count
    speak("Tell me the receiver's name")
    receiver = takecommand()
    receiver_mail_id = dictionary_of_EmailIDs[receiver]
    speak("Before proceeding further just verify the email id shown on the terminal")
    print(receiver_mail_id)
    speak("Okay! just tell me yes or no,is this the correct mail ID")
    verification = takecommand()
    if 'no' in verification:
        emailDetailsCollector()
        count += 1
    if count==0:           
        speak("Tell me the content that has to be sent")
        content = takecommand()
        speak("Tell me the subject of the mail")
        subject = takecommand()
        sendEmail(receiver_mail_id,subject,content)
        speak("The email is sent successfully")





if __name__ == '__main__':
    ConversationStarter()

    while True:
        query = takecommand().lower()
        
        if 'open' and 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open' and 'notepad' in query:
            speak("Opening notepad")
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif 'open' and 'vs code' in query:
            speak("Opening visual studio code editor")
            npath = 'C:\\Users\\sastri\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(npath)
        
        elif 'open' and 'zoom meetings' in query:
            speak("Opening zoom meetings")
            npath = 'C:\\Users\\sastri\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe'
            os.startfile(npath)

        elif 'open' and 'paint' in query:
            speak("Opening paint")
            npath = "C:\\Windows\\system32\\mspaint.exe"
            os.startfile(npath)

        elif 'open' and 'google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'what' and 'is' and 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'The time is {strTime}')

        elif 'open' and 'linkedin' in query:
            speak("Opening linkedin")
            webbrowser.open("www.linkedin.com")

        elif 'send' and 'email' in query:
            try:
                emailDetailsCollector()
            except Exception as e:
                print(e)
                speak("Unable to send the email, You can check the reason for that in your terminal")

        elif 'quit' in query:
            speak("Quitting, Thank You. See you soon")
            break
