from subprocess import Popen, PIPE
from asyncio import sleep

async def get_temp():
    while True:
        p = Popen(["cat", "/sys/class/thermal/thermal_zone0/temp"], stdout=PIPE, stderr=PIPE)
    #p = Popen(["ls", "-l"], stdout=PIPE, stderr=PIPE)
        for line in p.stdout:
            s = int(line)/1000
            print('Temp:', s, "C")
        await sleep(2)

async def get_cpu_usage():
    last_idle = 0;
    last_total = 0;
    while True:
        p = Popen(["cat", "/proc/stat"], stdout=PIPE, stderr=PIPE)
        #p.stdout.readline()
        s = p.stdout.readline()        
        sp = str(s).split(" ")
        total = 0
        for j in range(2,9):
            total += int(sp[j])
        idle = int(sp[5])
        total_diff = total - last_total
        idle_diff = idle - last_idle
        print("CPU usage: ", (total_diff-idle_diff)/total_diff*100, "%")
        last_idle = idle
        last_total = total
        await sleep(2)

async def get_mem_usage():
    while True:
        p = Popen(["free", "-m"], stdout=PIPE, stderr=PIPE)
        for line in p.stdout:
            s = str(line)
            if "Mem" in s:
                sp = s.split()
                total = int(sp[1])
                used = int(sp[2])
                print("Memory usage: ", used/total*100, "%")
        await sleep(2)