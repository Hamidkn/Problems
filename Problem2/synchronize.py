import os
import sys
import shutil
import logging

class sync(object):
    def __init__(self, source_path, replica_path, log_file, action):
        self.source_path = source_path
        self.replica_path = replica_path
        logging.basicConfig(filename=log_file,format='%(asctime)s %(message)s')
        self.logger = logging.getLogger() 
        self.logger.setLevel(logging.DEBUG)
        self.action = action
    
    def look_into(self):
        for folderName, subfolders, filenames in os.walk(self.source_path):
            self.logger.info('The current folder is ' + folderName)
            for subfolder in subfolders:
                self.logger.info('SUBFOLDER OF ' + folderName + ': ' + subfolder)
                try:
                    new_path = folderName.replace(self.source_path,self.replica_path)
                    os.mkdir(new_path+"\\"+subfolder)
                except:
                    self.logger.info("Folder Exists:" + subfolder)
            if self.action == 'c':
                self.logger.info("Copying file...")
                for filename in filenames:
                    new_path = folderName.replace(self.source_path,self.replica_path)
                    file = folderName + '\\'+ filename
                    self.copy(file, new_path)
            elif self.action == 'r':
                self.logger.info("Remove file...")
                self.remove(self.replica_path)

    def copy(self, file, new_path):
        try:
            self.logger.info("FROM: " + file + " TO: " + new_path)
            shutil.copy(file, new_path)
        except:
            self.logger.info("File Exists.")
    
    def remove(self, file):
        try:
            shutil.rmtree(file)
        except:
            self.logger.info("File not exist.")