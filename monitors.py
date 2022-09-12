from subprocess import Popen, PIPE
from asyncio import sleep

async def get_temp():
    for i in range(10):
        p = Popen(["cat", "/sys/class/thermal/thermal_zone0/temp"], stdout=PIPE, stderr=PIPE)
    #p = Popen(["ls", "-l"], stdout=PIPE, stderr=PIPE)
        for line in p.stdout:
            s = int(line)/1000
            print('Temp:', s, "C")
        await sleep(2)

async def get_cpu_usage():
    total_usage = list()
    idle_time = list()
    for i in range(10):
        p = Popen(["cat", "/proc/stat"], stdout=PIPE, stderr=PIPE)
        #p.stdout.readline()
        s = p.stdout.readline()        
        sp = str(s).split(" ")
        total = 0
        for j in range(2,9):
            total += int(sp[j])
        idle_time.append(int(sp[5]))
        total_usage.append(total)
        if i > 0:
            total_diff = total_usage[i] - total_usage[i-1]
            idle_diff = idle_time[i] - idle_time[i-1]
            print("CPU usage: ", (total_diff-idle_diff)/total_diff*100, "%")
        await sleep(2)

async def get_mem_usage():
    for i in range(10):
        p = Popen(["free", "-m"], stdout=PIPE, stderr=PIPE)
        for line in p.stdout:
            s = str(line)
            if "Mem" in s:
                sp = s.split()
                total = int(sp[1])
                used = int(sp[2])
                print("Memory usage: ", used/total*100, "%")
        await sleep(2)