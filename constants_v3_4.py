########################################
########################################
####                                ####
####        Posner task             ####
####                                ####
####      Constant variables        ####
####          version 3.3           ####
####                                ####
########################################
########################################

from psychopy.visual import Rect, Window, TextStim, ShapeStim, Circle
import time, random
from psychopy import event

########################################



wait_time = 1 # how long to wait for response before moving to next trial

n_trials = 30 # number of trials

p_rounds = 5 # number of practice rounds

########################################

# v-sync time (sec)
v_sync = 0.004508

# foreground and background colours

FGC = (-1, -1, -1) #black
BGC = (0, 0, 0) #grey
display_size = (1920,1080) #the monitor display resolution. if fullscr, then resol should match monitor's
disp = Window(size=display_size, units='pix', color = BGC, fullscr = False) # define the window of the experiment. KEEP FULLSCR TO FALSE
#flashing border color

cue_Flash = (1, 1, 0) #yellow

#potential cue locations 

Location_Cue = ['left','right']
Location_Targ = ['left', 'right'] 

#potential stimulus onset ansynchrony (SOA; time between cue and target onset)

SOA = [0.1 - v_sync] #in seconds; subtract v-sync to match monitor refresh rate

#potential targets
targ = ['C']

#times for fixation, cue, SOA and feedback

Time_Fixation = 1.5 - v_sync #in sec; subtract the time to match with v-sync

Time_Cue = 0.05 - v_sync

Time_Feedback = 1.0 - v_sync

#define and set the probability
validity_chance = random.random()

#define the instruction text and stimulus

instr_Text_1 = 'Welcome! \n\n\
Firstly, you are welcome to stop any time; just let the experimentor know!\n\n\
In this experiment, you will see a white cross in the middle, and two boxes to the sides.\n\n\
Circles of two difference sizes will appear in either boxes.\n\n\
Press the spacebar to continue'
instr_Text_2 = 'Press left arrow key when you see the circle to the left;\n\
press the right arrow when you see the circle to the right.\n\n\
Press the correct keys as quickly and as accurately as you can.\n\n\
Press the spacebar when you are ready to practice.'

inst_Stim_1 = TextStim(disp, text=instr_Text_1, color = FGC,\
    height = 24)
inst_Stim_2 = TextStim(disp, text = instr_Text_2, color = FGC,\
    height = 24)

#define the data output log file names
session_info = {'Observer': 'Type observer initials',\
    'Participant': 'Type participant ID'}

#current time in string
date_Str = time.strftime("%b_%d_%H%M", time.localtime())  # add the current time

#define the boxes for drawing cues and targets

Box_Dimen = [200, 200]

Box_Coord = {}
Box_Coord['left'] = (int(display_size[0]*-0.25),0) # a quarter of the way to the left and right from the center of the screen
Box_Coord['right'] = (int(display_size[0]*0.25),0)

#create the left and right boxes for presentation

Box_Left = Rect(disp, pos = Box_Coord['left'],\
    width = Box_Dimen[0], height = Box_Dimen[1], \
    lineColor = FGC, lineWidth = 3)

Box_Right = Rect(disp, pos = Box_Coord['right'],\
    width = Box_Dimen[0], height = Box_Dimen[1], \
    lineColor = FGC, lineWidth = 3)


#define the cue and create the cue windows (thicker border)
cue_Stim = {}

cue_Stim['left'] = Rect(disp, pos = Box_Coord['left'], \
    width = Box_Dimen[0], height = Box_Dimen[1], \
    lineColor = cue_Flash, lineWidth = 8)

cue_Stim['right'] = Rect(disp, pos = Box_Coord['right'],\
    width = Box_Dimen[0], height = Box_Dimen[1],\
    lineColor = cue_Flash, lineWidth = 8)



#create a fixation point/cross
fix_Stim = ShapeStim(disp, lineWidth = 50, lineColor = [1, 1, 1], \
    fillColor = [1, 1, 1], vertices = 'cross')

#create a dictionary for target display, and nested dict for different targets
targ_Stim = {}
targ_Stim['left'] = {}
targ_Stim['right'] = {}

targ_Stim['left']['P'] = Circle(disp, radius = 15, edges = 32, lineColor = FGC,\
    lineWidth = 5, fillColor = FGC, pos = Box_Coord['left'])
targ_Stim['right']['P'] = Circle(disp, radius = 15, edges = 32, lineColor = FGC,\
    lineWidth = 5, fillColor = FGC, pos = Box_Coord['right'])
targ_Stim['left']['C'] = Circle(disp, radius = 50, edges = 32, lineColor = FGC,\
    lineWidth = 5, fillColor = FGC, pos = Box_Coord['left'])
targ_Stim['right']['C'] = Circle(disp, radius = 50, edges = 32, lineColor = FGC,\
    lineWidth = 5, fillColor = FGC, pos = Box_Coord['right'])

# define the feedback screens
fb_scr = {}

fb_scr['Incorrect'] = TextStim(disp, text = 'Incorrect', height = 24,\
    color = (1, -1, -1))
fb_scr['Correct'] = TextStim(disp, text = 'Correct!', height = 24,\
    color = (-1, 1, -1))
fb_scr['NoResp'] = TextStim(disp, text = 'Please make a choice',\
    height = 24, color = (-1, 1, -1))

# define the post practice screen
prac_Fin_Text = 'The practice is now over. Press the Spacebar when you are ready to \
continue.\n\n Remember to be as quick and accurate as you can!'
prac_Fin_win = TextStim(disp, text = prac_Fin_Text, color = FGC, height = 24)

# define the finished screens
finished_Text = 'The experiment is now over\n\n\
Thank you for participating!\n\n\
Press the Esc key to exit'

finished_win = TextStim(disp, text = finished_Text,\
    color = FGC, height = 24)