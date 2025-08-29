class CounterContext:
  def __init__(self):
    self.count = 0
    self.subscribers = []
  
  def subscribe(self, callback):
    self.subscribers.append(callback)

  def increment(self):
    self.count += 1
    self._update()

  def decrement(self):
    self.count -= 1
    self._update()
  
  def _update(self):
    for cb in self.subscribers:
      cb()