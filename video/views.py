from datetime import datetime
from json import dumps, loads
import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from foundation.decorators import ticketable
from video import AUDIOFILES_DROP_FOLDER
from video.captions.subtitles_circuitAnime_basic import generateAudioFilePath_findEquation, generateAudioFilePath_solvingStep


def circuitAnimeRecord(request):
    if 'file' in request.FILES:
        uploaded_file = request.FILES['file'] # this is a InMemoryUploadedFile

        videoFilePath = os.path.join(settings.VIDEO_FOLDERPATH, uploaded_file.name)#, datetime.strftime(datetime.utcnow(), "%Y%M%d%H%M%S"))

        f = open(videoFilePath, 'wb')
        f.write(uploaded_file.read())
        f.close()
    return HttpResponse('', content_type="text/plain")


@ticketable
def basic_findEquations_audioFiles(request):
    """Inputs:
    list_equationNetworkInfoDict, textStr__textMeshUUID, nodeId__type, language_introduction_findEquations, language_conclusion_findEquations, folderpath

    Outputs:
    languages__subtitles, languages__subtitleIdx__dict_startTime_endTime, languages__filepath
    """
    folderpath = AUDIOFILES_DROP_FOLDER
    details = loads(request.body)
    subtitles, list_tuple_word_location_length_elapsedTime, filepath, pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime = generateAudioFilePath_findEquation(
        details['list_equationNetworkInfoDict'], 
        details['textStr__textMeshUUID'], 
        details['nodeId__type'], 
        details['language'],
        details['introduction_findEquations'], #>>>>>>>
        details['conclusion_findEquations'], #
        folderpath)
    #<<<<<<<<<<<<<<convert filepath to url friendly
    returnData = {
        'subtitles':subtitles,
        'list_tuple_word_location_length_elapsedTime':list_tuple_word_location_length_elapsedTime,
        'filename':os.path.basename(filepath),
        'pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime':pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime
    }
    return HttpResponse(dumps(returnData), content_type="text/plain")

@ticketable
def basic_solvingSteps_audioFiles(request):
    """Inputs:
    solvingSteps, language_introduction_solvingSteps, language_conclusion_solvingSteps, folderpath

    Outputs:
    languages__subtitles, languages__subtitleIdx__dict_startTime_endTime, languages__filepath
    """
    folderpath = AUDIOFILES_DROP_FOLDER
    details = loads(request.body)
    subtitles, list_tuple_word_location_length_elapsedTime, filepath, pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime = generateAudioFilePaths_solvingSteps(
        details['solvingSteps'], 
        details['language'],
        details['introduction_solvingSteps'], 
        details['conclusion_solvingSteps'], 
        folderpath)
    returnData = {
        'subtitles':subtitles,
        'list_tuple_word_location_length_elapsedTime':list_tuple_word_location_length_elapsedTime,
        'filename':os.path.basename(filepath),
        'pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime':pauseIdx__dict_startTime_endTime_listOfWordLocationLengthElapsedTime
    }
    return HttpResponse(dumps(returnData), content_type="text/plain")


def wavFiles(request):
    file = open(os.path.join(AUDIOFILES_DROP_FOLDER, request.POST['filename']), 'b')
    return HttpResponse(file.read(), content_type="application/octet-stream")