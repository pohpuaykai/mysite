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

list2 = [   
                 'La variable en couleur est liée à ce Piles AA, numéro '
                 "d'identité 8.",
                 'Nous avons trouvé toutes les équations relatives à ses '
                 'composants.']

text2 = '\n'.join(list2)

list3 = [   
                 'その8番号の電気部品のアルカリ乾電池で、強調した未知数は作れました。',
                 '今まで、その並列回路の素子においての公式を、求めました。']

text3 = '\n'.join(list3)

list4 = [   
                 'Этот аккумуляторов с идентификационным номером 8 создает эту '
                 'выделенную переменную.',
                 'Мы нашли все уравнения, касающиеся его компонентов.']

text4 = '\n'.join(list4)

list5 = [   
                 '我们可以从8编号的电池取得标注的变数。',
                 '现阶段，我们以求获所有相关的方程式。']

text5 = '\n'.join(list5)

#import pyttsx3
from video.common.text2audio import pyttsx3
import time

engine = pyttsx3.init()
voices = engine.getProperty('voices') # only to get the voices to get the mapping

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
    },
    {
        'text':text2,
        'voice':voices[3].id,
        'filep':'fr'
    },
    {
        'text':text3,
        'voice':voices[4].id,
        'filep':'jp'
    },
    {
        'text':text4,
        'voice':voices[5].id,
        'filep':'ru'
    },
    {
        'text':text5,
        'voice':voices[6].id,
        'filep':'zh'
    }
]
#breakEveryTiming = 1.0#[for splitting subtitles]might need to be customised according to language, or situation... but we hardcode this for now
speakerOccupied = False
workIdx = 0

languages__list_tuple_word_location_length_elapsedTime = {}
list_tuple_word_location_length_elapsedTime = []

def recorder(word, location, length, elapsedTime):
    list_tuple_word_location_length_elapsedTime.append((word, location, length, elapsedTime))

while workIdx < len(works):
    #init
    language = works[workIdx]['filep']
    #languages__list_tuple_word_location_length_elapsedTime[language] = []
    #
    
    #
    while speakerOccupied:
        #print('speakerOccupied')
        time.sleep(1) # wait 1 second
    #
    #speaker not occupied anymore
    from video.common.text2audio import pyttsx3
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    now = time.time() # reference time
    #
    engine.setProperty('rate', 150)#You can adjust this value as needed
    engine.setProperty('volume', 0.1)#1.0 is maximum volume
    #
    #hooks and their attachment to engine
    def onStart(name):
        #print('Starting:', name, '(', time.time() - now,')')
        speakerOccupied = True
    def onWord(name, word, location, length):
        timeElapsed = time.time() - now
        recorder = name['recorder']
        #print('Word:', word, location, length, '(', timeElapsed,')', name)#move doen 1 instruction, still work?
        recorder(word, location, length, timeElapsed)
        #print('onWord', 'list_tuple_word_location_length_elapsedTime', list_tuple_word_location_length_elapsedTime)
        
    def onEnd(name, completed):#name is idx
        #print('running End, name:', '_inLoop', engine._inLoop, '_isBusy', engine.proxy._busy, '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        #print(name) 
        _idx = name['idx']
        #print('onEnd, _idx: ', _idx)
        #print('Finishing:', name, completed, '(', time.time() - now,')', '_inLoop', engine._inLoop, '_isBusy', engine.proxy._busy)
        speakerOccupied = False
    def onError(e):
        print(e)
    engine.connect('started-utterance', onStart)
    engine.connect('started-word', onWord) # Note: 'word' event might not be supported by all drivers
    engine.connect('finished-utterance', onEnd)
    engine.connect('error', onError)
    #
    work = works[workIdx]
    engine.setProperty('voice', work['voice'])
    engine.say(work['text'], name={'idx':workIdx, 'recorder':recorder})
    engine.save_to_file(work['text'], 'D:\\textToSpeech\\withHooks\\'+work['filep']+'.wav')
    if workIdx >= len(works)-1:
        #engine.proxy.endLoop(False) # this ends the pumping
        engine.proxy._push(engine.endLoop, ())
    
    engine.runAndWait() # has to call this every idx else, package will not wait for .Speech to finish? 
    #runNext({'idx':workIdx, 'recorder':recorder})
    #
    
    #
    engine.disconnect({'topic':'started-utterance', 'cb':onStart})
    engine.disconnect({'topic':'started-word', 'cb':onWord}) # Note: 'word' event might not be supported by all drivers
    engine.disconnect({'topic':'finished-utterance', 'cb':onEnd})
    engine.disconnect({'topic':'error', 'cb':onError})
    workIdx += 1
    #
    languages__list_tuple_word_location_length_elapsedTime[language] = list_tuple_word_location_length_elapsedTime
    list_tuple_word_location_length_elapsedTime = []
    #




print('languages__list_tuple_word_location_length_elapsedTime', '************************')
import pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(languages__list_tuple_word_location_length_elapsedTime)

#text already grouped by animation, so group by text to get position to pause for animation synchronization
#actually you should do the front end first and then see what format suits the front end the best