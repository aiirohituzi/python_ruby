al = ['A', 'B', 'C', 'D']
print('A' in al)
print('E' in al)
print(len(al)) # 4
al.append('E')
print(al) #['A', 'B', 'C', 'D', 'E']
del(al[0])
print(al) #['B', 'C', 'D', 'E']