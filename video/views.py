from datetime import datetime
# from json import dumps, loads
import json
import os
# from pickle import loads
import pickle

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

# from foundation.decorators import ticketable
# from video.captions.subtitles_circuitAnime_basic import generateAudioFilePath_findEquation, generateAudioFilePath_solvingStep
from video.captions.subtitles_circuitAnime_basic import SubtitlesCircuitAnimeBasic
from video.captions.subtitles_template.webvtt.webvtt_template import WebVTTGenerator
from video.models import Audio


def subtitlesTimingRecord(request):
    details = json.loads(request.body)
    # print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    # print(details['list_subtitles_findEquations'])
    # print(details['list_subtitles_solveEquations'])
    # print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')#and also how to transform it to WebVTT format


    def getListSubtitlesBYTag(language, tag):
        audio = Audio.objects.filter(tag=tag).first() # this cannot be None
        return pickle.loads(audio.data)['language__list_subtitle'][language]

    language = details['language']
    list_subtitles_findEquations = getListSubtitlesBYTag(language, details['tag__getAudioUrls_findEquations'])#contains the text of the subtitles
    list_subtitles_solveEquations = getListSubtitlesBYTag(language, details['tag__getAudioUrls_solveEquations'])#contains the text of the subtitles
    
    webVTTGen = WebVTTGenerator([
        {
            'list_subtitleTimings':details['list_subtitles_findEquations'],
            'list_subtitles':list_subtitles_findEquations
        },
        {
            'list_subtitleTimings':details['list_subtitles_solveEquations'],
            'list_subtitles':list_subtitles_solveEquations
        }
    ])
    subtitleFileContent = webVTTGen.generate()

    #need to merge the content together<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    filename = datetime.strftime(datetime.utcnow(), f'basic_{details["circuitName"]}_%Y%m%d%H%M%S.vtt')
    videoSubtitlesPath = os.path.join(settings.VIDEO_SUBTITLES_FOLDERPATH, filename)
    f = open(videoSubtitlesPath, 'w', encoding='utf-8')
    f.write(subtitleFileContent)
    f.close()
    # print('video Subtitle is here: ', videoSubtitlesPath, '*****************************************************')
    #please check what you can do with this.... TODO
    return HttpResponse('', content_type="text/plain")


def circuitAnimeRecord(request):#receives the recorded video
    storageMethod = 'django'#<<<<<<<<<<<<refactor
    if 'file' in request.FILES:

        if storageMethod == 'plain':
            uploaded_file = request.FILES['file'] # this is a InMemoryUploadedFile

            videoFilePath = os.path.join(settings.VIDEO_FOLDERPATH, uploaded_file.name)#, datetime.strftime(datetime.utcnow(), "%Y%M%d%H%M%S"))

            f = open(videoFilePath, 'wb')
            f.write(uploaded_file.read())
            f.close()
        elif storageMethod == 'django':#hopeflly this does not crash
            from django.core.files.storage import FileSystemStorage
            uploaded_file = request.FILES['file'] # this is a InMemoryUploadedFile

            # videoFilePath = os.path.join(settings.VIDEO_FOLDERPATH, uploaded_file.name)#, datetime.strftime(datetime.utcnow(), "%Y%M%d%H%M%S"))

            fs = FileSystemStorage(location=settings.VIDEO_FOLDERPATH)
            filename = fs.save(uploaded_file.name, uploaded_file)
    return HttpResponse('', content_type="text/plain")


# @ticketable # no need, audio is already ticketable
def basic_findEquations_audioFiles(request):
    """Inputs:
    list_equationNetworkInfoDict, textStr__textMeshUUID, nodeId__type, language_introduction_findEquations, language_conclusion_findEquations, folderpath

    Outputs:
    languages__subtitles, languages__subtitleIdx__dict_startTime_endTime, languages__filepath
    """
    folderpath = settings.AUDIOFILES_DROP_FOLDER
    details = json.loads(request.body)
    # subtitles, list_tuple_word_location_length_elapsedTime, filepath, pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime = 
    #####
    # print('details:')
    # print(details)
    # import pdb;pdb.set_trace()
    #####
    scab = SubtitlesCircuitAnimeBasic()
    ticketNumber = scab.generateEachAudioFilePath_findEquation(
        details['circuitName'],
        details['list_equationNetworkInfoDict'], 
        details['textStr__textMeshUUID'], 
        details['id__type'], 
        details['language'],
        details['introduction_findEquations'], #>>>>>>>
        details['conclusion_findEquations'], #
        folderpath)
    #<<<<<<<<<<<<<<convert filepath to url friendly
    # returnData = {
    #     'subtitles':subtitles,
    #     'list_tuple_word_location_length_elapsedTime':list_tuple_word_location_length_elapsedTime,
    #     'filename':os.path.basename(filepath),
    #     'pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime':pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime
    # }
    # return HttpResponse(dumps(returnData), content_type="text/plain")
    return HttpResponse(str(ticketNumber), content_type="text/plain")

# @ticketable # no need, audio is already ticketable
def basic_solvingSteps_audioFiles(request):
    """Inputs:
    solvingSteps, language_introduction_solvingSteps, language_conclusion_solvingSteps, folderpath

    Outputs:
    languages__subtitles, languages__subtitleIdx__dict_startTime_endTime, languages__filepath
    """
    folderpath = settings.AUDIOFILES_DROP_FOLDER
    # print(request.body)
    # import pdb;pdb.set_trace()
    details = json.loads(request.body)
    # print(details)
    # import pdb;pdb.set_trace()
    # subtitles, list_tuple_word_location_length_elapsedTime, filepath, pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime = 
    scab = SubtitlesCircuitAnimeBasic()
    #
    import pprint;pp = pprint.PrettyPrinter(indent=4)
    print('))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
    pp.pprint(details)
    print('))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))')
    # import pdb;pdb.set_trace()
    #
    ticketNumber = scab.generateEachAudioFilePath_solvingStep(
        details['circuitName'],
        details['solvingSteps'], 
        details['runningStepsIdx__branchedStepsIdx'], 
        details['language'],
        details['introduction_solvingSteps'], 
        details['conclusion_solvingSteps'], 
        folderpath)
    # returnData = {
    #     'subtitles':subtitles,
    #     'list_tuple_word_location_length_elapsedTime':list_tuple_word_location_length_elapsedTime,
    #     'filename':os.path.basename(filepath),
    #     'pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime':pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime
    # }
    # return HttpResponse(dumps(returnData), content_type="text/plain")
    return HttpResponse(str(ticketNumber), content_type="text/plain")


def wavFiles(request):
    filename = request.POST.get('filename')
    print('obtainingwav filename: ', filename)
    filepath = os.path.join(settings.AUDIOFILES_DROP_FOLDER, filename)
    print('wavFilepatH: ', filepath)
    file = open(filepath, 'rb')
    # return HttpResponse(file.read(), content_type="application/octet-stream")
    return HttpResponse(file.read(), content_type="audio/wav")