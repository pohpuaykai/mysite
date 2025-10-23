import weakref

from .engine import Engine

_activeEngines = weakref.WeakValueDictionary()


def init(driverName=None, debug=False):
    """
    Constructs a new TTS engine instance or reuses the existing instance for
    the driver name.

    @param driverName: Name of the platform specific driver to use. If
        None, selects the default driver for the operating system.
    @type: str
    @param debug: Debugging output enabled or not
    @type debug: bool
    @return: Engine instance
    @rtype: L{engine.Engine}
    """
    try:
        # print('startINIT, _activeEngines: ', dict(_activeEngines))
        eng = _activeEngines[driverName]
        # print('completed INIT')
    except KeyError:
        #
        # import traceback; traceback.print_exc()
        #
        eng = Engine(driverName, debug)
        _activeEngines[driverName] = eng
    return eng


def speak(text) -> None:
    engine = init()
    engine.say(text)
    engine.runAndWait()
