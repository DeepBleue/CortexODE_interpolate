import os
from tqdm import tqdm
import re
from util.vtk_revise import read_vtk
from get_thickness_with_interpolate import get_thick_norm_and_ori
import gc




rootDir = './AllCortexData'


for dirName, subdirList, fileList in os.walk(rootDir):
    
    
    
    read_dir_name = dirName.replace("\\", "/")
    if 'SUBJ' in dirName : 
        subject_num = re.findall(r'\d+', read_dir_name)[0]
        
    full_file_name_lh_white = None
    full_file_name_lh_pial = None
    full_file_name_rh_white = None
    full_file_name_rh_pial  = None
    
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

    
    if full_file_name_lh_white != None and \
        full_file_name_lh_pial != None and \
        full_file_name_rh_white != None and \
        full_file_name_rh_pial != None : 
            
        ######## lh brain ########
        if 'BL' in full_file_name_lh_white :
            lh_file_name = 'SUBJ_' +  subject_num + '_lh_white_BL'
            _last = 'BL'

        elif 'FU' in full_file_name_lh_white :
            lh_file_name = 'SUBJ_' +  subject_num + '_lh_white_FU'
            _last = 'FU'
            
        print(f"-----------------SUBJECT {subject_num} LH {_last} BRAIN START----------------")
        

        file_dir = './output/white_data' 
        lh_file_name_check = lh_file_name + '.vtk'
        lh_full_path = os.path.join(file_dir, lh_file_name_check)
        if os.path.exists(lh_full_path):
            print(f'{lh_file_name_check} => already exist')
            print('continue')
        else : 
            lh_white = read_vtk(full_file_name_lh_white) 
            lh_pial = read_vtk(full_file_name_lh_pial)  
            get_thick_norm_and_ori(lh_file_name,lh_white,lh_pial,50)
            gc.collect()


        ######## rh brain ########
        if 'BL' in full_file_name_rh_white :
            rh_file_name = 'SUBJ_' +  subject_num + '_rh_white_BL'
            _last = 'BL'

        elif 'FU' in full_file_name_rh_white :
            rh_file_name = 'SUBJ_' +  subject_num + '_rh_white_FU'
            _last = 'FU'

        print(f"-----------------SUBJECT {subject_num} RH {_last} BRAIN START----------------")
        
        file_dir = './output/white_data' 
        rh_file_name_check = rh_file_name + '.vtk'
        rh_full_path = os.path.join(file_dir, rh_file_name_check)
        if os.path.exists(rh_full_path):
            print(f'{rh_file_name_check} => already exist')
            print('continue')
        else : 
            rh_white = read_vtk(full_file_name_rh_white)  
            rh_pial = read_vtk(full_file_name_rh_pial) 
            get_thick_norm_and_ori(rh_file_name,rh_white,rh_pial,50)
            gc.collect()
        

               

print('#####------- ALL PROSCESS DONE -------#####')
