def iloczynCiagu(a=1,b=4,ile=10):
    iloczyn = a
    for x in range(ile-1):
        iloczyn *= b
    return iloczyn

print(iloczynCiagu())