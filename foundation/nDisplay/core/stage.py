from copy import deepcopy
import math
import sys

import glfw
import glfw.GLFW as GLFW_CONSTANTS
#import pygame as pg
#import pygame.locals as pl
import OpenGL.GL as gl
import OpenGL.GLU as glu

from foundation.nDisplay import NDISPLAY_MODULE_DIR
from foundation.nDisplay.common import convertToPyArray
from foundation.nDisplay.controlsMapping import KEYBOARD_3D_DISPLAY_CONTROLS as KBCM

#TODO more Geometric shapes that components need
#TODO shining Geometric shapes to mimic flow of current : http://jerome.jouvie.free.fr/opengl-tutorials/Tutorial9.php

class Stage:

    def __init__(self, width, height, piece, metronome, displayCaption, fieldOfView, zNear, zFar, verbose):
        """
        :param width: width of the viewport (screen of the program)
        :type width: float
        :param height: height of the viewport (screen of the program)
        :type height: float

        :param piece: like the script of a movie or the score of a orchestration. Instructions for where to put piece,
        how they move, etc...
        :type piece: Callable

        :param metronome: frames-per-second
        :type metronome: float
        :param displayCaption: title of the screen
        :type displayCaption: str

        :param fieldOfView:
        This is the wideness of the Frustrum - the width of the whole stage

        For more information see here:
        https://registry.khronos.org/OpenGL-Refpages/gl2.1/xhtml/gluPerspective.xml
        -here is one with a diagram of a view frustum:
        https://www.songho.ca/opengl/gl_transform.html#example1

        0 to 360

        :type fieldOfView: float
        :param zNear: distance from most forefront of the stage to the eye. front of the stage. first clipping plane
        :type zNear: float
        :param zFar: distance from most backend of the stage to the eye. back of the stage. last clipping plane
        :type zFar: float
        :param verbose: show i display all processing?
        :type verbose: bool
        """
        self.width = width
        self.height = height
        self.piece = piece
        self.metronome = metronome
        self.displayCaption = displayCaption
        self.fieldOfView = fieldOfView
        self.zNear = zNear
        self.zFar = zFar
        self.verbose = verbose
        self.resetted = False
        self.resetting = False
        self._initScene()
        self.window = self._initGLFW(self.width, self.height)
        #setup input system
        self._keys = {} # key pressed to bool
        glfw.set_key_callback(self.window, self._keyCallback)
        # Sets the mouse button callback
        mouseNames = list(filter(lambda k: 'glfw_mouse' in k.lower(), dir(GLFW_CONSTANTS)))
        self._cursorPos = (0, 0)
        self._mouseButtonsPos = dict(map(lambda mouseName: (mouseName, {}), mouseNames)) # mouseButtons to UP_or_DOWN to tuple(x, y) that is the mouse_position
        self._mouseButtonsState = {}
        glfw.set_mouse_button_callback(self.window, self._mouseCallback)
        self._action()

    def _initScene(self):
        #pg.init()
        self._displayInit()

    def _initGLFW(self, SCREEN_WIDTH, SCREEN_HEIGHT): #for clock, mouse, keyboard
        """
        Courtesy of Andrew of www.youtube.com/@GetIntoGameDev
        """

        glfw.init()
        glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(GLFW_CONSTANTS.GLFW_CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(
            GLFW_CONSTANTS.GLFW_OPENGL_PROFILE, 
            GLFW_CONSTANTS.GLFW_OPENGL_CORE_PROFILE, 
        )
        glfw.window_hint(
            GLFW_CONSTANTS.GLFW_OPENGL_FORWARD_COMPAT, 
            GLFW_CONSTANTS.GLFW_TRUE, 
        )
        glfw.window_hint(GLFW_CONSTANTS.GLFW_DOUBLEBUFFER, GL_FALSE) # frame rate limiting not sure what is that
        
        window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, "My Game", None, None) #first None is the monitor, second None, programs showing resources with
        if not window: # https://pypi.org/project/glfw/
            glfw.terminate()
            return
        glfw.make_context_current(window)
        #glfw.set_input_mode(
        #    window,
        #    GLFW_CONSTANTS.GLFW_CURSOR, 
        #    GLFW_CONSTANTS.GLFW_CURSOR_HIDDEN
        #)
        return window

    def _displayInit(self):
        #pg.display.set_mode((self.width, self.height), pg.DOUBLEBUF|pg.OPENGL)
        #pg.display.set_caption(self.displayCaption)
        self.aspectRatio = float(self.width)/float(self.height)
        gl.glMatrixMode(gl.GL_MODELVIEW)
        gl.glLoadIdentity() # remove accumulated transformations
        glu.gluPerspective(
            self.fieldOfView,
            self.aspectRatio,
            self.zNear,
            self.zFar
        )
        gl.glTranslatef(0.0, 0.0, -5) # initial zoom out... TODO configurable/ calculated to give 'BEST initial VIEW of the stage'

    def _mouseCallback(self, window, button, action, mods):
        """
        Input args = https://www.glfw.org/docs/3.3/group__input.html#ga0184dcb59f6d85d735503dcaae809727

        :param window:
        The window that received the event
        :type window:
        :param button:
        The mouse button that was pressed or released
        :type button:
        :param action:
        One of GLFW_PRESS or GLFW_RELEASE. Future releases may add more actions
        :type action:
        :param mods:
        Bit field describing which modifier keys were held down
        https://www.glfw.org/docs/3.3/group__mods.html
        Like SHIFT, CONTROL, ALT
        :type mods:
        """
        state = False
        match action:
            case GLFW_CONSTANTS.GLFW_PRESS:
                state = True
            case GLFW_CONSTANTS.GLFW_RELEASE:
                state = True
            case _:
                return
        self._mouseButtonsState[key] = state
        self._mouseButtonsPos[key][action] = glfw.get_cursor_pos(self.window)
        

    def _mouseHandler(self):
        """
        All other unmapped buttons can be found here:
        list(filter(lambda k: 'mouse' in k.lower(), dir(GLFW_CONSTANTS)))

        NOTICE there is no mouseMotion like in pygame
        looking into https://github.com/pygame/pygame to see how pg.MOUSEMOTION was implemented
        """
        #DRAG should only work WHEN mouseButton is down
        if self._mouseButtonsState.get(GLFW_CONSTANTS.GLFW_MOUSE_BUTTON_LEFT, False) and \
            self._mouseButtonsPos[GLFW_CONSTANTS.GLFW_MOUSE_BUTTON_LEFT][GLFW_CONSTANTS.GLFW_PRESS] and \
            self._mouseButtonsPos[GLFW_CONSTANTS.GLFW_MOUSE_BUTTON_LEFT][GLFW_CONSTANTS.GLFW_RELEASE]:
            rel = self._mouseButtonsPos
            #TODO formulas should be configurable.... on a seperate configurable... file?
            # actually just a magnitude, user can adjust sensitivity 
            #math.atan(abs(rel[1])/abs(rel[0])) if rel[0] != 0.0 else 0 
            def angleF(): #TODO UI can be improved, vertical drag up and horizontal drag up a little weird...
                if rel[0] == 0.0 and rel[1] == 0.0:
                    return 0
                elif rel[0] == 0.0:
                    return 1.0/(KBCM['screen_out_sensitivity']+abs(rel[0]/rel[1]))
                else:
                    return 1.0/(KBCM['screen_out_sensitivity']+abs(rel[1]/rel[0]))
            xSign = abs(rel[0])/rel[0] if rel[0] != 0.0 else 1
            ySign = abs(rel[1])/rel[1] if rel[1] != 0.0 else 1
            zSign = abs(rel[0] * rel[1]) / (rel[0] * rel[1]) if rel[0] != 0.0 and rel[1] != 0.0 else 0# could also be 0 if rel[0] == 0.0 or rel[1] == 0.0 else xSign*ySign, depends on the processor, does 'or/==' cost more than multiply? (does logical operators cost more than arithmetic operators (processor specific configurations?)?)
            originVecVerViewPort = self.getPrickVerViewPort() # TODO needs to change this
            gl.glRotatef(angleF(), ySign*originVecVerViewPort[0], xSign*originVecVerViewPort[1], zSign*originVecVerViewPort[2])
            if self.verbose:
                print(rel, angleF(), xSign, ySign, zSign)



    def _keyCallback(self, window, key, scancode, action, mods):
        """ INIT
        Input args = https://www.glfw.org/docs/3.3/group__input.html#ga0184dcb59f6d85d735503dcaae809727

        :param window:
        The window that received the event.
        :type window:
        :param key:
        The keyboard key that was pressed or released
        :type key: 
        :param scancode:
        The system-specific scancode of the key
        :type scancode:
        :param action:
        GLFW_PRESS, GLFW_RELEASE, GLFW_REPEAT. Future releases may add more actions
        :type action:
        :param mods:
        Bit field describing which modifier keys were held down
        https://www.glfw.org/docs/3.3/group__mods.html
        Like SHIFT, CONTROL, ALT
        :type mods:
        """
        state = False
        match action:
            case GLFW_CONSTANTS.GLFW_PRESS:
                state = True
            case GLFW_CONSTANTS.GLFW_RELEASE:
                state = False
            case _:
                return
        self._keys[key] = state


    def _keysHandler(self):
        """RENDER
        r - right
        l - left
        u - up
        d - down
        i - in
        o - out

        r,l,u,d,i,o
        2^6 = 64
        00 000000 
        01 00000o o
        02 0000i0 i
        03 0000io 
        04 000d00 d
        05 000d0o do
        06 000di0 di
        07 000dio d
        08 00u000 u
        09 00u00o uo
        10 00u0i0 ui
        11 00u0io u
        12 00ud00 
        13 00ud0o o
        14 00udi0 i
        15 00udio 
        16 0l0000 l
        17 0l000o lo
        18 0l00i0 li
        19 0l00io l
        20 0l0d00 ld
        21 0l0d0o ldo
        22 0l0di0 ldi
        23 0l0dio ld
        24 0lu000 lu
        25 0lu00o luo
        26 0lu0i0 lui
        27 0lu0io lu
        28 0lud00 l
        29 0lud0o lo
        30 0ludi0 li
        31 0ludio l
        32 r00000 r
        33 r0000o ro
        34 r000i0 ri
        35 r000io r
        36 r00d00 rd
        37 r00d0o rdo
        38 r00di0 rdi
        39 r00dio rd
        40 r0u000 ru
        41 r0u00o ruo
        42 r0u0i0 rui
        43 r0u0io ru
        44 r0ud00 r
        45 r0ud0o ro
        46 r0udi0 ri
        47 r0udio r
        48 rl0000 
        49 rl000o o
        50 rl00i0 i
        51 rl00io 
        52 rl0d00 d
        53 rl0d0o do
        54 rl0di0 di
        55 rl0dio d
        56 rlu000 u
        57 rlu00o uo
        58 rlu0i0 ui
        59 rlu0io u
        60 rlud00 
        61 rlud0o o
        62 rludi0 i
        63 rludio 

        perspective change, moving camera instead of object
        """
        xMove = 0
        yMove = 0
        zMove = 0
        if self._keys.get(KBCM['screen_down']):
            #xMove -= KBCM['screen_left_sensitivity']
            #xMove += KBCM['screen_right_sensitivity']
            #yMove -= KBCM['screen_out_sensitivity']
            #yMove += KBCM['screen_in_sensitivity']
            zMove -= KBCM['screen_down_sensitivity']
            #zMove += KBCM['screen_up_sensitivity']
        elif self._keys.get(KBCM['screen_down']) and self._keys.get(KBCM['screen_in']):
            #xMove -= KBCM['screen_left_sensitivity']
            #xMove += KBCM['screen_right_sensitivity']
            #yMove -= KBCM['screen_out_sensitivity']
            yMove += KBCM['screen_in_sensitivity']
            zMove -= KBCM['screen_down_sensitivity']
            #zMove += KBCM['screen_up_sensitivity']
        elif self._keys.get(KBCM['screen_down']) and self._keys.get(KBCM['screen_out']):
            #xMove -= KBCM['screen_left_sensitivity']
            #xMove += KBCM['screen_right_sensitivity']
            yMove -= KBCM['screen_out_sensitivity']
            #yMove += KBCM['screen_in_sensitivity']
            zMove -= KBCM['screen_down_sensitivity']
            #zMove += KBCM['screen_up_sensitivity']
        elif self._keys.get(KBCM['screen_in']):
            #xMove -= KBCM['screen_left_sensitivity']
            #xMove += KBCM['screen_right_sensitivity']
            #yMove -= KBCM['screen_out_sensitivity']
            yMove += KBCM['screen_in_sensitivity']
            #zMove -= KBCM['screen_down_sensitivity']
            #zMove += KBCM['screen_up_sensitivity']
        elif self._keys.get(KBCM['screen_left']):
            xMove -= KBCM['screen_left_sensitivity']
            #xMove += KBCM['screen_right_sensitivity']
            #yMove -= KBCM['screen_out_sensitivity']
            #yMove += KBCM['screen_in_sensitivity']
            #zMove -= KBCM['screen_down_sensitivity']
            #zMove += KBCM['screen_up_sensitivity']
        elif self._keys.get(KBCM['screen_left']) and self._keys.get(KBCM['screen_down']):
            xMove -= KBCM['screen_left_sensitivity']
            #xMove += KBCM['screen_right_sensitivity']
            #yMove -= KBCM['screen_out_sensitivity']
            #yMove += KBCM['screen_in_sensitivity']
            zMove -= KBCM['screen_down_sensitivity']
            #zMove += KBCM['screen_up_sensitivity']
        elif self._keys.get(KBCM['screen_left']) and self._keys.get(KBCM['screen_down']) and self._keys.get(KBCM['screen_in']):
            xMove -= KBCM['screen_left_sensitivity']
            #xMove += KBCM['screen_right_sensitivity']
            #yMove -= KBCM['screen_out_sensitivity']
            yMove += KBCM['screen_in_sensitivity']
            zMove -= KBCM['screen_down_sensitivity']
            #zMove += KBCM['screen_up_sensitivity']
        elif self._keys.get(KBCM['screen_left']) and self._keys.get(KBCM['screen_down']) and self._keys.get(KBCM['screen_out']):
            xMove -= KBCM['screen_left_sensitivity']
            #xMove += KBCM['screen_right_sensitivity']
            yMove -= KBCM['screen_out_sensitivity']
            #yMove += KBCM['screen_in_sensitivity']
            zMove -= KBCM['screen_down_sensitivity']
            #zMove += KBCM['screen_up_sensitivity']
        elif self._keys.get(KBCM['screen_left']) and self._keys.get(KBCM['screen_in']):
            xMove -= KBCM['screen_left_sensitivity']
            #xMove += KBCM['screen_right_sensitivity']
            #yMove -= KBCM['screen_out_sensitivity']
            yMove += KBCM['screen_in_sensitivity']
            #zMove -= KBCM['screen_down_sensitivity']
            #zMove += KBCM['screen_up_sensitivity']
        elif self._keys.get(KBCM['screen_left']) and self._keys.get(KBCM['screen_out']):
            xMove -= KBCM['screen_left_sensitivity']
            #xMove += KBCM['screen_right_sensitivity']
            yMove -= KBCM['screen_out_sensitivity']
            #yMove += KBCM['screen_in_sensitivity']
            #zMove -= KBCM['screen_down_sensitivity']
            #zMove += KBCM['screen_up_sensitivity']
        elif self._keys.get(KBCM['screen_left']) and self._keys.get(KBCM['screen_up']):
            xMove -= KBCM['screen_left_sensitivity']
            #xMove += KBCM['screen_right_sensitivity']
            #yMove -= KBCM['screen_out_sensitivity']
            #yMove += KBCM['screen_in_sensitivity']
            #zMove -= KBCM['screen_down_sensitivity']
            zMove += KBCM['screen_up_sensitivity']
        elif self._keys.get(KBCM['screen_left']) and self._keys.get(KBCM['screen_up']) and self._keys.get(KBCM['screen_in']):
            xMove -= KBCM['screen_left_sensitivity']
            #xMove += KBCM['screen_right_sensitivity']
            #yMove -= KBCM['screen_out_sensitivity']
            yMove += KBCM['screen_in_sensitivity']
            #zMove -= KBCM['screen_down_sensitivity']
            zMove += KBCM['screen_up_sensitivity']
        elif self._keys.get(KBCM['screen_left']) and self._keys.get(KBCM['screen_up']) and self._keys.get(KBCM['screen_out']):
            xMove -= KBCM['screen_left_sensitivity']
            #xMove += KBCM['screen_right_sensitivity']
            yMove -= KBCM['screen_out_sensitivity']
            #yMove += KBCM['screen_in_sensitivity']
            #zMove -= KBCM['screen_down_sensitivity']
            zMove += KBCM['screen_up_sensitivity']
        elif self._keys.get(KBCM['screen_out']):
            #xMove -= KBCM['screen_left_sensitivity']
            #xMove += KBCM['screen_right_sensitivity']
            yMove -= KBCM['screen_out_sensitivity']
            #yMove += KBCM['screen_in_sensitivity']
            #zMove -= KBCM['screen_down_sensitivity']
            #zMove += KBCM['screen_up_sensitivity']
        elif self._keys.get(KBCM['screen_right']):
            #xMove -= KBCM['screen_left_sensitivity']
            xMove += KBCM['screen_right_sensitivity']
            #yMove -= KBCM['screen_out_sensitivity']
            #yMove += KBCM['screen_in_sensitivity']
            #zMove -= KBCM['screen_down_sensitivity']
            #zMove += KBCM['screen_up_sensitivity']
        elif self._keys.get(KBCM['screen_right']) and self._keys.get(KBCM['screen_down']):
            #xMove -= KBCM['screen_left_sensitivity']
            xMove += KBCM['screen_right_sensitivity']
            #yMove -= KBCM['screen_out_sensitivity']
            #yMove += KBCM['screen_in_sensitivity']
            zMove -= KBCM['screen_down_sensitivity']
            #zMove += KBCM['screen_up_sensitivity']
        elif self._keys.get(KBCM['screen_right']) and self._keys.get(KBCM['screen_down']) and self._keys.get(KBCM['screen_in']):
            #xMove -= KBCM['screen_left_sensitivity']
            xMove += KBCM['screen_right_sensitivity']
            #yMove -= KBCM['screen_out_sensitivity']
            yMove += KBCM['screen_in_sensitivity']
            zMove -= KBCM['screen_down_sensitivity']
            #zMove += KBCM['screen_up_sensitivity']
        elif self._keys.get(KBCM['screen_right']) and self._keys.get(KBCM['screen_down']) and self._keys.get(KBCM['screen_out']):
            #xMove -= KBCM['screen_left_sensitivity']
            xMove += KBCM['screen_right_sensitivity']
            yMove -= KBCM['screen_out_sensitivity']
            #yMove += KBCM['screen_in_sensitivity']
            zMove -= KBCM['screen_down_sensitivity']
            #zMove += KBCM['screen_up_sensitivity']
        elif self._keys.get(KBCM['screen_right']) and self._keys.get(KBCM['screen_in']):
            #xMove -= KBCM['screen_left_sensitivity']
            xMove += KBCM['screen_right_sensitivity']
            #yMove -= KBCM['screen_out_sensitivity']
            yMove += KBCM['screen_in_sensitivity']
            #zMove -= KBCM['screen_down_sensitivity']
            #zMove += KBCM['screen_up_sensitivity']
        elif self._keys.get(KBCM['screen_right']) and self._keys.get(KBCM['screen_out']):
            #xMove -= KBCM['screen_left_sensitivity']
            xMove += KBCM['screen_right_sensitivity']
            yMove -= KBCM['screen_out_sensitivity']
            #yMove += KBCM['screen_in_sensitivity']
            #zMove -= KBCM['screen_down_sensitivity']
            #zMove += KBCM['screen_up_sensitivity']
        elif self._keys.get(KBCM['screen_right']) and self._keys.get(KBCM['screen_up']):
            #xMove -= KBCM['screen_left_sensitivity']
            xMove += KBCM['screen_right_sensitivity']
            #yMove -= KBCM['screen_out_sensitivity']
            y#Move += KBCM['screen_in_sensitivity']
            zM#ove -= KBCM['screen_down_sensitivity']
            zMove += KBCM['screen_up_sensitivity']
        elif self._keys.get(KBCM['screen_right']) and self._keys.get(KBCM['screen_up']) and self._keys.get(KBCM['screen_in']):
            #xMove -= KBCM['screen_left_sensitivity']
            xMove += KBCM['screen_right_sensitivity']
            #yMove -= KBCM['screen_out_sensitivity']
            yMove += KBCM['screen_in_sensitivity']
            #zMove -= KBCM['screen_down_sensitivity']
            zMove += KBCM['screen_up_sensitivity']
        elif self._keys.get(KBCM['screen_right']) and self._keys.get(KBCM['screen_up']) and self._keys.get(KBCM['screen_out']):
            #xMove -= KBCM['screen_left_sensitivity']
            xMove += KBCM['screen_right_sensitivity']
            yMove -= KBCM['screen_out_sensitivity']
            #yMove += KBCM['screen_in_sensitivity']
            #zMove -= KBCM['screen_down_sensitivity']
            zMove += KBCM['screen_up_sensitivity']
        elif self._keys.get(KBCM['screen_up']):
            #xMove -= KBCM['screen_left_sensitivity']
            #xMove += KBCM['screen_right_sensitivity']
            #yMove -= KBCM['screen_out_sensitivity']
            #yMove += KBCM['screen_in_sensitivity']
            #zMove -= KBCM['screen_down_sensitivity']
            zMove += KBCM['screen_up_sensitivity']
        elif self._keys.get(KBCM['screen_up']) and self._keys.get(KBCM['screen_in']):
            #xMove -= KBCM['screen_left_sensitivity']
            #xMove += KBCM['screen_right_sensitivity']
            #yMove -= KBCM['screen_out_sensitivity']
            yMove += KBCM['screen_in_sensitivity']#
            #zMove -= KBCM['screen_down_sensitivity']
            zMove += KBCM['screen_up_sensitivity']#
        elif self._keys.get(KBCM['screen_up']) and self._keys.get(KBCM['screen_out']):
            #xMove -= KBCM['screen_left_sensitivity']
            #xMove += KBCM['screen_right_sensitivity']
            yMove -= KBCM['screen_out_sensitivity']#
            #yMove += KBCM['screen_in_sensitivity']
            #zMove -= KBCM['screen_down_sensitivity']
            zMove += KBCM['screen_up_sensitivity']#
        #else: #keys cancel out.... 
        #TODO handle reset key:
        ## screen related
        # if event.key == KBCM['actor_reset']: #TODO this does not work, not sure why
        #     self.resetting = True
        #     if self.verbose:
        #         print('actor reset')



    def _action(self):
        """
        ACTION! starts the scene rolling.

        

        :param piece:
        :type piece:
        :param metronome:
        :type metronome:
        :param verbose:
        :type verbose:

        event: function that runs continuously, dictating what happens on the screen
        metronome: 1/fps (frame per second)
        """

        #https://pypi.org/project/glfw/
        while not glfw.window_should_close(window) \
            or glfw.get_key(self.window, GLFW_CONSTANTS.GLFW_KEY_ESCAPE) == GLFW_CONSTANTS.GLFW_PRESS:
            self.handleKeys()
            self.handleMouse()
            glfw.poll_events()
            self.piece()


        # clock = pg.time.Clock()
        # running = True
        # while running:
        #     for event in pg.event.get():
        #         #quit event handling
        #         if event.type == pg.QUIT:
        #             running = False
        #         #
        #         self._mouseHandler(event)
        #         self._keyboardHandler(event)
        #     if self.resetting:
        #         #STENCIL is used for storing pixel data coming from reflection of light
        #         gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT) # GL_ACCUM_BUFFER_BIT GL_STENCIL_BUFFER_BIT
        #         self._displayInit()
        #         self.resetting = False
        #         if self.verbose:
        #             print('resetted............')
        #         self.resetted = True
        #     else:
        #         if not self.resetted:
        #             gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT) # cannot call glClear while pg.display.init
        #         else:
        #             self.resetted = False
        #             if self.verbose:
        #                 print('unresetted..............')
        #         self.piece()
        #         pg.display.flip()
        #     clock.tick(self.metronome)#pg.time.wait(metronome)
        # pg.quit()
        # sys.exit() # comes with clean-up from 'finally' # https://www.geeksforgeeks.org/python-exit-commands-quit-exit-sys-exit-and-os-_exit/
        #os.exit(os.EX_OK) # sub-pub for multithreading/processing, wait for other thread/process to finish

    def _mouseHandler(self, event):
        """

        :param event:
        :type event:
        """
        if event.type == pg.MOUSEBUTTONDOWN:
            self.mouseDownPos = pg.mouse.get_pos()
            self.mouseDown = True
            if self.verbose:
                print(self.mouseDownPos, "FIRST mouse button down")
                self.printModelProjView()
        if event.type == pg.MOUSEBUTTONUP:
            self.mouseDown = False
            if self.verbose:
                print(self.mouseDown, "mouse button up")
        if self.mouseDown and event.type == pg.MOUSEMOTION:
            rel = pg.mouse.get_rel()
            btn = pg.mouse
            #TODO formulas should be configurable.... on a seperate configurable... file?
            # actually just a magnitude, user can adjust sensitivity 
            #math.atan(abs(rel[1])/abs(rel[0])) if rel[0] != 0.0 else 0 
            def angleF(): #TODO UI can be improved, vertical drag up and horizontal drag up a little weird...
                if rel[0] == 0.0 and rel[1] == 0.0:
                    return 0
                elif rel[0] == 0.0:
                    return 1.0/(KBCM['screen_out_sensitivity']+abs(rel[0]/rel[1]))
                else:
                    return 1.0/(KBCM['screen_out_sensitivity']+abs(rel[1]/rel[0]))
            xSign = abs(rel[0])/rel[0] if rel[0] != 0.0 else 1
            ySign = abs(rel[1])/rel[1] if rel[1] != 0.0 else 1
            zSign = abs(rel[0] * rel[1]) / (rel[0] * rel[1]) if rel[0] != 0.0 and rel[1] != 0.0 else 0# could also be 0 if rel[0] == 0.0 or rel[1] == 0.0 else xSign*ySign, depends on the processor, does 'or/==' cost more than multiply? (does logical operators cost more than arithmetic operators (processor specific configurations?)?)
            originVecVerViewPort = self.getPrickVerViewPort() # model view
            gl.glRotatef(angleF(), ySign*originVecVerViewPort[0], xSign*originVecVerViewPort[1], zSign*originVecVerViewPort[2])
            if self.verbose:
                print(rel, angleF(), xSign, ySign, zSign)

    # def _keyboardHandler(self, event):
    #     """also handle 
    #     screen_left & screen_right
    #     screen_left & screen_up
    #     ...
        
    #     :param event:
    #     :type event:
    #     """

    #     if event.type == pg.KEYDOWN:
    #         ## screen related
    #         if event.key == KBCM['screen_left']:
    #             gl.glTranslatef(-KBCM['screen_left_sensitivity'], 0, 0)
    #             if self.verbose:
    #                 print("left")
    #         if event.key == KBCM['screen_right']:
    #             gl.glTranslatef(KBCM['screen_right_sensitivity'], 0, 0)
    #             if self.verbose:
    #                 print("right")
    #         if event.key == KBCM['screen_up']:
    #             gl.glTranslatef(0, KBCM['screen_up_sensitivity'], 0)
    #             if self.verbose:
    #                 print("up")
    #         if event.key == KBCM['screen_down']:
    #             gl.glTranslatef(0, -KBCM['screen_down_sensitivity'], 0)
    #             if self.verbose:
    #                 print("down")
    #         if event.key == KBCM['screen_in']:
    #             gl.glTranslatef(0, 0, KBCM['screen_in_sensitivity'])
    #             if self.verbose:
    #                 print("in")
    #         if event.key == KBCM['screen_out']:
    #             gl.glTranslatef(0, 0, -KBCM['screen_out_sensitivity'])
    #             if self.verbose:
    #                 print("out")
    #         ## screen related
    #         if event.key == KBCM['actor_reset']: #TODO this does not work, not sure why
    #             self.resetting = True
    #             if self.verbose:
    #                 print('actor reset')

    #GETTERS of stage
    def getPythonicModelViewMatrix(self):
        """
        
        """
        model = gl.glGetDoublev(gl.GL_MODELVIEW_MATRIX)
        return convertToPyArray(deepcopy(model))


    def getPythonicProjectionMatrix(self):
        """

        """
        proj = gl.glGetDoublev(gl.GL_PROJECTION_MATRIX)
        return convertToPyArray(deepcopy(proj))

    def getPythonicViewport(self):
        """

        """
        view = gl.glGetDoublev(gl.GL_VIEWPORT)
        return convertToPyArray(deepcopy(view))


    def getPrickVerViewPort(self):
        """
        Get the prick(vector from origin) towards(ver) me(viewport)
        """
        pyModel = self.getPythonicModelViewMatrix()
        #get the vectors of x-axis, y-axis, z-axis and return a linear combination
        xAxisVector = [pyModel[0][0], pyModel[1][0], pyModel[2][0]]
        yAxisVector = [pyModel[0][1], pyModel[1][1], pyModel[2][1]]
        zAxisVector = [pyModel[0][2], pyModel[1][2], pyModel[2][2]]
        lcVector = []
        for idx in range(0, 3):
            lci = xAxisVector[idx] + yAxisVector[idx] + zAxisVector[idx]
            lcVector.append(lci)
        return lcVector

    def printModelProjView(self):
        """
        print the states of this stage, 
        Model
        Projection
        View
        """
        model = gl.glGetDoublev(gl.GL_MODELVIEW_MATRIX)
        proj = gl.glGetDoublev(gl.GL_PROJECTION_MATRIX)
        view = gl.glGetDoublev(gl.GL_VIEWPORT)
        ####
        pyModel = convertToPyArray(deepcopy(model))
        pyProj = convertToPyArray(deepcopy(proj))
        pyView = convertToPyArray(deepcopy(view))
        # import pprint
        # pp = pprint.PrettyPrinter(indent=4)
        # print('model-------')
        # pp.pprint(pyModel)
        # print('projection-------')
        # pp.pprint(pyProj)
        # print('view-----------')
        # pp.pprint(pyView)


