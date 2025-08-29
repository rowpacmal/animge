from .counter_context import CounterContext

class ContextProvider:
  def __init__(self):
    self.counter = CounterContext()

app_contexts = ContextProvider()