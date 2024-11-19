import threading

event = threading.Event()

# 重置代码中的 event 对象，使得所有的该 event 对象都处于一个待命的状态
event.clear()

# 阻塞线程，让线程处于一个阻塞的状态，等待 event 指令
event.wait()

# 发送 event 指令，使得所有的设该 event 事件的线程执行
event.set()