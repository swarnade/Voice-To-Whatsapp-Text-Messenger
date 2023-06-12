import speech_recognition as s_r
import win32com.client
import pywhatkit


def text_speech(text):
    speaker=win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)
def speech_text():
    sp_recog=s_r.Recognizer()
    with s_r.Microphone() as sp_mic:
        sp_recog.pause_theshold =1
        audio=sp_recog.listen(sp_mic)
        try:
            final_text=sp_recog.recognize_google(audio, language="en-in")
            final_text.title()
            print(f"User:- {final_text}")
            return final_text
        except Exception as e:
            print("No Speech Recognised , Plzz Try Again")
            return "No Speech Recognised , Plzz Try Again"
def whatsapp_send(number,message):
    pywhatkit.sendwhatmsg_instantly(number,message,15 , True , 5)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
        print("Welcome To Swarnadeep Voice To Whatsapp Text Messanger")
        number = input("Enter Number:- ")
        print("Listening.......")
        text=speech_text()
        text_speech(text)
        whatsapp_send(number,text)
        print("Thanks For Using SWL Speech Recogniser")
        print("")


