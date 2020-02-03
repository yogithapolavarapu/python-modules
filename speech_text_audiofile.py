import speech_recognition as sr
r = sr.Recognizer()


harvard = sr.AudioFile('harvard.wav')


#jackhammer = sr.AudioFile('jackhammer.wav')
with harvard as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)

print(r.recognize_google(audio))