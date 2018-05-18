# import modules

import socket
import datetime
import uuid

# scan class

class Target():
	
	def __init__(self, host):
		
		# host
		self.host = host
		
		# reports
		self.reports = []

	def scan(self, min = 1, max = 100, timeout = 0.01):
		
		# ports
		self.ports = {}
		self.ports["min"] = min
		self.ports["max"] = max
		self.ports["open"] = []

		# start time
		self.t_start = datetime.datetime.now()
		
		# scan
		for port in range(self.ports["min"], self.ports["max"] + 1):

			try:

				scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				scanner.settimeout(timeout)
				
				status = scanner.connect_ex((self.host, port))
				if status == 0:
					self.ports["open"].append(port)
		
				scanner.close()

			except:
				pass
							
		# end time
		self.t_end = datetime.datetime.now()

		# duration
		self.t_duration = round((self.t_end - self.t_start).total_seconds(), 2)
		
		# report results
		
		self.results = {}
		self.results["scan_id"] = str(uuid.uuid4())
		self.results["url"] = self.host
		self.results["ip"] = socket.gethostbyname(self.host)
		self.results["ports_range"] = (self.ports["min"], self.ports["max"])
		self.results["ports_open"] = self.ports["open"]
		self.results["duration"] = self.t_duration
		self.reports.append(self.results)
		
	def report(self, all = True):
		
		if all:
			return self.reports

		else:
			return self.reports[-1]



ip = Target("example.com")
ip.scan()
ip.scan()
print(ip.report(False))