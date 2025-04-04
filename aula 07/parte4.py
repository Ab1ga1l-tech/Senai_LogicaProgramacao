#kelvin e fahrehit
def converter_temp(celsius):
    kelvin = celsius + 273
    fahrehit = (((celsius*9)/5)+32)
    
    
    return ({"celsius":celsius,"kelvin":kelvin,"fahrehit":fahrehit})

res = converter_temp(30)
print(res)