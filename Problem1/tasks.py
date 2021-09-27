import psutil as ps
import time
import pandas as pd
import os

class Task_Manager(object):
    def __init__(self, path, time_interval):
        self.path = path
        self.time_interval = time_interval
        self.number_of_open_handles = 0

    def get_process_info(self):
        self.processes = []

        self.pro = os.popen(self.path)
        self.proc_name = self.path.split('\\')[-1]

        for process in ps.process_iter():
            with process.oneshot():
                if process._name == self.proc_name:
                    print(process)
                    self.process_id = process._pid

                    self.name = process._name
                    try: 
                        self.memory_usage = process.memory_full_info().uss
                    except ps.AccessDenied:
                        self.memory_usage = 0
                
                    self.cpu_usage = process.cpu_percent(self.time_interval)

                    self.status = process.status()

                    self.processes.append({'process_id': self.process_id, 'name': self.name,
                    'cpu_usage': self.cpu_usage, 'status': self.status, 'memory_usage': self.memory_usage})

        return self.processes

    def generate_dataframe(self, processes, sort_by, columns):

        self.dataframe = pd.DataFrame(processes)
        self.dataframe.set_index('process_id', inplace=True)

        self.dataframe.sort_values(sort_by , inplace=True, ascending=False)

        self.dataframe = self.dataframe[columns.split(',')]
        self.dataframe.to_csv('log/log.csv')
        return self.dataframe

    def run(self, columns, sort_by, n):
        
        pro = self.get_process_info()
        dataframe = self.generate_dataframe(pro, sort_by, columns)
        self.number_of_open_handles = len(pro)

        if n == 0:
            print(dataframe.to_string())
            print(f'Numebr of open handles: {self.number_of_open_handles}')
        elif n > 0:
            print(dataframe.head(n).to_string())
            print(f'Numebr of open handles: {self.number_of_open_handles}')
        
        while True:
            pro = self.get_process_info()
            dataframe = self.generate_dataframe(pro, sort_by, columns)
            self.number_of_open_handles = len(pro)

            if len(pro) == 0:
                print(dataframe.to_string())
                print(f'Numebr of open handles: {self.number_of_open_handles}')
            elif len(pro) > 0:
                print(dataframe.head().to_string())
                print(f'Numebr of open handles: {self.number_of_open_handles}')
            
            time.sleep(0.7)
