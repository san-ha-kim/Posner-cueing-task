######################################
######################################
####                              ####
####        Posner task           ####
####    conditions version 3.5    ####
####    contains the constants    ####
####    and dicts for exp 3.5     ####
####                              ####
######################################
######################################

from constants_v3_5 import *

#define an empty all trials list
all_trials = []

# populate the all trials list will all the possible conditions
for cue_side in Location_Cue: # loop through all parameters
    for targ_side in Location_Targ:
        for soa in SOA:
            for targets in targ:
                trial = {
                    
                    'targ_side':targ_side,
                    'cue_side':cue_side,
                    'targets':targets, 
                    'soa':soa
                    
                    }
                    
                all_trials.extend([trial])

valid_car_trials = [] # valid car trials list
valid_ped_trials = [] # valid pedestrian/cyclist trials list
invalid_car_trials = [] # invalid car trials list
invalid_ped_trials = [] # invalid pedestria/cyclist trials list

for cue_side in Location_Cue: # loop through all parameters
    for targ_side in Location_Targ:
        for targets in targ:
            if cue_side == targ_side and targets == "C":
                valid_car_dict = {
                    
                    "targ_side":targ_side,
                    "cue_side":cue_side,
                    "targets":targets
                    
                    }
                    
                valid_car_trials.extend([valid_car_dict])
                
            elif cue_side == targ_side and targets == "P":
                valid_ped_dict ={
                    
                    "targ_side":targ_side, 
                    "cue_side":cue_side,
                    "targets":targets
                    
                    }
                    
                valid_ped_trials.extend([valid_ped_dict])
                
            elif cue_side != targ_side and targets == "C":
                invalid_car_dict = {
                    
                    "targ_side":targ_side, 
                    "cue_side":cue_side,
                    "targets":targets
                    
                    }
                
                invalid_car_trials.extend([invalid_car_dict])
                
            elif cue_side != targ_side and targets == "P":
                invalid_ped_dict = {
                    
                    "targ_side":targ_side, 
                    "cue_side":cue_side,
                    "targets":targets
                    
                    }

                invalid_ped_trials.extend([invalid_ped_dict])

# create separate dicts for left and right for each conditions
valid_car_trials_left = [valid_car_trials[0]]
valid_car_trials_right = [valid_car_trials[1]]

invalid_car_trials_left = [invalid_car_trials[0]]
invalid_car_trials_right = [invalid_car_trials[1]]


car_trials = list.copy(valid_car_trials)
car_trials.extend(invalid_car_trials)
