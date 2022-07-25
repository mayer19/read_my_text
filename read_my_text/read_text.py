import pyttsx3

#Iniciate Object
engine = pyttsx3.init()

#Define the speed
rate = engine.getProperty('rate')   # getting details of current speaking rate
#print (rate)                        #printing current voice rate
engine.setProperty('rate', 130) 

answer = ''
while True:
    try:
        text = input("Please write the text you want to ear: ")
        if text == 'n':
            print('Exiting program.')
            break
        else:
            engine.say(text)
            engine.runAndWait()
    except:
        print('Some error happend. Try again.')