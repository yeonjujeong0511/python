class Pokemon:
    def __init__(self,id,name):
        self.id = id
        self.name = name

# python에서도 생성자 함수를 지원한다.

getFromJson = ['피카츄','라이츄','파이리','꼬부기','버터풀','야도란','피존투','또가스','야도킹','고오스']

pokemon_list = []

for i in range(getFromJson.__len__()):
    pokemon_list.append(Pokemon(i+1,getFromJson[i]))


for obj in range(pokemon_list.__len__()):
    print(pokemon_list[obj].__dict__)
