#!/usr/bin/env python
# coding: utf-8

# This code is simple copy file structure

# In[23]:


import pandas as pd
import os
import shutil


# In[24]:


objective_folder_df = pd.read_csv('objective_files_with_acronyms.csv', sep = ',')


# Testing on small data set
# 

# In[20]:


'''
obj_df_10 = objective_folder_df[0:10].copy()
#sample files created
#print(obj_df_10.head(10))


def create_files_in_desktop(source):
    
    for index, row in obj_df_10.iterrows():
        source_path = source
        for i in range(11,0,-1):
            col_name = 'trim_'+str(i)
            if (row[col_name] != 'no name'):
                source_path = source_path+row[col_name]+'_t'+'\\'
        
        #print(path_val)
        if not os.path.exists(source_path):
            os.makedirs(source_path)
        
        #create the file 
        file_name = source_path+row['documentname']+'.'+row['fileextension']
        f= open(file_name,"w+")
        for i in range(10):
            f.write("This is line %d\r\n" % (i+1))
        f.close() 
        
#source = input('Source:') 

#create_files_in_desktop(source)

def create_files_in_xdrive1(source, destination):
    
    for index, row in obj_df_10.iterrows():
        source_path = source+'\\'
        dest_path = destination+'\\'
        
        for i in range(11,0,-1):
            dest_col_name = 'trim_'+str(i)
            source_col_name = 'trim_'+str(i)
            if (row[dest_col_name] != 'no name'):
                source_path = source_path+row[source_col_name]+'_t'+'\\'
                dest_path = dest_path+row[dest_col_name]+'\\'
        
        source_file_name = source_path+row['documentname']+'.'+row['fileextension']
        
        # adding exception handling
        
        # create the folders if not already exists
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)

        # adding exception handling
        try:
            shutil.copy(source_file_name, dest_path)
        except IOError as e:
            print("Unable to copy file. %s" % e)
        except:
            print("Unexpected error:", sys.exc_info())
            
source = input('Enter source root folder:')#'/home/santhilata/Desktop/'    
destination = input('Enter destination root folder:') #'/home/santhilata/Documents/'    
print('Given source path (top folder):- ', source)
print('Given destination path (top folder):- ', destination)
create_files_in_xdrive1(source, destination)
'''


# In[25]:


def create_files_to_xdrive(source, destination):
    
    for index, row in objective_folder_df.iterrows():
        source_path = source+'\\'
        dest_path = destination+'\\'
        
        for i in range(11,0,-1):
            dest_col_name = 'trim_'+str(i)
            source_col_name = 'parent'+str(i)
            if (row[dest_col_name] != 'no name'):
                source_path = source_path+row[source_col_name]+'\\'
                dest_path = dest_path+row[dest_col_name]+'\\'
        
        source_file_name = source_path+row['documentname']+'.'+row['fileextension']
        
        # adding exception handling
        
        # create the folders if not already exists
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)

        # adding exception handling
        try:
            print('Copying ',source_file_name,' to ',dest_path)
            shutil.copy(source_file_name, dest_path)
        except IOError as e:
            print("Unable to copy file. %s" % e)
        except:
            print("Unexpected error: ", sys.exc_info())
            
    input('Transfer Complete. press ANY KEY to close ')


# In[26]:


source = input('Enter source top folder: ') 
destination = input('Enter destination top folder: ') 
print('Given source path (top folder):- ', source)
print('Given destination path (top folder):- ', destination)

create_files_to_xdrive(source, destination)
#closeexe = input('Transfer Complete. press ANY KEY to close ')


# In[ ]:




