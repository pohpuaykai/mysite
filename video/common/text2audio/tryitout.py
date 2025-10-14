list0 = [   'This is a circuit with two resistors connected in parallel, '
                 'lets find all the equations related to the components of '
                 'this circuit',
                 'With these circuit elements and Kirchhoff Current Law, we '
                 'can get this formula:',
                 'The highlighted variable is associated with this battery, '
                 'identity number 8.',
                 'The highlighted variable comes from this resistor, with '
                 'identity number 0.',
                 'This resistor, with identity number 3, produces this '
                 'highlighted variable.',
                 'With these circuit elements and Kirchhoff Voltage Law, we '
                 'can get this formula:',
                 'The highlighted variable is associated with this resistor, '
                 'identity number 0.',
                 'The highlighted variable is associated with this battery, '
                 'identity number 8.',
                 'The following formula is derived from Kirchhoff Voltage Law, '
                 'based on these circuit elements:',
                 'The highlighted variable comes from this battery, with '
                 'identity number 8.',
                 'This resistor, with identity number 3, produces this '
                 'highlighted variable.',
                 'Using Ohm Law on these circuit elements, we obtain the '
                 'following formula:',
                 'The highlighted variable comes from this resistor, with '
                 'identity number 0.',
                 'This resistor, with identity number 0, produces this '
                 'highlighted variable.',
                 'The highlighted variable comes from this resistor, with '
                 'identity number 0.',
                 'Using Ohm Law on these circuit elements, we obtain the '
                 'following formula:',
                 'The highlighted variable comes from this resistor, with '
                 'identity number 3.',
                 'This resistor, with identity number 3, produces this '
                 'highlighted variable.',
                 'This resistor, with identity number 3, produces this '
                 'highlighted variable.',
                 'Using Ohm Law on these circuit elements, we obtain the '
                 'following formula:',
                 'This battery, with identity number 8, produces this '
                 'highlighted variable.',
                 'The highlighted variable is associated with this battery, '
                 'identity number 8.',
                 'The highlighted variable is associated with this battery, '
                 'identity number 8.',
                 'We have found all the equations relating to the two '
                 'resistors and their parallel connectivity.']

text0 = '\n'.join(list0)

list1 = [   'Der folgende Stromkreis ist eine ParallelSchaltung. '
                 'Versuchen wir jetzt, alle Gleichungen der Bauelemente dieses '
                 'Stromkreises aufzuschreiben',
                 'Die folgende Formel wird aus Regel von KIRCHHOFF: '
                 'Knotenregel abgeleitet, basierend auf diesen Bauelementen:',
                 'Die hervorgehobene Variabel ist mit diesem Akku, '
                 'Identitätsnummer 8 verknüpft.',
                 'Die hervorgehobene Variabel stammt von diesem Widerstand mit '
                 'der Identitätsnummer 0.',
                 'Dieser Widerstand mit der Identitätsnummer 3 erzeugt diese '
                 'hervorgehobene Variabel.',
                 'Die folgende Formel wird aus Regel von KIRCHHOFF: '
                 'Maschenregel abgeleitet, basierend auf diesen Bauelementen:',
                 'Die hervorgehobene Variabel stammt von diesem Widerstand mit '
                 'der Identitätsnummer 0.',
                 'Dieser Akku mit der Identitätsnummer 8 erzeugt diese '
                 'hervorgehobene Variabel.',
                 'Die folgende Formel wird aus Regel von KIRCHHOFF: '
                 'Maschenregel abgeleitet, basierend auf diesen Bauelementen:',
                 'Dieser Akku mit der Identitätsnummer 8 erzeugt diese '
                 'hervorgehobene Variabel.',
                 'Dieser Widerstand mit der Identitätsnummer 3 erzeugt diese '
                 'hervorgehobene Variabel.',
                 'Mit diesen Bauelementen und Ohmsches Gesetz können wir diese '
                 'Formel erhalten:',
                 'Die hervorgehobene Variabel stammt von diesem Widerstand mit '
                 'der Identitätsnummer 0.',
                 'Die hervorgehobene Variabel ist mit diesem Widerstand, '
                 'Identitätsnummer 0 verknüpft.',
                 'Die hervorgehobene Variabel stammt von diesem Widerstand mit '
                 'der Identitätsnummer 0.',
                 'Die folgende Formel wird aus Ohmsches Gesetz abgeleitet, '
                 'basierend auf diesen Bauelementen:',
                 'Die hervorgehobene Variabel stammt von diesem Widerstand mit '
                 'der Identitätsnummer 3.',
                 'Dieser Widerstand mit der Identitätsnummer 3 erzeugt diese '
                 'hervorgehobene Variabel.',
                 'Dieser Widerstand mit der Identitätsnummer 3 erzeugt diese '
                 'hervorgehobene Variabel.',
                 'Die folgende Formel wird aus Ohmsches Gesetz abgeleitet, '
                 'basierend auf diesen Bauelementen:',
                 'Die hervorgehobene Variabel ist mit diesem Akku, '
                 'Identitätsnummer 8 verknüpft.',
                 'Die hervorgehobene Variabel stammt von diesem Akku mit der '
                 'Identitätsnummer 8.',
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
    engine.save_to_file(work['text'], 'D:\\textToSpeech\\withHooks\\'+work['filep']+'.wav')
    print('save_to_file', '_inLoop', engine._inLoop, '_isBusy', engine.proxy._busy)
    print(work['filep'], '@@@@queue:', list(map(lambda command: (command[0], command[2]), engine.proxy._queue)))
    #print(engine.proxy._queue)
    #engine.runAndWait()
    #print('runAndWait', '_inLoop', engine._inLoop, '_isBusy', engine.proxy._busy)
    #print(work['filep'], '@@@@queue:', list(map(lambda command: (command[0], command[2]), engine.proxy._queue)))
    print('idx >= len(works)-1', idx >= len(works)-1, '}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}');
    #if idx >= len(works)-1:
    #    print('calling endLoop^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        #engine.proxy.endLoop(False) # this ends the pumping
    engine.proxy._push(engine.endLoop, ())
    print('queue:', list(map(lambda command: (command[0], command[2]), engine.proxy._queue)))
    #elif idx == 0:
    print('calling runAndWait^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    #if idx == 0:
    engine.runAndWait() # has to call this every idx else, package will not wait for .Speech to finish? 
    engine.proxy._driver.endLoop()
    


def onEnd(name, completed):#name is idx
    #_runNext(int(name))
    print('running End, name:', '_inLoop', engine._inLoop, '_isBusy', engine.proxy._busy)
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