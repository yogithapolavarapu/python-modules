import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone(device_index=1)
#print(sr.Microphone.list_microphone_names())

print("speak")
with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

print("wait")
try:
    print(r.recognize_google(audio))
except:
    print("sorry i cant understand")