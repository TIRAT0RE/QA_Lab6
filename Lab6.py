import subprocess

my_iperf_process = subprocess.Popen(["iperf3","-c","192.168.0.1","--forceflush"],stdout=subprocess.PIPE)

for line in my_iperf_process.stdout:
    print(line)
