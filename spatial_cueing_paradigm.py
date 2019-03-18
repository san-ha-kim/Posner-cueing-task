from psychopy.visual import Window, Rect, ShapeStim, TextStim, Circle
from psychopy.core import wait
from psychopy.event import waitKeys
from psychopy.gui import DlgFromDict
from random import choice
import time, sys

# ===== Number of trials =====
n_real = 100
n_practice = 10
p_valid = 0.8

# ===== Window size =====
win_width, win_height = 1920, 1080
win_dimension = (win_width, win_height)

# ===== Colours to be used =====
GREY = [128, 128, 128]
BLACK = [0, 0, 0]
WHITE = [1, 1, 1]
YELLOW = [255, 255, 0]
GREEN = [0, 255, 0]
RED = [255, 0, 0]

cue_color = YELLOW

# ===== Times and durations in seconds =====
t_fix = 0.1
t_cue = 0.05
t_feedback = 0.1
t_target = 0.01  # for how long the target appears
t_answer = 0.1  # for how long to make an answer choice
v_sync = 0

# ===== Parameters for font, text and writing =====
font_size = 30

welcome_text = "You will see a screen with a white cross in the middle, and two boxes to the sides.\n\n" \
               "One of the boxes will briefly flash. Ignore this!\n\n" \
               "A circle will then appear in either left or right box.\n" \
               "Press the LEFT ARROW KEY when you see the circle in the left box.\n" \
               "Press the RIGHT ARROW KEY when you see the circle in the right box.\n\n" \
               "Press the correct keys as quickly and accurately as you can.\n\n" \
               "Press the SPACEBAR when you are ready to practice.\n\n" \
               "If you need to stop, let the experimenter know."

practice_finished_text = "The practice is now over.\n\n" \
                "When you are ready for the real trials, press the SPACEBAR to continue.\n\n" \
                "Remember to be as quick and accurate as you can!"

experiment_finished_Text = "The experiment is now over. Thank you for participating!\n\n" \
                "Please let the experimenter know"

# ===== Target radius in pixels =====
target_size = 30

# ===== CSV file preparation ======
session_info = {'Observer': 'Type observer ID', 'Participant': 'Type participant ID'}
date_Str = time.strftime("%b_%d_%H%M", time.localtime())  # add the current time

file_prefix = date_Str + ' pcpnt_' + session_info['Participant'] + '_obsvr_'+session_info['Observer']


def convertRGB(RGB):
    """function to convert RGB guns from 255-range values to normalised values for PsychoPy"""
    normalised_color = []
    for gun in RGB:
        normV = ((1/127.5)*gun)-1
        normalised_color.append(normV)

    return normalised_color

    
# ===== Display window =====
disp = Window(size=win_dimension, pos=(0, 0), color=GREY, colorSpace="rgb255", fullscr=False, units="pix")
# - Fixation cross in the center of display
fixation_cross = ShapeStim(disp, lineWidth=5, lineColor=convertRGB(BLACK), fillColor=convertRGB(BLACK), vertices='cross')


class Box:
    """class to draw boxes, neutrally or to flash as cues"""
    def __init__(self):

        self.normal_color = convertRGB(BLACK)
        self.normal_line = 3

        self.cue_color = convertRGB(cue_color)
        self.cue_line = 8

        self.width = self.height = 200

        self.left_x = int(win_width * -0.25)
        self.right_x = int(win_width * 0.25)

    def default_draw(self):
        y = 0
        left_box = Rect(disp, pos=(self.left_x,y), width=self.width, height=self.height,
                        lineColor=self.normal_color, lineWidth=self.normal_line)
        right_box = Rect(disp, pos=(self.right_x,y), width=self.width, height=self.height,
                         lineColor=self.normal_color, lineWidth=self.normal_line)
        left_box.draw()
        right_box.draw()

    def cue(self, location):
        y = 0
        if location == "left":
            left_cue =  Rect(disp, pos=(self.left_x,y), width=self.width, height=self.height,
                             lineColor=self.cue_color, lineWidth=self.cue_line)
            right_box = Rect(disp, pos=(self.right_x, y), width=self.width, height=self.height,
                             lineColor=convertRGB(BLACK), lineWidth=self.normal_line)
            right_box.draw()
            left_cue.draw()

        if location == "right":
            left_box = Rect(disp, pos=(self.left_x, y), width=self.width, height=self.height,
                            lineColor=convertRGB(BLACK), lineWidth=self.normal_line)
            right_cue = Rect(disp, pos=(self.right_x,y), width=self.width, height=self.height,
                             lineColor=self.cue_color, lineWidth=self.cue_line)
            right_cue.draw()
            left_box.draw()


