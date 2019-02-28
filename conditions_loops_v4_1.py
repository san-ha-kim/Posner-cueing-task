########################################
########################################
####                                ####
####        Posner task             ####
####                                ####
####    Condition loop functions    ####
####         version 4.1            ####
####                                ####
########################################
########################################

from constants_v4_1 import *
from conditions_decomposed_v4_1 import *
from psychopy import core, data, logging
from psychopy.visual import Window, TextStim, Circle, Rect, ShapeStim
from psychopy.event import waitKeys, getKeys
from psychopy.core import wait
from psychopy import logging
from psychopy.gui import DlgFromDict
import time, random

# define the data log names
dlg_box = DlgFromDict(session_info, title = 'Posner', fixed = ['date'])
if dlg_box.OK:
    print(session_info)
else:
    print('User has cancelled')
    core.quit()

LOGFILE = date_Str + ' pcpnt_' + session_info['Participant'] + '_obsvr_'+session_info['Observer']

# open a log to record the data
log = open(LOGFILE + '.tsv', 'w')

# watch for order change

# write the header row 
header = ['fix_onset', 'cue_onset', 'cue_offset', 'targ_onset', 'targ_offset', 'cue_side','targ_side', 
    'targets', 'response', 'validity', 'correct', 'reaction_time']
header_tabbed = '\t'.join(header)
header_tabbed += '\n'
log.write(header_tabbed)


