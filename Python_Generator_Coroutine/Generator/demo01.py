def generators():
    print("hello")
    yield 5
    print("world")

print(type(generators()))

generators().__next__()
generators().__next__()
generators().__next__()
generators().__next__()
generators().__next__()
generators().__next__()
print(generators().__next__())