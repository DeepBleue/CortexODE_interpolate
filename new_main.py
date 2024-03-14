import os
from tqdm import tqdm
import re
from util.vtk_revise import read_vtk
from get_thickness_with_interpolate import get_thick_norm_and_ori
import gc


rootDir = './new_data/FreeCortex_output'

subdirectories = [d for d in os.listdir(rootDir) 
                  if os.path.isdir(os.path.join(rootDir, d))]

cnt = 0 

for dirName, subdirList, fileList in tqdm(os.walk(rootDir)):
    
    sub_dir_name = subdirectories[cnt]
    
    
    if 'surf' in dirName : 
        read_dir_name = dirName.replace("\\", "/")

        for fname in fileList:
            if 'vtk' in fname:
                if 'lh' in fname : 
                    if 'white' in fname : 
                        full_file_name_lh_white = read_dir_name + '/' + fname
                        
                    elif 'pial' in fname : 
                        full_file_name_lh_pial = read_dir_name + '/' + fname
                        
                    
                    
                elif 'rh' in fname : 
                    if 'white' in fname : 
                        full_file_name_rh_white = read_dir_name + '/' + fname
                    elif 'pial' in fname : 
                        full_file_name_rh_pial = read_dir_name + '/' + fname

        
        print(f"-----------------SUBJECT {cnt+1} LH {sub_dir_name} BRAIN START----------------")
        
        lh_file_name = 'lh' + sub_dir_name
        
        lh_white = read_vtk(full_file_name_lh_white) 
        lh_pial = read_vtk(full_file_name_lh_pial)  
        get_thick_norm_and_ori(lh_file_name,lh_white,lh_pial,50)
        gc.collect()


        print(f"-----------------SUBJECT {cnt+1} RH {sub_dir_name} BRAIN START----------------")
        
        rh_file_name = 'rh' + sub_dir_name

        rh_white = read_vtk(full_file_name_rh_white)  
        rh_pial = read_vtk(full_file_name_rh_pial) 
        get_thick_norm_and_ori(rh_file_name,rh_white,rh_pial,50)
        gc.collect()   
        
        
        cnt += 1
        
        
    








