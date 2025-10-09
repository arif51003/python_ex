def out():
    name="Hello!"
    print(name)
    def inner():
        nonlocal name
        print(name)
    inner()
out()