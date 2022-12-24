import psutil # pip install psutil
proc_name = 'Google Chrome.exe'
for proc in psutil.process_iter():
    if proc.name() == proc_name:
        print("Process {}  started".format(proc_name))
    else:
        print("Процесс запущен!")