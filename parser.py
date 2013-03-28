import query
import Queue
import threading

def load():
	servers = []

	class ServerInfo(threading.Thread):

		def __init__(self, queue):
			threading.Thread.__init__(self)
			self.queue = queue

		def run(self):
			while True:
				address = self.queue.get()
				self.query(address)
				self.queue.task_done()

		def query(self, address):
			addr = address.split(":")[0]
			port = int(address.split(":")[1])

			info = query.GetInfo(addr, port)
			if info:
				servers.append(info)

	queue = Queue.Queue()
	ips = query.GetServers()

	for i in range(40):
		t = ServerInfo(queue)
		t.setDaemon(True)
		t.start()

	for address in ips:
		queue.put(address)

	queue.join()

	return servers