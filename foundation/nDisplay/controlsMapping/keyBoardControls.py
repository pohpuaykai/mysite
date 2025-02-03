import glfw.GLFW as GLFW_CONSTANTS

#all possible keys can be listed by list(filter(lambda k: 'key' in k.lower(), dir(GLFW_CONSTANTS)))

KEYBOARD_3D_DISPLAY_CONTROLS = {
    "screen_left": GLFW_CONSTANTS.GLFW_KEY_LEFT,#pg.K_LEFT,
    "screen_right": GLFW_CONSTANTS.GLFW_KEY_RIGHT,#pg.K_RIGHT,
    "screen_up": GLFW_CONSTANTS.GLFW_KEY_UP,#pg.K_UP,
    "screen_down": GLFW_CONSTANTS.GLFW_KEY_DOWN,#pg.K_DOWN,
    "screen_in": GLFW_CONSTANTS.GLFW_KEY_A,#pg.K_a,
    "screen_out": GLFW_CONSTANTS.GLFW_KEY_S,#pg.K_s,
    "screen_left_sensitivity":0.1,
    "screen_right_sensitivity":0.1,
    "screen_up_sensitivity":0.1,
    "screen_down_sensitivity":0.1,
    "screen_in_sensitivity":0.1,
    "screen_out_sensitivity":0.1,
    ###
    "actor_reset": GLFW_CONSTANTS.GLFW_KEY_R#pg.K_r,
}