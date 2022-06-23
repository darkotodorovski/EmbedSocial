import requests
import json



with open(r"C:\Users\Dell\Desktop\EmbedSocial\new.json") as g:
  filter=json.load(g)

with open(r"C:\Users\Dell\Desktop\EmbedSocial\reviews.json") as f:
  data = json.load(f)



# rating=filter[0][0]
# minRating=filter[0][1]
# date=filter[0][2]
# priority=filter[0][3]

#priority text, rating, date

priority=False
minRating=3
rating="Lowest"
date="Oldest"

lista=[]
podatoci=[]

for i in range(0,len(data)):
  podatoci=[data[i]['reviewFullText'],data[i]['rating'],data[i]['reviewCreatedOnTime']]
  lista.append(podatoci)

for i in range(0,len(data)):
  if len(data[i]['reviewFullText'])>1:
    lista[i][0]=1
  else:
    lista[i][0]=0

#######
#case 1 111
if priority==True and rating=="Highest" and date=="Newest":
  lista.sort(key=lambda x: (-x[0], -x[1], -x[2]))

  # lista.sort(reverse=True)
  for i in range(0,len(lista)):
    if lista[i][1]>=minRating:
      if lista[i][0]==1:
        print(str(lista[i][1])+"-star review with text - newest first")
      else:
        print(str(lista[i][1])+"-star review without text - newest first")

########
#case 2 011
elif priority==False and rating=="Highest" and date=="Newest":
  for i in range(0,len(lista)):
    del(lista[i][0])
  lista.sort(key=lambda x: (-x[0], -x[1]))
 
  for i in range(0,len(lista)):
    if lista[i][0]>=minRating:
      print(str(lista[i][0])+"-star review - newest first")

#######
#case 3 101
elif priority==True and rating=="Lowest" and date=="Newest":
  lista.sort(key=lambda x: (-x[0], x[1], -x[2]))

  for i in range(0,len(lista)):
    if lista[i][1]>=minRating:
      if lista[i][0]==1:
        print(str(lista[i][1])+"-star review with text - newest first")
      else:
        print(str(lista[i][1])+"-star review without text - newest first")

####
#case 4 110
elif priority==True and rating=="Highest" and date=="Oldest":
  lista.sort(key=lambda x: (-x[0], -x[1], x[2]))

  for i in range(0,len(lista)):
    if lista[i][1]>=minRating:
      if lista[i][0]==1:
        print(str(lista[i][1])+"-star review with text - oldest first")
      else:
        print(str(lista[i][1])+"-star review without text - oldest first")

#case 5 001
elif priority==False and rating=="Lowest" and date=="Newest":
  for i in range(0,len(lista)):
   del(lista[i][0])
  lista.sort(key=lambda x: (x[0], -x[1]))


  for i in range(0,len(lista)):
    if lista[i][0]>=minRating:
      print(str(lista[i][0])+"-star review - newest first")

#####
#case 6 100
elif priority==True and rating=="Lowest" and date=="Oldest":
  lista.sort(key=lambda x: (-x[0], x[1], x[2]))

  for i in range(0,len(lista)):
    if lista[i][1]>=minRating:
      if lista[i][0]==1:
        print(str(lista[i][1])+"-star review with text - oldest first")
      else:
        print(str(lista[i][1])+"-star review without text - oldest first")

#####
#case 7 000
elif priority==False and rating=="Lowest" and date=="Oldest":
  for i in range(0,len(lista)):
   del(lista[i][0])
  lista.sort(key=lambda x: (x[0], x[1]))

  for i in range(0,len(lista)):
    if lista[i][0]>=minRating:
      print(str(lista[i][0])+"-star review - oldest first")
