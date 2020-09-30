import random

units = [
			["Mimring", 150],
			["Moltenclaw", 170], 
			["Othkurik the Black Dragon", 140],
			["Nakita Agents", 120],
			["Pelloth", 100],
			["Spartacus", 200],
			["Izumi Samurai", 60],
			["Krav Maga Agents", 100],
			["Marrden Nagrubs", 30],
			["Crixus", 90],
			["Sgt. Drake Alexander", 170],
			["Deathwalker 9000", 140],
			["Raelin the Kyrie Warrior", 120],
			["Ninjas of the Northern Wind", 110],
			["Agent Carr", 100],
			["Arkmer", 50],
			["Zettian Guards", 70],
			["Major Q10", 150],
			["Frost Giant of Morh", 140],
			["Darrak Ambershard", 60],
			["Finn the Viking Champion", 80],
			["Erevan Sunshadow", 80],
			["Kozuke Samurai", 100],
			["Grimnak", 120],
			["Marro Drudge", 50],
			["Tor-Kul-Na", 220],
			["Marro Stingers", 60],
			["Thorgrim the Viking Champion", 80],
			["Tarn Viking Warriors", 50],
			["Feral Troll", 90],
			["Blastatrons", 60],
			["Evar Scarcarver", 110],
			["Warriors of Ashra", 50],
			["Raelin the Kyrie Warrior", 80],
			["Sgt. Drake Alexander", 110],
			["Sonlen", 160],
			["Marro Hive", 160],
			["Eltahale", 140],
			["Marro Stingers", 60],
			["Ulginesh", 150],
			["Deathstalkers", 100],
			["Marro Drudge", 50],
			["Airborne Elite", 110],
			["Jorhdawn", 100],
			["Horned Skull Brutes", 75],
			["Death chasers of Thesk", 55],
			["Master of the Hunt", 140],
			["Emirroon", 80],
			["Blade Gruts", 40],
			["Ne-Gok-Sa", 90],
			["Deepwyrm Drow", 70],
			["Syvarris", 100],
			["Ana Karithon", 100],
			["Shiori", 60],
			["Retiarus", 90],
			["Tandros Kreel", 120],
			["Arrow Gruts", 40],
			["Ice Troll Beserker", 85],
			["Deathreavers", 40],
			["Marrden Nagrubs", 30],
			["Marro Warriors", 50],
			["Siege", 120],
	]

def gen(unit_list, players, points):
	i = 0
	for i in range(0,players):
		remaining = points
		army = []
		while(remaining >= min_points(unit_list)):
			r = random.randint(0,len(unit_list)-1)
			if unit_list[r][1] <= remaining:
				army.append(unit_list[r])
				remaining = remaining-(unit_list[r][1])
				del unit_list[r]
		print("Player "+str(i+1)+"'s Army:")
		print(army)

	

def min_points(unit_list):
	i = 0
	points = []
	for i in range(0,len(unit_list)):
		points.append(unit_list[i][1])

	return min(points)

print("Enter the number of players: ")
players = input()
print("Enter the number of points: ")
points = input()

gen(units, int(players), int(points))


#print(units[index][attribute])