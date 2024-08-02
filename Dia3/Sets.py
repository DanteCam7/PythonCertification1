mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)
print(len(mi_set))
print(2 in mi_set)

otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)
###############################################
s1 = {1,2,3}
s2 = {3,4,5}
s1.add(20)
s1.remove(1)  #discard es otro que si no esta un elemento, no truena
sorteo = s1.pop() #elimina un elemento aleatorio
s3 = s1.union(s2)
print(s3)
s1.clear() #borra todoooo
