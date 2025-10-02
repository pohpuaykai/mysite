

def generateSubtitles_findEquations(list_equationLatexStr, dependentVarStr, list_independentVarStr, introductions, conclusions):
    """

    """
    

    return



def generateSubtitles_solvingSteps(solvingSteps, introductions, conclusions):
    """
    Because front end might do some processing to the animationData from the backend, to generate the right audio, we have to take the data directly from the frontend to generate subtitles.

    """

    for solvingStep in solvingSteps:
        pass

    return 

def generateAudioFromText(text):
    import pyttsx3

    #Initialise the text-to-speech engine
    engine = pyttsx3.init()

    #Provide the text you want to convert to speech
    #text = "This is an animated circuit with 2 resistors connected in parallel."
    text = ""

    #Events and callbacks<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#more here: https://pyttsx3.readthedocs.io/en/latest/engine.html
    def onStart(name):
        print("Speech started for:"+name)
        
    def onEnd(name, completed):
        print("Speech ended for:"+name+", completed:"+str(completed))
        
    engine.connect('started-utterance', onStart)
    engine.connect('finished-utterance', onEnd)
    #Events and callbacks<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


    #Set the rate (words per minute)
    engine.setProperty('rate', 150)#You can adjust this value as needed

    #Set the volume (0.0 to 1.0)
    engine.setProperty('volume', 1.0)#1.0 is maximum volume

    #Get the list of available voices
    voices = engine.getProperty('voices')

    #
    """
    [   {   'age': 'Adult',
            'gender': 'Male',
            'id': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0',
            'languages': ['en-US'],
            'name': 'Microsoft David Desktop - English (United States)'},
        {   'age': 'Adult',
            'gender': 'Female',
            'id': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_DE-DE_HEDDA_11.0',
            'languages': ['de-DE'],
            'name': 'Microsoft Hedda Desktop - German'},
        {   'age': 'Adult',
            'gender': 'Female',
            'id': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0',
            'languages': ['en-US'],
            'name': 'Microsoft Zira Desktop - English (United States)'},
        {   'age': 'Adult',
            'gender': 'Female',
            'id': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_FR-FR_HORTENSE_11.0',
            'languages': ['fr-FR'],
            'name': 'Microsoft Hortense Desktop - French'},
        {   'age': 'Adult',
            'gender': 'Female',
            'id': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_JA-JP_HARUKA_11.0',
            'languages': ['ja-JP'],
            'name': 'Microsoft Haruka Desktop - Japanese'},
        {   'age': 'Adult',
            'gender': 'Female',
            'id': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_RU-RU_IRINA_11.0',
            'languages': ['ru-RU'],
            'name': 'Microsoft Irina Desktop - Russian'},
        {   'age': 'Adult',
            'gender': 'Female',
            'id': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ZH-CN_HUIHUI_11.0',
            'languages': ['zh-CN'],
            'name': 'Microsoft Huihui Desktop - Chinese (Simplified)'},
        {   'age': 'Adult',
            'gender': 'Female',
            'id': 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ZH-TW_HANHAN_11.0',
            'languages': ['zh-TW'],
            'name': 'Microsoft Hanhan Desktop - Chinese (Taiwan)'}]
    """
    #import pprint; pp = pprint.PrettyPrinter(indent=4)
    #pp.pprint(list(map(lambda o: {'age':o.age, 'gender':o.gender, 'id':o.id, 'languages':o.languages, 'name':o.name}, voices)))
    #

    #Select a voice
    engine.setProperty('voice', voices[2].id) # You can change the index as needed # 2 is default


    #Convert text to speech
    engine.say(text)

    #save_to_file
    #engine.save_to_file(text, "output.mp3")

    #Play the converted speech
    engine.runAndWait()