class Target:
    """class to draw targets"""
    def __init__(self, color, radius=target_size):
        self.color = color
        self.radius = radius

    def draw(self, location):
        y = 0
        if location == "left":
            x = int(win_width * -0.25)
            left_targ = Circle(disp, pos=(x, y), radius=self.radius, edges=32, lineColor=self.color, fillColor=self.color)
            left_targ.draw()
        if location == "right":
            x = int(win_width * 0.25)
            right_targ = Circle(disp, pos=(x, y), radius=self.radius, edges=32, lineColor=self.color, fillColor=self.color)
            right_targ.draw()


class Write:
    """class to display texts on screen"""
    def __init__(self, size):
        self.size = size

    def instructions(self, state):
        if state == "welcome":
            textscreen = TextStim(disp, text=welcome_text, color=convertRGB(BLACK), height=self.size)
            textscreen.draw()
            disp.flip()

        if state == "experiment finished":
            endscreen = TextStim(disp, text=experiment_finished_Text, color=convertRGB(BLACK), height=self.size)
            endscreen.draw()
            disp.flip()

        if state == "practice finished":
            pracscreen = TextStim(disp, text=practice_finished_text, color=convertRGB(BLACK), height=self.size)
            pracscreen.draw()
            disp.flip()

    def feedback_text(self, state):
        if state == "incorrect":
            fb_inc = TextStim(disp, text='Incorrect!', height=self.size, color=convertRGB(RED))
            fb_inc.draw()
        if state == "correct":
            fb_C = TextStim(disp, text='Correct!', height=self.size, color=convertRGB(GREEN))
            fb_C.draw()
        if state == "no response":
            fb_nr = TextStim(disp, text='Please make a choice!', height=self.size, color=convertRGB(BLACK))
            fb_nr.draw()


def record_response(validity, target_location, correct, RT, log):
    """function to record responses"""
    header_list = [validity, target_location, correct, RT]
    header_str = map(str, header_list)
    header_line = ",".join(header_str)
    header_line += "\n"
    log.write(header_line)


def default_screen():
    """function to display cross and neutral boxes"""
    fixation_cross.draw()
    Box().default_draw()


def cue_and_target(validity, target_location, record, log):
    """function to cue and present target"""
    if validity == "valid":
        if target_location == "left":
            fixation_cross.draw()
            Box().cue("left")
            disp.flip()
            wait(t_cue)

            default_screen()
            Target(convertRGB(BLACK)).draw("left")
            t_target_onset = disp.flip()
            wait(t_target)

            default_screen()
            disp.flip()
            # wait(t_answer)

        if target_location == "right":
            fixation_cross.draw()
            Box().cue("right")
            disp.flip()
            wait(t_cue)

            default_screen()
            Target(convertRGB(BLACK)).draw("right")
            t_target_onset = disp.flip()
            wait(t_target)

            default_screen()
            disp.flip()

    if validity == "invalid":
        if target_location == "left":
            fixation_cross.draw()
            Box().cue("right")
            disp.flip()
            wait(t_cue)

            default_screen()
            Target(convertRGB(BLACK)).draw("left")
            t_target_onset = disp.flip()
            wait(t_target)

            default_screen()
            disp.flip()

        if target_location == "right":
            fixation_cross.draw()
            Box().cue("left")
            disp.flip()
            wait(t_cue)

            default_screen()
            Target(convertRGB(BLACK)).draw("right")
            t_target_onset = disp.flip()
            wait(t_target)

            default_screen()
            disp.flip()

    # -- Returns a list of which key is pressed in a predefined list
    resp_list = waitKeys(maxWait=t_answer, keyList=['left', 'right'], timeStamped=True)
    correct = 0
    if resp_list is not None:
        response, t_keypress = resp_list[0]
        if response == target_location:
            correct = 1
        else:
            correct = 0

        RT = t_keypress - t_target_onset

        if correct == 1:
            Write(font_size).feedback_text("correct")
            disp.flip()
        elif correct == 0:
            Write(font_size).feedback_text("incorrect")
            disp.flip()

    else:
        Write(font_size).feedback_text("no response")
        disp.flip()
        RT = "no_response"

    if record:
        record_response(validity, target_location, correct, RT, log)


