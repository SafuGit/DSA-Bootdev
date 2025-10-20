from my_queue import Queue

def matchmake(queue: Queue, user):
  print(f"DEBUG START: Queue before action = {queue.items}, size = {queue.size()}")
  
  if user[1] == 'join':
    queue.push(user[0])
    print(f"DEBUG: After join, queue = {queue.items}, size = {queue.size()}")
  elif user[1] == 'leave':
    queue.search_and_remove(user[0])
    print(f"DEBUG: After leave, queue = {queue.items}, size = {queue.size()}")
  
  if queue.size() >= 4:
    print(f"DEBUG: Queue size is {queue.size()}, should match!")
    user1 = queue.pop()
    user2 = queue.pop()
    return f"{user1} matched {user2}!"
  else:
    print(f"DEBUG: Queue size is {queue.size()}, no match")
    return "No match found"
