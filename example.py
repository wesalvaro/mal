import mal

mock = mal.Mock()

print mock
print mock()
print mock.fake_method()

print mock._calls
print mock.foo()

expect(mock.foo.bar.baz).to_receive('hello').and_return('world')

