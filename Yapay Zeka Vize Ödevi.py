#!/usr/bin/env python
# coding: utf-8

# In[37]:


""" Genetik Algoritma Minimum Ve Maksimum Değerleri Bulan Kodlar"""
"""Harun Çetin"""

#Gerekli kütüphanelerin eklenmesi
import numpy as np
import random as rnd 
import math 
import matplotlib.pylab as plt


# In[38]:


#İterasyon,popülasyon ve gen sayıları gibi değişkenlerin belirlenmesi
iterasyon=2
crosover_rate=0.50
pop_size=10
gen_size=2
fig = plt.figure()


# In[39]:


#Kromozom ve popülasyon oluşturduğumuz metodların yazılması
def create_chromosome():
    return [rnd.uniform(-10,10) for x in range(0,gen_size)]

def create_initial_population():
    return [create_chromosome() for x in range(0,pop_size)]


# In[40]:


#fitness fonksiyonunun formülize edilmesi
def fitness(cr):
    return 1/(1+abs(math.sin(cr[0])+math.sin(cr[1]*10/3)))


# In[41]:


#Olasılık hesabı
def probability(fitness_values):
    P=[]
    total=sum(fitness_values)
    for f in fitness_values:
        P.append(f/total)
    return P


# In[42]:


#Crossover metodunun oluşturulması 
def crossover(p1,p2):
    o1=[]
    o2=[]
    c=rnd.randint(1,gen_size-1)
    print("Cut point:",c)
    o1[:c]=p2[:c]
    o1[c:]=p1[c:]
    
    o2[:c]=p1[:c]
    o2[c:]=p2[c:]
    
    return o1,o2


# In[43]:


#Mutasyon metodunun oluşturulması 
def mutasyon(mut):
    temp=[]
    temp=mut[:]
    gen=rnd.uniform(-10,10)
    index=rnd.randint(0,gen_size-1)
    temp[index]=gen
    return temp


# In[44]:


#popülasyon değişkenine popülasyon oluşturulan metodun atanması ve popülasyonun oluşturulması
population=create_initial_population()
fitness_values=[]

for c in population:
    fitness_values.append(fitness(c))
epok=0
#iterasyon sayısıncac dönüş yapan kod parçacığı
while epok<iterasyon:
    P=probability(fitness_values)

    C=np.cumsum(P)

    rulet_parents=[]

    for i in range(0,len(C)):
        r=rnd.random()
        print("Random:",r)
        for j in range(0,len(C)):
            if C[j]>r: #1
                rulet_parents.append(j)
                break


    for c, f,p in zip(population,fitness_values,P):
        print(c, " ",f," ",p)
    print(C)

    print(rulet_parents)

    #crossover işlemi
    crosover_parents=[]
    k=0
    while k<pop_size:
        r=rnd.random()
        if(r<crosover_rate):
            if(rulet_parents[k] not in crosover_parents):
                crosover_parents.append(rulet_parents[k])
        k=k+1
    print("Caprazalnacak bireyler:",crosover_parents)


    if(len(crosover_parents)>=2):
        for i in range(0,len(crosover_parents)):
            for j in range (i+1, len(crosover_parents)):
                o1,o2=crossover(population[crosover_parents[i]]
                        ,population[crosover_parents[j]])
                population.append(o1)
                population.append(o2)
                fitness_values.append(fitness(o1))
                fitness_values.append(fitness(o2))

    else:
        print("Crossover icin yetrli birey gelmedi !!!")
    print("crossover sonrasi populasyon")
    for c, f in zip(population,fitness_values):
        print(c, " ",f )
        #Mutasyonun eklendiği döngü
    for r in range(0,5):
        mut=mutasyon(population[rnd.randint(0,len(population)-1)])

        population.append(mut)
        fitness_values.append(fitness(mut))

    print("mutasyon sonrasi populasyon")
    for c, f in zip(population,fitness_values):
        print(c, " ",f )

    zip_list=zip(fitness_values,population)

    sort_list=sorted(zip_list,reverse=True)

    #elitizm işlemi
    
    for f,p in list(sort_list):
        print(f," ",p)

    p=len(population)

    while(p>pop_size):
        sort_list.pop()
        p=p-1
    print("elitizm sonrasi")

    for f,p in list(sort_list):
        print(f," ",p)

    population=[]
    fitness_values=[]

    for f,p in list(sort_list):
        population.append(p)
        fitness_values.append(f)
    epok+=1

print("Son populasyon")
for c, f in zip(population,fitness_values):
        print(c, " ",f )

#değerlerin karşılaştırılması için oluşturduğum sanal noktalar
a=fitness_values[0]

b=fitness_values[0]

z=population[0]

p=population[0]


