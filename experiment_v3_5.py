########################################
########################################
####                                ####
####        Posner task             ####
####                                ####
####    Experiment version 3.5      ####
####                                ####
########################################
########################################

from constants_v3_5 import *
from conditions_decomposed_v3_5 import *
from conditions_loops_v3_5 import *
from psychopy.visual import Window, TextStim, Circle, Rect, ShapeStim
from psychopy.event import waitKeys, getKeys
from psychopy.core import wait
from psychopy.gui import DlgFromDict
from psychopy import core, data, logging
import time, random

########################################

# define the data log names
dlg_box = DlgFromDict(session_info, title = 'Posner', fixed = ['date'])
if dlg_box.OK:
    print(session_info)
else:
    print('User has cancelled')
    core.quit()

# randomise the order of all trials
random.shuffle(all_trials)
random.shuffle(valid_car_trials)
random.shuffle(invalid_car_trials)

#present the first instructions
inst_Stim_1.draw()
disp.flip()

#wait for any  keypress to advance past the instructions screen
waitKeys(maxWait = float('inf'), keyList = ['space'], timeStamped = False)
"""
#present the second instructions
inst_Stim_2.draw()
disp.flip()

#wait for any  keypress to advance past the instructions screen
waitKeys(maxWait = float('inf'), keyList = ['space'], timeStamped = True)
"""
# present the practice loops

p_left = p_right = p_rounds/2

while p_left > 0 and p_right > 0:
    if random.random() < 0.5: # left trials
        if random.random() < 0.8: #valid targets
            exp_VCL_prac()
            p_left -= 1
        else: # invalid trials
            exp_VCR_prac()
            p_right -= 1
    else: # right trials
        if random.random() < 0.8: # valid targets
            exp_ICL_prac()
            p_left -= 1
        else: # invalid trials
            exp_ICR_prac()
            p_right -= 1

if p_left == 0 and p_right > 0: # if there has been more than 50% left targets
    while p_right > 0:
        if random.random() < 0.8:
            exp_VCR_prac()
            p_right -= 1
        else:
            exp_ICR_prac()
            p_right -= 1

elif p_left > 0 and p_right == 0: # if there has been more than 50% right targets
    while p_left > 0:
        if random.random() < 0.8:
            exp_VCL_prac()
            p_left -= 1
        else:
            exp_ICL_prac()
            p_left -= 1
    
# present the post practice screens
prac_Fin_win.draw()
disp.flip()
waitKeys(maxWait = float('inf'), keyList = ['space'], timeStamped=False)
"""
# prepare the experimental loop

left = right = n_trials/2

while left > 0 and right > 0:
    if random.random() < 0.5: # left trials
        if random.random() < 0.8: #valid targets
            exp_VCL_record()
            left -= 1
        else: # invalid trials
            exp_VCR_record()
            right -= 1
    else: # right trials
        if random.random() < 0.8: # valid targets
            exp_ICL_record()
            left -= 1
        else: # invalid trials
            exp_ICR_record()
            right -= 1

if left == 0 and right > 0: # if there has been more than 50% left targets
    while right > 0:
        if random.random() < 0.8:
            exp_VCR_record()
            right -= 1
        else:
            exp_ICR_record()
            right -= 1

elif left > 0 and right == 0: # if there has been more than 50% right targets
    while left > 0:
        if random.random() < 0.8:
            exp_VCL_record()
            left -= 1
        else:
            exp_ICL_record()
            left -= 1

# finish the experiment
finished_win.draw()
disp.flip()
waitKeys(maxWait = float('inf'), keyList = ['escape'], timeStamped = False,\
    clearEvents = False)
"""
# close the display
disp.close()

# close the log
log.close()