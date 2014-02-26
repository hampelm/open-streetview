# import serial
# import threading
# import time
#
# class Timer:
#     def __init__(self):
#         self.count = 0
#         self.counter_thread = threading.Thread(target=self.counter)
#         self.counter_thread.daemon = True
#         self.counter_thread.start()
#         # self.counter_thread.join()
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, a, b, c):
#         print "Exiting"
#
#     def counter(self):
#         while True:
#             self.count += 1
#             time.sleep(2)
#
#
# with Timer() as timer_obj:
#     while True:
#         print timer_obj.count
#         time.sleep(3)