#fitness değerlerinin karşılaştırıldığı for döngüsü
for x in fitness_values:
    if a>x:
        a=x
    elif b<x:
        b=x
        
        
#popülasyon değerlerinin karşılaştırıldığı for döngüsü
for w in population:
    if z<w:
        z=w
    elif p>w:
        p=w
    
#Maks ve Min değerlerinin ekrana yazıldığı alanlar.
print("en küçük nokta: ",z,"fitness değeri: ",a)
print("en büyük nokta: ",p,"fitness değeri: ",b)


# In[45]:


#Maks ve min Noktaların grafikte gösterimi
plt.plot(z)
print("Min: ", z)


# In[46]:


plt.plot(p)
print("Max: ", p)


# In[47]:


""" Parçacık Sürü Algoritması Minimum Ve Maksimum Değerleri Bulan Kodlar"""
"""Harun Çetin"""
import numpy as np
import random as rnd 
import math 
import matplotlib.pylab as plt


# In[48]:


#Gerekli değerlerin yazılması
iterasyon=2
current_direction=0.50
w=0.5
partical=10
velocity_fact=1
c1=1.0
c2=1.0
fig = plt.figure()


# In[49]:


#Konum metodunun oluşturulması
def create_location():
    return [(round(rnd.uniform(-10,10),2)) for x in range(0,partical)]
#Hız metodunun oluşturulması
def create_velocity():
    return [(round(rnd.randint(0,0),2)) for x in range(0,partical)]      


# In[50]:


#Fitness fonksiyonunun oluşturulması
def fitness(x):
    return round(math.sin(x)+math.sin(10/3*x),4)


# In[51]:


#Hız güncelleme fonksiyonu
def update_velocity(velocity, pBest, c1, c2, gBest, location):
    r1 = rnd.uniform(0,1.0)
    r2 = rnd.uniform(0,1.0)
    w = 0.5
    new_velocity = np.array([0.0 for i in range(len(location))])
    for i in range(0, len(location)):
        new_velocity[i] = w*velocity[i] + c1*r1*(pBest[i]-location[i])+c2*r2*(gBest-location[i])
    return new_velocity
#Konum güncelleme fonksiyonu
def update_location(velocity, location):
    new_location = location + velocity
    location = new_location
    return location


# In[52]:


location=create_location()
velocity=create_velocity()
location_max=location
velocity_max=velocity
location_min=location
velocity_min=velocity

fitness_values_min=[]
location.sort()
print("******MAX*******")
for i in range(0,iterasyon):
    print(i+1,". İterasyon")
    
    fitness_values_max=[]
    
    for c in location_max:
        fitness_values_max.append(fitness(c))

    if i == 0:
        print("İlk Hızlar: ",velocity)
        print("İlk Parçacıklar: ",location)
    
    print("Yeni Hızlar : ", velocity_max)
    print("Yeni Parçacıklar :", location_max)
    pBest_max=[]
    pBest_max = location_max
    print("Fitness'lar : ",fitness_values_max)
    print("pBest : " ,pBest_max)
    maxFitness = max(fitness_values_max)
    print("Max Fitness : " , maxFitness)
    maxIndex = fitness_values_max.index(max(fitness_values_max))
    print("maxIndex : " ,maxIndex)
    gBest = location_max[maxIndex]
    
    print("Global Best :" ,gBest)
    velocity_max = update_velocity(velocity_max, pBest_max, c1, c2, gBest, location_max)
    location_max = update_location(location_max, velocity_max)
    pBest_max = location_max
    location_max.sort()
    
print("****MİN*******")
for i in range(0,iterasyon):
    print(i+1,". İterasyon")
    
    fitness_values_min=[]
    
    for c in location_min:
        fitness_values_min.append(fitness(c))

    if i == 0:
        print("İlk Hızlar: ",velocity)
        print("İlk Parçacıklar: ",location)
    
    print("Yeni Hızlar : ", velocity_min)
    print("Yeni Parçacıklar :", location_min)
    pBest_min=[]
    pBest_min = location_min
    print("Fitness'lar : ",fitness_values_min)
    print("pBest : " ,pBest_min)
    minFitness = min(fitness_values_min)
    print("Min Fitness : " ,minFitness)
    minIndex = fitness_values_min.index(min(fitness_values_min))
    print("minIndex" ,minIndex)
    gWorse = location_min[minIndex]
    print("Min : " , gWorse)
    velocity_min= update_velocity(velocity_min, pBest_min, c1, c2, gBest, location_min)
    location_min = update_location(location_min, velocity_min)
    pBest_min = location_min
    location_min.sort()


# In[53]:


plt.plot(pBest_max,'bo')
plt.plot(gBest,'ro')


# In[54]:


plt.plot(pBest_min,'bo')
plt.plot(gWorse,'ro')


# In[ ]:


#Ga 19sn Pso 6sn

