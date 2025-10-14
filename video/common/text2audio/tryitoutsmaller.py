list0 = [   
                 'The highlighted variable is associated with this battery, '
                 'identity number 8.',
                 'We have found all the equations relating to the two '
                 'resistors and their parallel connectivity.']

text0 = '\n'.join(list0)

list1 = [   
                 'Die hervorgehobene Variabel ist mit diesem Akku, '
                 'Identitätsnummer 8 verknüpft.',
                 'Wir haben alle Gleichungen der Bauelemente dieses '
                 'Stromkreises gefunden,']

text1 = '\n'.join(list1)

#import pyttsx3
from video.common.text2audio import pyttsx3
import time




engine = pyttsx3.init()

voices = engine.getProperty('voices')
#import pprint; pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(list(map(lambda voice: (voice.languages, voice.age, voice.gender, voice.name, voice.id), voices)))
#import pdb;pdb.set_trace()

works = [
    {
        'text':text0,
        'voice':voices[2].id,
        'filep':'en'
    },
    {
        'text':text1,
        'voice':voices[1].id,
        'filep':'de'
    }
]



now = time.time()

def onStart(name):
    print('Starting:', name, '(', time.time() - now,')')


def onWord(name, location, length):
    pass
    #print('Word:', name, location, length, '(', time.time() - now,')', '_inLoop', engine._inLoop, '_isBusy', engine.proxy._busy)

def runNext(d):#can you do the same for per sentence? <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    
    #print('setting engine._inLoop = False')
    #engine._inLoop = False # still does not call in _pump
    #engine._driver.setBusy(False)#
    
    print('in runNext', '_inLoop', engine._inLoop, '_isBusy', engine.proxy._busy)
    idx = d['idx']
    print('runNext, idx: ', idx)
    if idx >= len(works):
        print('returning from runNext***********&^^^^^^^^ idx: ', idx, len(works))
        return
    if idx >0:
        print('setting engine._inLoop = False')
        engine._inLoop = False # this causes the .Speech(1) to run, but then stops pumping after that
    print('runNext idx', idx, '_inLoop', engine._inLoop, '_isBusy', engine.proxy._busy)
    work = works[idx]
    print('got works', '_inLoop', engine._inLoop, '_isBusy', engine.proxy._busy)
    engine.setProperty('voice', work['voice']) # english
    print('setting voice', '_inLoop', engine._inLoop, '_isBusy', engine.proxy._busy)
    print(work['filep'], 'setProperty-voice-@@@@queue:', list(map(lambda command: (command[0], command[2]), engine.proxy._queue)))
    #engine.say(work['text'], name=str(idx))
    engine.say(work['text'], name=d)
    print('said', '_inLoop', engine._inLoop, '_isBusy', engine.proxy._busy)
    print(work['filep'], 'say@@@@queue:', list(map(lambda command: (command[0], command[2]), engine.proxy._queue)))
    #turn this on, but slot it at the back
    #engine.save_to_file(work['text'], 'D:\\textToSpeech\\withHooks\\'+work['filep']+'.wav') # you might need to play everything first then do the save_to_file NOPE comment it out does not fire finish_play_event
    #print('save_to_file', '_inLoop', engine._inLoop, '_isBusy', engine.proxy._busy)
    #print(work['filep'], '@@@@queue:', list(map(lambda command: (command[0], command[2]), engine.proxy._queue)))
    
    #print(engine.proxy._queue)
    #engine.runAndWait()
    #print('runAndWait', '_inLoop', engine._inLoop, '_isBusy', engine.proxy._busy)
    #print(work['filep'], '@@@@queue:', list(map(lambda command: (command[0], command[2]), engine.proxy._queue)))
    print('idx >= len(works)-1', idx >= len(works)-1, '}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}');
    if idx >= len(works)-1:
        print('calling endLoop^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        #engine.proxy.endLoop(False) # this ends the pumping
        engine.proxy._push(engine.endLoop, ())
    print('queue:', list(map(lambda command: (command[0], command[2]), engine.proxy._queue)))
    #elif idx == 0:
    print('calling runAndWait^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    #if idx == 0:
    engine.runAndWait() # has to call this every idx else, package will not wait for .Speech to finish? 
    #engine.proxy._driver.endLoop()
    


def onEnd(name, completed):#name is idx
    #_runNext(int(name))
    print('running End, name:', '_inLoop', engine._inLoop, '_isBusy', engine.proxy._busy, '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print(name) 
    _idx = name['idx']
    _runNext = name['runNext'];
    print('onEnd, _idx: ', _idx)
    #import pdb;pdb.set_trace()
    #if _idx+1 >= len(works):
    #    engine.proxy.endLoop()
    #    print('returning because overshot****************************')
    #    return
    _runNext({'idx':_idx+1, 'runNext':_runNext})
    print('Finishing:', name, completed, '(', time.time() - now,')', '_inLoop', engine._inLoop, '_isBusy', engine.proxy._busy)


engine.setProperty('rate', 150)#You can adjust this value as needed
engine.setProperty('volume', 0.1)#1.0 is maximum volume


def onError(e):
    print(e)

# Connect callback functions to events
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord) # Note: 'word' event might not be supported by all drivers
engine.connect('finished-utterance', onEnd)
engine.connect('error', onError)

runNext({'idx':0, 'runNext':runNext})
#engine.setProperty('voice', voices[2].id) # english
#engine.setProperty('voice', voices[6].id) # chinese


#
#engine.say("Hello, world! This is a test of pyttsx3 event hooks.", name='0')
#

#
#engine.say("Hello, world!", name='0')
#engine.say("This is a test of pyttsx3 event hooks.", name='1')
#

#engine.save_to_file("Hello, world! This is a test of pyttsx3 event hooks.", 'D:\\withHooks\\tryme.wav')

#engine.say(text0, name='0')

#for name, line in enumerate(list0):#does not work, because the audio will not wait until the next one is done... but can be rewritten, but for now, we will just do string matching...
#    engine.say(line, name=name)
#    engine.runAndWait()

#engine.save_to_file(text0, 'D:\\textToSpeech\\withHooks\\en.wav')
#print(engine.proxy._queue)
#import pdb;pdb.set_trace()
#engine.runAndWait()
#engine.runAndWait()





#engine.say(text1, name='1')

#for name, line in enumerate(list0):#does not work, because the audio will not wait until the next one is done... but can be rewritten, but for now, we will just do string matching...
#    engine.say(line, name=name)
#    engine.runAndWait()

#engine.setProperty('voice', voices[6].id) # chinese
#engine.save_to_file(text1, 'D:\\textToSpeech\\withHooks\\zh.wav')
#completed = False
#print(engine.proxy._queue)
#import pdb;pdb.set_trace()
#engine.runAndWait()