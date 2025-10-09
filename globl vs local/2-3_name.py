def greet(name:str):
    def message():
        nonlocal name
        name=f'Hello {name}!'
    message()
    print(name)
    
greet('Arif')