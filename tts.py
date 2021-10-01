''' Sources
https://www.geeksforgeeks.org/convert-text-speech-python/
https://towardsdatascience.com/easy-text-to-speech-with-python-bfb34250036e
'''

from gtts import gTTS
import os

language = "en"

# WORK IN PROGRESS QUESTIONS
def ask_question(question):
    try:
        os.remove("question.mp3")
    except:
        print("no file yet to remove")
    speech = gTTS(text = question, lang = language, slow = False)
    speech.save("question.mp3")
    os.system("start question.mp3")
