import os
from tqdm import tqdm
import re
from util.vtk_revise import read_vtk
# from get_thickness_with_interpolate import get_thick_norm_and_ori
from modify_thickness import get_thick_norm_and_ori
import gc


rootDir = './ADNI_Cortex_vtk'


subdirectories = [d for d in os.listdir(rootDir) 
                  if os.path.isdir(os.path.join(rootDir, d))]


cnt = 0 

for dirName, subdirList, fileList in tqdm(os.walk(rootDir)):
    
    full_file_name_lh = None 
    
    read_dir_name = dirName.replace("\\", "/")
    
    subdir_name = os.path.basename(read_dir_name)
    


    new_path = 'new_output2/'
    
    new_dir_path = new_path + subdir_name
    
    

    if subdir_name not in rootDir : 
        if not os.path.exists(new_dir_path):
            os.makedirs(new_dir_path)
    

    
    for fname in fileList : 
        
        if 'vtk' and not 'ic3' in fname : 
            if 'lh' in fname :                         
                full_file_name_lh = read_dir_name + '/' + fname
            if 'rh' in fname :                         
                full_file_name_rh = read_dir_name + '/' + fname
                
    
    if full_file_name_lh == None : 
        continue 
    
    else : 
    
        print(f"-----------------SUBJECT  LH {subdir_name} BRAIN START----------------")
        
        lh_file_name = 'new.' + 'lh.sphere.reg.vtk'
        
        new_lh_file_name = new_dir_path + '/' + lh_file_name
        
        
        if not os.path.exists(new_lh_file_name):
            lh_brain = read_vtk(full_file_name_lh) 
            try : 
                get_thick_norm_and_ori(new_lh_file_name,lh_brain,50)
            except : 
                print(f'Could not read this file : {subdir_name}')
                continue
            gc.collect()

        else:
            print(f"{new_lh_file_name} already exists")
        
        


        print(f"-----------------SUBJECT RH {subdir_name} BRAIN START----------------")
        
        rh_file_name = 'new.' + 'rh.sphere.reg.vtk'
        
        new_rh_file_name = new_dir_path + '/' + rh_file_name
        
        if not os.path.exists(new_rh_file_name):
            rh_brain = read_vtk(full_file_name_rh) 
            try : 
                get_thick_norm_and_ori(new_rh_file_name,rh_brain,50)
            except : 
                print(f'Could not read this file : {subdir_name}')
                continue 
            gc.collect()

        else:
            print(f"{new_rh_file_name} already exists")



                
    

            
            

