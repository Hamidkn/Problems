from tasks import Task_Manager
import os

if __name__ == '__main__':

    path = os.path.join('C:\\','Program Files','Google','Chrome','Application','chrome.exe')
    time_interval = 2
    columns = 'name,cpu_usage,memory_usage,status'
    sort_by = 'memory_usage'
    n = 10
    process = Task_Manager(path, time_interval)
    result = process.run(columns, sort_by, n)