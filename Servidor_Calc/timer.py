import time
import threading
import requests


class Timer(threading.Thread):
    def __init__(self, segundos):
        self.runTime = segundos
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(self.runTime)
        response = requests.get("http://localhost:8080/region")
        print("Rodando combinação")
        print(response)


t = Timer(60)
while True:
    t.run()
