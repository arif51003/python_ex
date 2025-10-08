def studen_info(name,age,**details):
    s=f"{name} {age}"
    if  details:
        for key, val in details.items():
            s+=f" {key}: {val}"
    return s
print(studen_info("Arif",23,familya="Baxronov",country="Uzbekiston"))
