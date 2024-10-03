import random
MUTATION_RATE = 0.4

l = []

for i in range (5):
    x = random.randint(0,99)
    y = random.randint(0,99)
    l.append((x,y))

 
print ("first list", l)
# nb_bees_to_mutate = int(len(l) * MUTATION_RATE)

# print(nb_bees_to_mutate, "nb")
# l = random.sample(l, nb_bees_to_mutate)
# print(l, "random, sample")

# for bee in l:
a = random.randint(0,len(l)-1)
b = random.randint(0,len(l)-1)
# print(a,b)
if a != b:
    # print(l[a], "A avant")
    # print(l[b],"B avant")
    l[a], l[b] = l[b], l[a]
    # print(l[a], "A après")
    # print(l[b],"B après")

    

print("List mutate", l)