class Shader:
    """
    Courtesy of ChatGPT:
    Order of shader pipeline:
    1. Vertex Shader
    - Processes individual vertices
    - Transforms vertex positions from object space to clip space (via the model, view, and projection matrices)
    - Outputs data (e.g., position, normals, texture coordinates) to the next stage.
    2. Tessellation Shaders (Optional)
    - If enabled, tesellation control and evaluation shaders refine geometry
    - Used for subdividing surfaces
    3. Geometry Shaders (Optional)
    - Operates on primitives (points, lines, or triangles) output by the vertex shader (or tessellation stage)
    - Can generate additional geometry (e.g., extrude a triangle into three new triangles).
    4. Fragment Shader 
    - Processes fragments (potential pixels) created by rasterizing primitives (triangles, lines, points)
    - Handles color, lighting, textures, and effects for each pixel.
    - Output the final color for each fragment
    5. Post-Processing and Framebuffer Operations
    - Blends, depth tests, and stencil tests occur here before the final image is rendered to the screen.
    """
    VERTEX_SHADER_FILEPATH = os.path.join(NDISPLAY_MODULE_DIR, 'core', 'shaders', 'vertex.glsl')
    #from the tutorial, the fragment shader computes diffuse, specular... for now we do not need that
    #FRAGMENT_SHADER_FILEPATH = os.path.join(NDISPLAY_MODULE_DIR, 'core', 'shaders', 'fragment.glsl')

    def __init__(self):
        with open(Shader.VERTEX_SHADER_FILEPATH, 'r') as f:
            vertex_src = f.readlines()

        # with open(Shader.FRAGMENT_SHADER_FILEPATH, 'r') as f:
        #     fragment_src = f.readlines()

        self.program = compileProgram( # linkage
            compileShader(vertex_src, gl.GL_VERTEX_SHADER), #compilation
            # compileShader(fragment_src, gl.GL_FRAGMENT_SHADER)
        )


class StandardStage(Stage):

    def __init__(self, piece):
        width = 800
        height = 600
        metronome = 10
        displayCaption = "Standard Stage"
        fieldOfView = 45
        zNear = 0.1
        zFar = 50
        verbose = False
        super().__init__(width, height, piece, metronome, displayCaption, fieldOfView, zNear, zFar, verbose)