def trial(trial_number, record_answers, log):
    """trial loop function"""
    # == Number of specific condition trials, must be rounded
    n_valid_left = n_valid_right = round((trial_number*p_valid)/2)
    n_invalid_left = n_invalid_right = round((trial_number*(1-p_valid))/2)

    print(n_valid_left, n_valid_right, n_invalid_left, n_invalid_right)

    # == count of total trials completed
    c_total = 0
    # -- Count of total conditional trials
    TOTAL_VALID_LEFT = TOTAL_INVALID_LEFT = TOTAL_VALID_RIGHT = TOTAL_INVALID_RIGHT = 0

    # == Set to record answer to true or false for recording responses
    if record_answers:
        record = True

    else:
        record = False

    # == variable to make it easier to denote locations and validity
    left = "left"
    right = "right"
    valid = "valid"
    invalid = "invalid"

    # == Pool of different conditions for fixed number of conditions across trials
    pool = ["VL", "VR", "IL", "IR"]

    while c_total < trial_number:
        # print("Total trials completed: {:d}".format(c_total))
        default_screen()
        disp.flip()
        wait(t_fix)

        # -- Randomly pick a condition from the pool, and name it ticket (like picking a name from a hat)
        ticket = choice(pool)

        # print(pool)

        if ticket == "VL" and n_valid_left > 0:  # VL
            cue_and_target(valid, left, record, log)
            wait(t_feedback)

            n_valid_left -= 1
            c_total += 1
            TOTAL_VALID_LEFT += 1

            if n_valid_left == 0:
                pool.remove("VL")

        if ticket == "VR" and n_valid_right > 0:  # VR
            cue_and_target(valid, right, record, log)
            wait(t_feedback)

            n_valid_right -= 1
            c_total += 1
            TOTAL_VALID_RIGHT += 1

            if n_valid_right == 0:
                pool.remove("VR")

        if ticket == "IL" and n_invalid_left > 0:  # IL
            cue_and_target(invalid, left, record, log)
            wait(t_feedback)
            n_invalid_left -= 1
            c_total += 1
            TOTAL_INVALID_LEFT += 1

            if n_invalid_left == 0:
                pool.remove("IL")

        if ticket == "IR" and n_invalid_right > 0:  # IR
            # if n_invalid_right > 0:
            cue_and_target(invalid, right, record, log)
            wait(t_feedback)
            n_invalid_right -= 1
            c_total += 1
            TOTAL_INVALID_RIGHT += 1

            if n_invalid_right == 0:
                pool.remove("IR")

    print("Total number of left: valid {TVL:d}, invalid {TIL:d}; right: valid {TVR:d}, invalid {TIR:d}".format(TVL=TOTAL_VALID_LEFT, TIL=TOTAL_INVALID_LEFT, TVR=TOTAL_VALID_RIGHT, TIR=TOTAL_INVALID_RIGHT))


def main():
    """main loop"""
    # == Box to enter subject and experimenter information ==
    dlg_box = DlgFromDict(session_info, title="Spatial Cueing Paradigm", fixed=["date"])

    if dlg_box.OK:  # - If participant information has been entered

        # == Prepare file to record responses ==
        file = open(file_prefix+".csv", "w")
        header = ["validity", "target_location", "correct", "response_time"]
        delim = ",".join(header)
        delim += "\n"
        file.write(delim)

        # == Welcome screen ==
        Write(font_size).instructions("welcome")
        waitKeys(keyList=['space'], timeStamped=False)

        # == Practice trials, not recording responses ==
        trial(n_practice, False, file)

        # == Practice over screen and key
        Write(font_size).instructions("practice finished")
        waitKeys(keyList=['space'], timeStamped=False)

        # == Real trials
        trial(n_real, True, file)

        # == Experiment over
        Write(font_size).instructions("experiment finished")
        waitKeys(keyList=['escape', 'space'])
        file.close()
        disp.close()
        sys.exit()

    else:
        print("User has cancelled")
        disp.close()
        sys.exit()


if __name__ == "__main__":
    main()
