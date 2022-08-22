# Python program to explain the
# use of wait() method for Condition object

import threading
import time
import random

class subclass:
  # Initialising the shared resources
  def __init__(self):
    self.x = []

  def producer(self,subclass_obj, condition_obj):
      
      r = random.randint(1,3) # Selecting a random number from the 1 to 3
      print("Random number selected was:", r)
      
      # Creting r number of items by the producer
      for i in range(1, r):
        print("Producing an item, time it will take(seconds): " + str(i))
        time.sleep(i)
        
        print("Producer acquiring the lock")
        condition_obj.acquire()
        try:
          # Produce an item
          self.x.append(i)
          # Notify that an item  has been produced
          condition_obj.notify()
        finally:
          # Releasing the lock after producing
          condition_obj.release()
        
  def consumer(self,subclass_obj, condition_obj):
      condition_obj.acquire()
      while True:
        try:
          # Consume the item 
          consumed_item = self.x.pop()
          print("Consumed item: ", consumed_item)
        except:
          print("No item to consume, list empty")
          print("Waiting for 10 seconds")
          # wait with a maximum timeout of 10 sec
          value = condition_obj.wait(10)
          if value:
            print("Item produced notified")
            continue
          else:
            print("Waiting timeout")
            break
          
      # Releasig the lock after consuming
      condition_obj.release()