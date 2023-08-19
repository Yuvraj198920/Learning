import threading

class Logger:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(Logger, cls).__new__(cls)
                    cls._instance.log_file = "app.log"
        return cls._instance
    
    def log(self, message):
        with open(self.log_file, 'a') as f:
            f.write(message + '\n')

# Usage
def worker_thread(logger):
    for _ in range(5):
        logger.log(threading.current_thread().name + " is working.")

logger_instance = Logger()

threads = []
for i in range(3):
    thread = threading.Thread(target=worker_thread, args=(logger_instance,))
    threads.append(thread)
    thread.start()

# for thread in threads:
#     thread.join()

print("Logging completed.")