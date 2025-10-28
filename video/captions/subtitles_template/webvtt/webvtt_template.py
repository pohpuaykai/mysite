from copy import copy
from datetime import datetime
import os

from jinja2 import Environment, FileSystemLoader

class WebVTTGenerator:

    def __init__(self, list_dict_listSubtitleTimings_listSubtitles):
        self.templateInit()
        self.list_subtitleTimings, self.list_subtitles = self.inputInit(list_dict_listSubtitleTimings_listSubtitles)

    def inputInit(self, list_dict_listSubtitleTimings_listSubtitles):
        lastSnNumber = 0; touList_subtitleTimings = []; touList_subtitles = []; firstStartTime = None
        for dict_s in list_dict_listSubtitleTimings_listSubtitles:
            for subtitleItem in dict_s['list_subtitles']:
                touList_subtitles.append(subtitleItem.replace(os.linesep, '')) # subtitleItem is string.
            for subtitleTimingItem in dict_s['list_subtitleTimings']:
                subtitleTimingItem__new = copy(subtitleTimingItem)
                subtitleTimingItem__new['sn'] = subtitleTimingItem['sn'] + lastSnNumber
                if firstStartTime is None:
                    firstStartTime = self.javascriptTimeStamp__dtObj(subtitleTimingItem__new['startTime'])
                # import pdb;pdb.set_trace()
                print(subtitleTimingItem__new)
                #This should not happen... frontend is sending something wrong.........please check<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                if 'endTime' not in subtitleTimingItem__new:
                    continue
                #
                subtitleTimingItem__new['startTime'] = self.dtTimeDifferenceObj__WebVTTFormat(self.javascriptTimeStamp__dtObj(subtitleTimingItem__new['startTime']) - firstStartTime)
                subtitleTimingItem__new['endTime'] = self.dtTimeDifferenceObj__WebVTTFormat(self.javascriptTimeStamp__dtObj(subtitleTimingItem__new['endTime']) - firstStartTime)
                touList_subtitleTimings.append(subtitleTimingItem__new)
            lastSnNumber = len(dict_s['list_subtitleTimings'])
        return touList_subtitleTimings, touList_subtitles

    def templateInit(self):
        self.templateFilePath = os.path.join(os.path.dirname(__file__), 'webvtt_template.jinja2')
        import pprint
        pp = pprint.PrettyPrinter(indent=4)
        self.pformat = pp.pformat


    def generate(self):
        environment = Environment(loader=FileSystemLoader(os.path.dirname(self.templateFilePath)))# put in the full directory
        # environment.filters['formatJavascriptTimeStamp'] = self.formatJavascriptTimeStamp
        template = environment.get_template(os.path.basename(self.templateFilePath))
        renderedTemplate = template.render({
            'list_subtitleTimings':self.list_subtitleTimings,
            'list_subtitles':self.list_subtitles
        })
        return renderedTemplate


    def javascriptTimeStamp__dtObj(self, javascriptTimeStamp):
        # Convert milliseconds to seconds for datetime.fromtimestamp()
        timestamp_s = javascriptTimeStamp / 1000

        # Create a datetime object from the timestamp
        dt_object = datetime.fromtimestamp(timestamp_s)
        return dt_object

    # def dtObj__WebVTTFormat(self, dt_object):
    #     # Extract hours, minutes, seconds, and milliseconds
    #     hours = dt_object.hour
    #     minutes = dt_object.minute
    #     seconds = dt_object.second
    #     milliseconds = dt_object.microsecond // 1000  # Convert microseconds to milliseconds

    #     # Format the output string
    #     return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"

    def dtTimeDifferenceObj__WebVTTFormat(self, dtTimeDifferenceObj):
        hours = int(dtTimeDifferenceObj.total_seconds() / 3600)
        minutes = int(dtTimeDifferenceObj.total_seconds() / 60) - (hours * 60)
        seconds = int(dtTimeDifferenceObj.total_seconds()) - (hours * 60) - (minutes * 60)
        milliseconds = int((dtTimeDifferenceObj.total_seconds() - int(dtTimeDifferenceObj.total_seconds())) * 1000)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"
