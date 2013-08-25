class Call(object):

  def __init__(self, *args, **kwargs):
    self.args = args
    self.kwargs = kwargs


class Mock(object):

  def __init__(self):
    self._calls = []
    self._attrs = {}
    self._expected_calls = {}

  def __getattr__(self, name):
    if name in self._attrs:
      return self._attrs[name]
    else:
      return Mock()

  def __call__(self, *args, **kwargs):
    call = Call(*args, **kwargs)
    self._calls.append(call)
    if call in _expected_calls:
      return self._expected_calls[call]
    else:
      return Mock()

  def __del__(self):
    pass


class Expectation(object):

  def __init__(self, mock):
    self._mock = mock

  def to_receive(self, attr_path):
    pass

  def and_return(self, retval):
    pass

  def and_raise(self, exception):
    pass


def expect(mock):
  return Expectation(mock)
