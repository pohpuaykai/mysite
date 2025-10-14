from datetime import datetime
import logging
import os
import time

class AudioFromText:

    # Silence all comtypes messages
    logging.getLogger("comtypes").setLevel(logging.CRITICAL)

    # Optionally, silence all pyttsx3 messages too
    logging.getLogger("pyttsx3").setLevel(logging.CRITICAL)
    # def __init__(self):
    #     pass

    languageTwoLetterCode__voiceId = {
        'en-US':2,
        'zh-CN':6,
        'ja-JP':4,
        'de-DE':1,
        'fr-FR':3,
        'ru-RU':5
    }

    @classmethod
    def convert(cls, language__list_subtitle, outputfolderpath, volume=0.1, rate=150, wavFileOutPrefix='basic_'):
        #just for getting voices
        from video.common.text2audio import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        #
        wavFileOutPrefix = f"{wavFileOutPrefix}_{datetime.strftime(datetime.utcnow(), '%Y%m%d%H%M%S')}"
        works = [] # this is for generating the timings
        language__list_tuple_subtitleStartPos_subtitleEndPos = {} # for marking pauses in subtitles
        for language, list_subtitle in language__list_subtitle.items():
            works.append({
                'text':os.linesep.join(list_subtitle), 
                'voice':voices[AudioFromText.languageTwoLetterCode__voiceId[language]].id, 
                'filename':f'{wavFileOutPrefix}{language[0:2]}.wav',
                'language':language
            })
            lastStartPos = 0; list_tuple_subtitleStartPos_subtitleEndPos = []
            for subtitle in list_subtitle:
                endPos = lastStartPos+len(subtitle)
                list_tuple_subtitleStartPos_subtitleEndPos.append((lastStartPos, endPos))
                lastStartPos = endPos
            language__list_tuple_subtitleStartPos_subtitleEndPos[language] = list_tuple_subtitleStartPos_subtitleEndPos
        #
        speakerOccupied = False
        workIdx = 0

        language__wavFilePath = {}
        language__list_tuple_word_location_length_elapsedTime = {}
        list_tuple_word_location_length_elapsedTime = []

        def recorder(word, location, length, elapsedTime):
            list_tuple_word_location_length_elapsedTime.append((word, location, length, elapsedTime))

        while workIdx < len(works):
            #init
            language = works[workIdx]['language']
            #
            
            #
            while speakerOccupied:
                time.sleep(1) # wait 1 second
            #
            #speaker not occupied anymore
            from video.common.text2audio import pyttsx3
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            now = time.time() # reference time
            #
            engine.setProperty('rate', rate)#You can adjust this value as needed
            engine.setProperty('volume', volume)#1.0 is maximum volume
            #
            #hooks and their attachment to engine
            def onStart(name):
                speakerOccupied = True
            def onWord(name, word, location, length):
                timeElapsed = time.time() - now
                recorder = name['recorder']
                recorder(word, location, length, timeElapsed)
                
            def onEnd(name, completed):#name is idx
                _idx = name['idx']
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
            wavFilePath = os.path.join(outputfolderpath, works['filename'])
            engine.save_to_file(work['text'], wavFilePath)
            language__wavFilePath[language] = wavFilePath
            if workIdx >= len(works)-1:
                #engine.proxy.endLoop(False) # this ends the pumping
                engine.proxy._push(engine.endLoop, ())
            
            engine.runAndWait() # has to call this every idx else, package will not wait for .Speech to finish? 
            #
            
            #
            engine.disconnect({'topic':'started-utterance', 'cb':onStart})
            engine.disconnect({'topic':'started-word', 'cb':onWord}) # Note: 'word' event might not be supported by all drivers
            engine.disconnect({'topic':'finished-utterance', 'cb':onEnd})
            engine.disconnect({'topic':'error', 'cb':onError})
            workIdx += 1
            #
            language__list_tuple_word_location_length_elapsedTime[language] = list_tuple_word_location_length_elapsedTime
            list_tuple_word_location_length_elapsedTime = []
            #
        #reconstruct the subtitles_with_timings from the list_tuple_word_location_length_elapsedTime
        language__pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime = {}
        for language, list_tuple_word_location_length_elapsedTime in language__list_tuple_word_location_length_elapsedTime.items():
            list_tuple_subtitleStartPos_subtitleEndPos = language__list_tuple_subtitleStartPos_subtitleEndPos[language]; pauseIdx = 0;
            pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime = {}
            for word, location, length, elapsedTime in list_tuple_word_location_length_elapsedTime:
                subtitleStartPos, subtitleEndPos = list_tuple_subtitleStartPos_subtitleEndPos[pauseIdx]
                if not(substitleStartPos <= location and location+length <= subtitleEndPos):
                    pauseIdx += 1
                    subtitleStartPos, subtitleEndPos = list_tuple_subtitleStartPos_subtitleEndPos[pauseIdx]
                dict_startTime_endTime_listOfWordLocationLengthElapsedTime = pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime.get(pauseIdx, {
                    'startTime':elapsedTime,
                    'endTime':elapsedTime,
                    'listOfWordLocationLengthElapsedTime':[]
                })
                dict_startTime_endTime_listOfWordLocationLengthElapsedTime['endTime'] = elapsedTime
                dict_startTime_endTime_listOfWordLocationLengthElapsedTime['listOfWordLocationLengthElapsedTime'].append((word, location, length, elapsedTime))
                pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime[pauseIdx] = dict_startTime_endTime_listOfWordLocationLengthElapsedTime
            language__pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime[language] = pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime
        return language__list_tuple_word_location_length_elapsedTime, language__wavFilePath, language__pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime