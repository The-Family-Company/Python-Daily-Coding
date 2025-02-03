class sisters:
    color=""
    food=""
    def drawing(self):
        print("i am artist")       
    def embroid(self):
        print("my hobby is embroiding")

hawwa=sisters()
aysha=sisters()

hawwa.color= "pink is my favorite"
aysha.color="i love red"

hawwa.food="biriyani"
aysha.food="ghee rice"

print('hawwa')
print(hawwa.color)
print("food:",hawwa.food)
hawwa.drawing()
print()
print('aysha')
print(aysha.color)
print("food:",aysha.food)
aysha.embroid()