for VCL in valid_car_trials_left:
    for ICL in invalid_car_trials_left:
        for VCR in valid_car_trials_right:
            for ICR in invalid_car_trials_right:
                
                # does not have the decrements; record responses
                
                def exp_VCL_record(): 
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    # update the monitor
                    fix_onset = disp.flip()
                    
                    # wait for fixation time
                    wait(Time_Fixation)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    #draw a cueStim
                    cue_Stim[VCL['cue_side']].draw()
                    # update the monitor
                    cue_onset = disp.flip()
                    # wait for a bit
                    wait(Time_Cue)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    # update the monitor
                    cue_offset = disp.flip()
                    # wait for a bit before the target is shown
                    wait(trial['soa']-Time_Cue)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    #draw a target stimulus
                    targ_Stim[VCL['targ_side']][VCL['targets']].draw()
                    #update the monitor
                    targ_onset=disp.flip()
                    
                    # wait for fixation time
                    wait(Time_Target)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    # update the monitor
                    targ_offset = disp.flip()
                    
                    # wait for a response
                    resp_list = waitKeys(maxWait = wait_time, keyList=['left','right'],\
                        timeStamped = True)
                    # select the first response from the respose list
                    
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
                            
                        #record the responses
                        header_list = [fix_onset, cue_onset, cue_offset, targ_onset, targ_offset, \
                            VCL['targ_side'],\
                            VCL['cue_side'], \
                            VCL['targets'], response, validity, correct, RT]
                        # convert to string
                        header_str = map(str, header_list)
                    
                        # convert to a single line, separated by tabs
                        header_line = '\t'.join(header_str)
                        header_line += '\n'
                        log.write(header_line)
                    else:
                        fb_scr['NoResp'].draw()
                        
                        # calculate the reaction time
                        RT = wait_time
                        
                        # check validity
                        if VCL['cue_side'] == VCL['targ_side']:
                            validity = "valid"
                        else:
                            validity = "invalid"
                        
                        #record the non response
                        header_list = [fix_onset, cue_onset, cue_offset, targ_onset, targ_offset, \
                            VCL['targ_side'],\
                            VCL['cue_side'], \
                            VCL['targets'], "NoResp", validity, "NoResp", RT]
                        # convert to string
                        header_str = map(str, header_list)
                    
                        # convert to a single line, separated by tabs
                        header_line = '\t'.join(header_str)
                        header_line += '\n'
                        log.write(header_line)
                        disp.flip()
                        wait(Time_Feedback)
                
                def exp_VCR_record(): 
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    # update the monitor
                    fix_onset = disp.flip()
                    # wait for fixation time
                    wait(Time_Fixation)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    #draw a cueStim
                    cue_Stim[VCR['cue_side']].draw()
                    # update the monitor
                    cue_onset = disp.flip()
                    # wait for a bit
                    wait(Time_Cue)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    # update the monitor
                    cue_offset = disp.flip()
                    # wait for a bit before the target is shown
                    wait(trial['soa']-Time_Cue)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    #draw a target stimulus
                    targ_Stim[VCR['targ_side']][VCR['targets']].draw()
                    #update the monitor
                    targ_onset=disp.flip()
                    
                    # wait for fixation time
                    wait(Time_Target)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    # update the monitor
                    targ_offset = disp.flip()
                    
                    # wait for a response
                    resp_list = waitKeys(maxWait = wait_time, keyList=['left','right'],\
                        timeStamped = True)
                    # select the first response from the respose list
                    
                    if resp_list != None:
                        response, press_time = resp_list[0]
                        
                        # check if the response was correct
                        if response == VCR['targ_side']:
                            correct = 1
                        else:
                            correct = 0
                        # calculate the reaction time
                        RT = press_time - targ_onset
                        
                        # check validity
                        if VCR['cue_side'] == VCR['targ_side']:
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
                            
                        #record the responses
                        header_list = [fix_onset, cue_onset, cue_offset, targ_onset, targ_offset, \
                            VCR['targ_side'],\
                            VCR['cue_side'], \
                            VCR['targets'], response, validity, correct, RT]
                        # convert to string
                        header_str = map(str, header_list)
                    
                        # convert to a single line, separated by tabs
                        header_line = '\t'.join(header_str)
                        header_line += '\n'
                        log.write(header_line)
                    else:
                        fb_scr['NoResp'].draw()
                        
                        # calculate the reaction time
                        RT = wait_time
                        
                        # check validity
                        if VCR['cue_side'] == VCR['targ_side']:
                            validity = "valid"
                        else:
                            validity = "invalid"
                        
                        #record the non response
                        header_list = [fix_onset, cue_onset, cue_offset, targ_onset, targ_offset, \
                            VCR['targ_side'],\
                            VCR['cue_side'], \
                            VCR['targets'], "NoResp", validity, "NoResp", RT]
                        # convert to string
                        header_str = map(str, header_list)
                    
                        # convert to a single line, separated by tabs
                        header_line = '\t'.join(header_str)
                        header_line += '\n'
                        log.write(header_line)
                        
                        # display the feedback screen
                        disp.flip()
                        
                        # move on after showing feedback
                        wait(Time_Feedback)
                
                def exp_ICL_record(): 
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    # update the monitor
                    fix_onset = disp.flip()
                    # wait for fixation time
                    wait(Time_Fixation)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    #draw a cueStim
                    cue_Stim[ICL['cue_side']].draw()
                    # update the monitor
                    cue_onset = disp.flip()
                    # wait for a bit
                    wait(Time_Cue)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    # update the monitor
                    cue_offset = disp.flip()
                    # wait for a bit before the target is shown
                    wait(trial['soa']-Time_Cue)
                
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    #draw a target stimulus
                    targ_Stim[ICL['targ_side']][ICL['targets']].draw()
                    #update the monitor
                    targ_onset=disp.flip()
                    
                    # rest to default screen, then wait for targ time
                    wait(Time_Target)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    # update the monitor
                    targ_offset = disp.flip()
                
                    # wait for a response
                    resp_list = waitKeys(maxWait = wait_time, keyList=['left','right'],\
                        timeStamped = True)
                    
                    # select the first response from the respose list
                    
                    if resp_list != None:
                        response, press_time = resp_list[0]
                        
                        # check if the response was correct
                        if response == ICL['targ_side']:
                            correct = 1
                        else:
                            correct = 0
                        # calculate the reaction time
                        RT = press_time - targ_onset
                        
                        # check validity
                        if ICL['cue_side'] == ICL['targ_side']:
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
                            
                        #record the responses
                        header_list = [fix_onset, cue_onset, cue_offset, targ_onset, targ_offset,\
                            ICL['targ_side'],\
                            ICL['cue_side'], \
                            ICL['targets'], response, validity, correct, RT]
                        # convert to string
                        header_str = map(str, header_list)
                    
                        # convert to a single line, separated by tabs
                        header_line = '\t'.join(header_str)
                        header_line += '\n'
                        log.write(header_line)
                    else:
                        fb_scr['NoResp'].draw()
                        
                        # calculate the reaction time
                        RT = wait_time
                        
                        # check validity
                        if ICL['cue_side'] == ICL['targ_side']:
                            validity = "valid"
                        else:
                            validity = "invalid"
                        
                        #record the non response
                        header_list = [fix_onset, cue_onset, cue_offset, targ_onset, targ_offset,\
                            ICL['targ_side'],\
                            ICL['cue_side'], \
                            ICL['targets'], "NoResp", validity, "NoResp", RT]
                        # convert to string
                        header_str = map(str, header_list)
                    
                        # convert to a single line, separated by tabs
                        header_line = '\t'.join(header_str)
                        header_line += '\n'
                        log.write(header_line)
                        disp.flip()
                        wait(Time_Feedback)
                
                def exp_ICR_record():
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    # update the monitor
                    fix_onset = disp.flip()
                    # wait for fixation time
                    wait(Time_Fixation)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    #draw a cueStim
                    cue_Stim[ICR['cue_side']].draw()
                    # update the monitor
                    cue_onset = disp.flip()
                    # wait for a bit
                    wait(Time_Cue)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    # update the monitor
                    cue_offset = disp.flip()
                    # wait for a bit before the target is shown
                    wait(trial['soa']-Time_Cue)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    #draw a target stimulus
                    targ_Stim[ICR['targ_side']][ICR['targets']].draw()
                    #update the monitor
                    targ_onset=disp.flip()
                    
                    # rest to default screen, then wait for targ time
                    wait(Time_Target)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    # update the monitor
                    targ_offset = disp.flip()
                    
                    # wait for a response
                    resp_list = waitKeys(maxWait = wait_time, keyList=['left','right'],\
                        timeStamped = True)
                    # select the first response from the respose list
                    
                    if resp_list != None:
                        response, press_time = resp_list[0]
                        
                        # check if the response was correct
                        if response == ICR['targ_side']:
                            correct = 1
                        else:
                            correct = 0
                            
                        # calculate the reaction time
                        RT = press_time - targ_onset
                        
                        # check validity
                        if ICR['cue_side'] == ICR['targ_side']:
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
                            
                        #record the responses
                        header_list = [fix_onset, cue_onset, cue_offset, targ_onset, targ_offset,\
                            ICR['targ_side'],\
                            ICR['cue_side'], \
                            ICR['targets'], response, validity, correct, RT]
                        # convert to string
                        header_str = map(str, header_list)
                    
                        # convert to a single line, separated by tabs
                        header_line = '\t'.join(header_str)
                        header_line += '\n'
                        log.write(header_line)
                    else:
                        fb_scr['NoResp'].draw()
                        
                        # calculate the reaction time
                        RT = wait_time
                        
                        if ICR['cue_side'] == ICR['targ_side']:
                            validity = "valid"
                        else:
                            validity = "invalid"
                        
                        #record the non response
                        header_list = [fix_onset, cue_onset, cue_offset, targ_onset, targ_offset,\
                            ICR['targ_side'],\
                            ICR['cue_side'], \
                            ICR['targets'], "NoResp", validity, "NoResp", RT]
                        # convert to string
                        header_str = map(str, header_list)
                    
                        # convert to a single line, separated by tabs
                        header_line = '\t'.join(header_str)
                        header_line += '\n'
                        log.write(header_line)
                        disp.flip()
                        wait(Time_Feedback)
                
                def exp_VCL_prac(): 
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    # update the monitor
                    fix_onset = disp.flip()
                    
                    # wait for fixation time
                    wait(Time_Fixation)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    #draw a cueStim
                    cue_Stim[VCL['cue_side']].draw()
                    # update the monitor
                    cue_onset = disp.flip()
                    # wait for a bit
                    wait(Time_Cue)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    # update the monitor
                    cue_offset = disp.flip()
                    # wait for a bit before the target is shown
                    wait(trial['soa']-Time_Cue)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    #draw a target stimulus
                    targ_Stim[VCL['targ_side']][VCL['targets']].draw()
                    #update the monitor
                    targ_onset=disp.flip()
                    
                    # rest to default screen, then wait for targ time
                    wait(Time_Target)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    # update the monitor
                    targ_offset = disp.flip()
                    
                    # wait for a response
                    resp_list = waitKeys(maxWait = wait_time, keyList=['left','right'], \
                        timeStamped = True)
                    # select the first response from the respose list
                    
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
                        
                    else:
                        fb_scr['NoResp'].draw()
                        disp.flip()
                        wait(Time_Feedback)
                    
                def exp_VCR_prac(): 
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    # update the monitor
                    fix_onset = disp.flip()
                    # wait for fixation time
                    wait(Time_Fixation)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    #draw a cueStim
                    cue_Stim[VCR['cue_side']].draw()
                    # update the monitor
                    cue_onset = disp.flip()
                    # wait for a bit
                    wait(Time_Cue)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    # update the monitor
                    cue_offset = disp.flip()
                    # wait for a bit before the target is shown
                    wait(trial['soa']-Time_Cue)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    #draw a target stimulus
                    targ_Stim[VCR['targ_side']][VCR['targets']].draw()
                    #update the monitor
                    targ_onset=disp.flip()
                    
                    # rest to default screen, then wait for targ time
                    wait(Time_Target)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    # update the monitor
                    targ_offset = disp.flip()
                    
                    # wait for a response
                    resp_list = waitKeys(maxWait = wait_time, keyList=['left','right'],\
                        timeStamped = True)
                    # select the first response from the respose list
                    
                    if resp_list != None:
                        response, press_time = resp_list[0]
                        
                        # check if the response was correct
                        if response == VCR['targ_side']:
                            correct = 1
                        else:
                            correct = 0
                        # calculate the reaction time
                        RT = wait_time
                        
                        # check validity
                        if VCR['cue_side'] == VCR['targ_side']:
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
                            
                    else:
                        fb_scr['NoResp'].draw()
                        disp.flip()
                        wait(Time_Feedback)
                
                def exp_ICL_prac(): 
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    # update the monitor
                    fix_onset = disp.flip()
                    # wait for fixation time
                    wait(Time_Fixation)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    #draw a cueStim
                    cue_Stim[ICL['cue_side']].draw()
                    # update the monitor
                    cue_onset = disp.flip()
                    # wait for a bit
                    wait(Time_Cue)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    # update the monitor
                    cue_offset = disp.flip()
                    # wait for a bit before the target is shown
                    wait(trial['soa']-Time_Cue)
                
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    #draw a target stimulus
                    targ_Stim[ICL['targ_side']][ICL['targets']].draw()
                    #update the monitor
                    targ_onset=disp.flip()
                    
                    # rest to default screen, then wait for targ time
                    wait(Time_Target)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    # update the monitor
                    targ_offset = disp.flip()
                    
                    # wait for a response
                    resp_list = waitKeys(maxWait = wait_time, keyList=['left','right'],\
                        timeStamped = True)
                    
                    # select the first response from the respose list
                    
                    if resp_list != None:
                        response, press_time = resp_list[0]
                        
                        # check if the response was correct
                        if response == ICL['targ_side']:
                            correct = 1
                        else:
                            correct = 0
                        # calculate the reaction time
                        RT = press_time - targ_onset
                        
                        # check validity
                        if ICL['cue_side'] == ICL['targ_side']:
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
                            
                    else:
                        fb_scr['NoResp'].draw()
                        disp.flip()
                        wait(Time_Feedback)
                
                def exp_ICR_prac():
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    # update the monitor
                    fix_onset = disp.flip()
                    # wait for fixation time
                    wait(Time_Fixation)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    #draw a cueStim
                    cue_Stim[ICR['cue_side']].draw()
                    # update the monitor
                    cue_onset = disp.flip()
                    # wait for a bit
                    wait(Time_Cue)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    # update the monitor
                    cue_offset = disp.flip()
                    # wait for a bit before the target is shown
                    wait(trial['soa']-Time_Cue)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    #draw a target stimulus
                    targ_Stim[ICR['targ_side']][ICR['targets']].draw()
                    #update the monitor
                    targ_onset=disp.flip()
                    
                    # rest to default screen, then wait for targ time
                    wait(Time_Target)
                    
                    # draw the fixation mark, and the left and right boxes
                    fix_Stim.draw()
                    Box_Left.draw()
                    Box_Right.draw()
                    # update the monitor
                    targ_offset = disp.flip()
                    
                    # wait for a response
                    resp_list = waitKeys(maxWait = wait_time, keyList=['left','right'],\
                        timeStamped = True)
                    # select the first response from the respose list
                    
                    if resp_list != None:
                        response, press_time = resp_list[0]
                        
                        # check if the response was correct
                        if response == ICR['targ_side']:
                            correct = 1
                        else:
                            correct = 0
                            
                        # calculate the reaction time
                        RT = wait_time
                        
                        # check validity
                        if ICR['cue_side'] == ICR['targ_side']:
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
                    else:
                        fb_scr['NoResp'].draw()
                        disp.flip()
                        wait(Time_Feedback)