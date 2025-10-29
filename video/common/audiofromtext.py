import base64
from datetime import datetime
import logging
import os
import pickle
import time

from video.common.parallelisationmanager import ThreadingManager, parallelise
from video.models import Audio

@ThreadingManager(maximum_number_of_running_threads=1, waitingPollingTimeInSeconds=6, saveRequestInDatabase=True, storageType='json') # only allow 1 thread, because we only have 1 speaker
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

    @parallelise
    def convert(self, circuitName, language__list_subtitle, outputfolderpath, volume=0.1, rate=150, wavFileOutPrefix='basic_', useOld=True):
        """
        If we have the same wavFileOutPrefix, then we give back the same return.....<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        """

        #just for getting voices
        from video.common.text2audio import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        #
        theWavFileOutPrefix = wavFileOutPrefix
        wavFileOutPrefix = f"{wavFileOutPrefix}_{datetime.strftime(datetime.utcnow(), '%Y%m%d%H%M%S')}"
        works = [] # this is for generating the timings
        language__list_tuple_subtitleStartPos_subtitleEndPos = {} # for marking pauses in subtitles
        language__existingData = {}
        for language, list_subtitle in language__list_subtitle.items():
            if useOld:
                # print(0)
                tag = f'{theWavFileOutPrefix}{language}'
                oldAudioData = self.getFirstOldAudioByTag(tag)
                if oldAudioData is not None:
                    # print(1)
                    language__existingData[language] = oldAudioData
                    list_tuple_subtitleStartPos_subtitleEndPos = oldAudioData['list_tuple_subtitleStartPos_subtitleEndPos']
                    wavFilePath = oldAudioData['wavFilePath']
                else:
                    wavFilePath = f'{wavFileOutPrefix}{language[0:2]}.wav'
            else:
                wavFilePath = f'{wavFileOutPrefix}{language[0:2]}.wav'
            works.append({
                'text':os.linesep.join(list_subtitle), #
                'voice':voices[AudioFromText.languageTwoLetterCode__voiceId[language]].id, 
                'filename':wavFilePath,
                'language':language
            })
            #skip if useOld
            if not useOld or language not in language__existingData:
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
        language__endTime = {}#endTime is the end of the whole audio
        list_tuple_word_location_length_elapsedTime = []

        def recorder(word, location, length, elapsedTime):
            list_tuple_word_location_length_elapsedTime.append((word, location, length, elapsedTime))

        while workIdx < len(works):
            language = works[workIdx]['language']
            if useOld and language in language__existingData:
                # print(3)
                # data = json.loads(works[workIdx]['exist'])
                oldAudioData = language__existingData[language]
                language__wavFilePath[language] = oldAudioData['wavFilePath']
                language__list_tuple_word_location_length_elapsedTime[language] = oldAudioData['list_tuple_word_location_length_elapsedTime']
                
                if workIdx >= len(works)-1:
                    break
                workIdx+=1

                continue
            #init
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

            #for now we will use defaults
            rate = {
                'en-US':150,
                'zh-CN':150,
                'ja-JP':120, # this is too fast for the minWaitTime for pauseUntilCallback on frontend?????<<<<<<<<<
                'de-DE':150,
                'fr-FR':150,
                'ru-RU':150
            }.get(language, rate)
            print('rate:', rate, 'language')
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
                language__endTime[language] = time.time() - now
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
            # print('work^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
            # print(work)
            # import pdb;pdb.set_trace()
            wavFilePath = os.path.join(outputfolderpath, work['filename'])
            engine.save_to_file(work['text'], wavFilePath)
            # language__wavFilePath[language] = wavFilePath
            language__wavFilePath[language] = os.path.basename(wavFilePath)
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
            returnedOld = False
            if useOld and language in language__existingData:
                existingData = language__existingData[language]
                language__list_tuple_word_location_length_elapsedTime[language] = existingData['list_tuple_word_location_length_elapsedTime']
                language__wavFilePath[language] = existingData['wavFilePath']
                language__pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime[language] = existingData['pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime']
                returnedOld = True
                continue
            list_tuple_subtitleStartPos_subtitleEndPos = language__list_tuple_subtitleStartPos_subtitleEndPos[language]; pauseIdx = 0;
            # import pdb;pdb.set_trace()
            pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime = {}; perLineOffset = len(os.linesep)
            for idx, (word, location, length, elapsedTime) in enumerate(list_tuple_word_location_length_elapsedTime):
                subtitleStartPos, subtitleEndPos = list_tuple_subtitleStartPos_subtitleEndPos[pauseIdx]
                # print('subtitleStartPos, subtitleEndPos', subtitleStartPos, subtitleEndPos)
                # print('pauseIdx: ', pauseIdx, 'len(list_tuple_subtitleStartPos_subtitleEndPos)', len(list_tuple_subtitleStartPos_subtitleEndPos))
                # print('location', location, 'length:', length)
                # print('******************************************************************')
                if not(subtitleStartPos <= location-(pauseIdx* perLineOffset) and location+length-(pauseIdx* perLineOffset) <= subtitleEndPos):
                    #the first of each pauseIdx, we use this to set the last of the previous pauseIdx
                    pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime[pauseIdx]['endTime'] = elapsedTime #elapsedTime is the startTime
                    #
                    pauseIdx += 1
                    if pauseIdx < len(list_tuple_subtitleStartPos_subtitleEndPos):
                        subtitleStartPos, subtitleEndPos = list_tuple_subtitleStartPos_subtitleEndPos[pauseIdx]
                dict_startTime_endTime_listOfWordLocationLengthElapsedTime = pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime.get(pauseIdx, {
                    'startTime':elapsedTime,
                    'endTime':elapsedTime,
                    'listOfWordLocationLengthElapsedTime':[]
                })
                # if pauseIdx >= len(list_tuple_subtitleStartPos_subtitleEndPos):
                #     import pdb;pdb.set_trace()
                dict_startTime_endTime_listOfWordLocationLengthElapsedTime['endTime'] = elapsedTime#should take the next's first?
                dict_startTime_endTime_listOfWordLocationLengthElapsedTime['listOfWordLocationLengthElapsedTime'].append((word, location, length, elapsedTime))
                pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime[pauseIdx] = dict_startTime_endTime_listOfWordLocationLengthElapsedTime
                # print(pauseIdx);
                # print(pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime)
                # import pdb;pdb.set_trace()
            #we use this to set the last to the endTime of the audio
            pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime[len(pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime)-1]['endTime'] = language__endTime[language]
            #
            language__pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime[language] = pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime
            if useOld and not returnedOld:
                data = {
                    'list_tuple_subtitleStartPos_subtitleEndPos':list_tuple_subtitleStartPos_subtitleEndPos,
                    'list_tuple_word_location_length_elapsedTime':list_tuple_word_location_length_elapsedTime,
                    'wavFilePath':language__wavFilePath[language],
                    'pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime':language__pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime[language]
                }
                self.storeByTag(tag, data)
        return {
            'language__list_tuple_word_location_length_elapsedTime':language__list_tuple_word_location_length_elapsedTime,
            'language__wavFilePath':language__wavFilePath,
            'language__pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime':language__pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime
        }

        # return language__list_tuple_word_location_length_elapsedTime, language__wavFilePath, language__pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime

    @parallelise
    def convertEachSentenceItsOwnWav(self, circuitName, language__list_subtitle, outputfolderpath, volume=0.1, rate=150, wavFileOutPrefix='basic_', useOld=True):
        from pathlib import Path
        print(circuitName)
        wavFileOutPrefix = f'{wavFileOutPrefix}_{circuitName}_{"_".join(sorted(language__list_subtitle.keys()))}'
        if useOld:
            print('useOld! tag: ', wavFileOutPrefix)
            data = self.getFirstOldAudioByTag(wavFileOutPrefix)
            if data is not None:
                print('returning OLD AUDIO!')
                # return data['language__filepaths']
                return data
            print('generating new AUDIO!')
        from video.common.text2audio import pyttsx3
        print('starting pyttsx3 engine')
        engine = pyttsx3.init()
        print('inited pyttsx3 engine')
        voices = engine.getProperty('voices')
        print('got pyttsx3 voices')
        #
        engine.setProperty('rate', rate)#You can adjust this value as needed
        print('set pyttsx3 rate')
        engine.setProperty('volume', volume)#1.0 is maximum volume
        print('set pyttsx3 volume')
        #
        returnedOld = False
        wavFileOutPrefixN = f"{wavFileOutPrefix}_{datetime.strftime(datetime.utcnow(), '%Y%m%d%H%M%S')}"
        print('wavFileOutPrefixN: ', wavFileOutPrefixN)
        language__filepaths = {}
        for language, list_subtitle in language__list_subtitle.items():
            print('language>>>>>>>>>>>>>>>>>', language)
            voice = voices[AudioFromText.languageTwoLetterCode__voiceId[language]].id
            #create a new folder for each language
            newOutputFolderpath = os.path.join(outputfolderpath, f'{wavFileOutPrefixN}_{language}')
            if not os.path.isdir(newOutputFolderpath):
                os.makedirs(newOutputFolderpath)
            #
            filepaths = []
            for subtitleIdx, subtitle in enumerate(list_subtitle):
                print('setting voice')
                engine.setProperty('voice', voice)
                print('setted voice')
                # engine.say(subtitle)#if i don't want the word-by-word timing, should i still need to say it? or will engine.save_to_file suffisant?
                wavFilePath = os.path.join(newOutputFolderpath, f'{subtitleIdx}.wav')
                engine.save_to_file(subtitle, wavFilePath)
                #cut out the last last 2 parts from wavFilePath
                pathObj = Path(wavFilePath)
                filepaths.append(os.path.join(*pathObj.parts[-2:]))
                #
            #
            engine.proxy._push(engine.endLoop, ()) # add the terminating job
            engine.runAndWait()
                # language__wavFilePath[language] = wavFilePath
                # language__wavFilePath[language] = os.path.basename(wavFilePath)
            language__filepaths[language] = filepaths
        if useOld and not returnedOld:
            self.storeByTag(wavFileOutPrefix, {
                'language__filepaths':language__filepaths, 
                'language__list_subtitle':language__list_subtitle,
                'tag':wavFileOutPrefix
            })
        return {'language__filepaths':language__filepaths, 'tag':wavFileOutPrefix}


    def getFirstOldAudioByTag(self, tag):
        oldAudios = Audio.objects.filter(tag=tag)
        audio = oldAudios.first()
        if audio:
            return pickle.loads(audio.data)
        return None

    def storeByTag(self, tag, data):

        audio = Audio.objects.create(tag=tag, data=pickle.dumps(data))
        audio.save()