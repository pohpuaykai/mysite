from datetime import datetime
from json import dumps, loads
import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

# from foundation.decorators import ticketable
from video import AUDIOFILES_DROP_FOLDER
# from video.captions.subtitles_circuitAnime_basic import generateAudioFilePath_findEquation, generateAudioFilePath_solvingStep
from video.captions.subtitles_circuitAnime_basic import SubtitlesCircuitAnimeBasic


def circuitAnimeRecord(request):#receives the recorded video
    if 'file' in request.FILES:
        uploaded_file = request.FILES['file'] # this is a InMemoryUploadedFile

        videoFilePath = os.path.join(settings.VIDEO_FOLDERPATH, uploaded_file.name)#, datetime.strftime(datetime.utcnow(), "%Y%M%d%H%M%S"))

        f = open(videoFilePath, 'wb')
        f.write(uploaded_file.read())
        f.close()
    return HttpResponse('', content_type="text/plain")


# @ticketable # no need, audio is already ticketable
def basic_findEquations_audioFiles(request):
    """Inputs:
    list_equationNetworkInfoDict, textStr__textMeshUUID, nodeId__type, language_introduction_findEquations, language_conclusion_findEquations, folderpath

    Outputs:
    languages__subtitles, languages__subtitleIdx__dict_startTime_endTime, languages__filepath
    """
    folderpath = AUDIOFILES_DROP_FOLDER
    details = loads(request.body)
    # subtitles, list_tuple_word_location_length_elapsedTime, filepath, pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime = 
    scab = SubtitlesCircuitAnimeBasic()
    ticketNumber = scab.generateEachAudioFilePath_findEquation(
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
    folderpath = AUDIOFILES_DROP_FOLDER
    # print(request.body)
    # import pdb;pdb.set_trace()
    details = loads(request.body)
    # subtitles, list_tuple_word_location_length_elapsedTime, filepath, pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime = 
    scab = SubtitlesCircuitAnimeBasic()
    #
    # import pprint;pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(details)
    # import pdb;pdb.set_trace()
    #
    ticketNumber = scab.generateEachAudioFilePath_solvingStep(
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
    filepath = os.path.join(AUDIOFILES_DROP_FOLDER, filename)
    print('wavFilepatH: ', filepath)
    file = open(filepath, 'rb')
    # return HttpResponse(file.read(), content_type="application/octet-stream")
    return HttpResponse(file.read(), content_type="audio/wav")