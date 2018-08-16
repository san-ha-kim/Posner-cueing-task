########################################
########################################
####                                ####
####        Posner task             ####
####                                ####
####    Experiment version 3.4      ####
####                                ####
########################################
########################################

from constants_v3_4 import *
from conditions_decomposed_v3_4 import *
from conditions_loops_v3_4 import *
from psychopy.visual import Window, TextStim, Circle, Rect, ShapeStim
from psychopy.event import waitKeys, getKeys
from psychopy.core import wait
from psychopy.gui import DlgFromDict
from psychopy import core, data, logging
import time, random

########################################
"""
# define the data log names
dlg_box = DlgFromDict(session_info, title = 'Posner', fixed = ['date'])
if dlg_box.OK:
    print(session_info)
else:
    print('User has cancelled')
    core.quit()
"""
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

# present the practice loops

for trial in all_trials:
    while p_rounds > 0:
        # draw the fixation mark, and the left and right boxes
        fix_Stim.draw()
        Box_Left.draw()
        Box_Right.draw()
        # update the monitor
        disp.flip()
        # wait for fixation time
        wait(Time_Fixation)
    
        # draw the fixation mark, and the left and right boxes
        fix_Stim.draw()
        Box_Left.draw()
        Box_Right.draw()
        #draw a cueStim
        cue_Stim[trial['cue_side']].draw()
        # update the monitor
        cue_onset = disp.flip()
        # wait for a bit
        wait(Time_Cue)
        
        # draw the fixation mark, and the left and right boxes
        fix_Stim.draw()
        Box_Left.draw()
        Box_Right.draw()
        # update the monitor
        cueoffset = disp.flip()
        # wait for a bit before the target is shown
        wait(trial['soa']-Time_Cue)
        
        # draw the fixation mark, and the left and right boxes
        fix_Stim.draw()
        Box_Left.draw()
        Box_Right.draw()
        #draw a target stimulus
        targ_Stim[trial['targ_side']][trial['targets']].draw()
        #update the monitor
        targ_onset = disp.flip()
    
        # wait for a response
        resp_list = waitKeys(maxWait = wait_time, keyList=['left','right'],\
            timeStamped = True)
        if resp_list != None:
            response, press_time = resp_list[0]
            
            # check if the response was correct
            if response == VCL['targ_side']:
                correct = 1
            else:
                correct = 0
            # calculate the reaction time
            RT = press_time - targ_onset
            
            # check validity
            if VCL['cue_side'] == VCL['targ_side']:
                validity = "valid"
            else:
                validity = "invalid"
        
            # show the appropriate feedback scr
            if correct == 1:
                fb_scr['Correct'].draw()
                disp.flip()
                wait(Time_Feedback)
            elif correct == 0:
                fb_scr['Incorrect'].draw()
                disp.flip()
                wait(Time_Feedback)
            
            p_rounds -= 1
            
        else:
            # display the feedback screen for no response
            
            fb_scr['NoResp'].draw()
            disp.flip()
            wait(Time_Feedback+0.5)
            
            p_rounds -= 1
    
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

# close the display
disp.close()

# close the log
log.close()