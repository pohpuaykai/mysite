from datetime import datetime
import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


def circuitAnimeRecord(request):
    if 'file' in request.FILES:
        uploaded_file = request.FILES['file'] # this is a InMemoryUploadedFile

        videoFilePath = os.path.join(settings.VIDEO_FOLDERPATH, uploaded_file.name)#, datetime.strftime(datetime.utcnow(), "%Y%M%d%H%M%S"))

        f = open(videoFilePath, 'wb')
        f.write(uploaded_file.read())
        f.close()
    return HttpResponse('', content_type="text/plain")