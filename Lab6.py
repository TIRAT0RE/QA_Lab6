import subprocess
import re

server_ip = '192.168.0.1'
# 

def client (server_ip=server_ip):
	my_iperf_process = subprocess.Popen(["iperf","-t 10","-i 1","-u", "-c",server_ip],stdout=subprocess.PIPE)

	return my_iperf_process.communicate()


def parse(client_output):
	REGEXP = "(\d{1,4}.\d{1,4}-\d{1,4}.\d{1,4}) sec\s+(\d{1,4}.?\d{1,4})\s(\w?Bytes)\s+(\d{1,4}.?\d{1,4})\s\w?(bits/sec)"

	res = re.findall(REGEXP, client_output)
	l = []
	for tuple in res:
		l.append({'Interval': tuple[0],'Transfer': float(tuple[1]),'Transfer_rate': tuple[2],'Bandwidth': float(tuple[3]),'Bandwidth_rate': tuple[4]})
	return l

result, error = client()
result = result.decode('utf-8')
print(result)
result_list = parse(result)
	
if error:
	print(error)
else:
	for value in result_list:
		if float(value['Transfer']) > 128:
			print(value)
