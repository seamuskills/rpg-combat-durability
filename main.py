import random
combat = False
green = "\033[32m "
white = '\033[37m '
red = '\033[31m '
class Weapon:
	def __init__(self,hitchance,mindamage,maxdamage,name,attackone,attacktwo,attackthree,durability):
		self.hitchance = hitchance
		self.mindamage = mindamage
		self.maxdamage = maxdamage
		self.name = name
		self.attacktext = [attackone,attacktwo,attackthree]
		self.dur = durability
		self.maxdur = durability

class Creature:
	def __init__(self,hp,ac,weapon,name,coins,maxhp):
		self.hp = hp
		self.ac = ac
		self.weapon = weapon
		self.name = name
		self.maxhp = maxhp
		self.coins = coins
	def attack(self,enemy):
		if combat == True:
			damage = random.randint(self.weapon.mindamage,self.weapon.maxdamage)
			if enemy.ac > self.weapon.hitchance:
				enemy.hp -= round(damage - (damage * enemy.ac),1)
			else:
				enemy.hp -= round(damage - ((damage * enemy.ac)/2),1)
			if enemy.hp <= 0:
				if enemy == player:
					print("Game Over")
				else:
					enemy.hp = enemy.maxhp
				print(enemy.name + " defeated")
				self.hp += round((self.maxhp - self.hp)/2,1)
				print(self.name + " healed half the lost hp back for winning the fight (" + str(round(self.hp,1)) +"hp)")
				self.coins += enemy.coins
				return False
			else:
				return True

stick=Weapon(0.1,5,20,"Stick","You poke it with a stick! It was slightly annoyed.","You plunge the stick into its flesh! It wasnt impressed.","As the stick went into its chest, it laughed at you!",10000000)
sword=Weapon(0.3,15,35,"Sword","You swing your sword peircing its skin!","As you plunge your blade into its stomach, it yells at you!","You swing the sword with all your might! The hit proved effective.",25)
ensword=Weapon(0.3,30,50,"Enchanted Sword","The sword seems to cut the enemy unusually well.","It seems that the enchanted sword cuts flesh and bone with little effort.","With a mighty strike the enchanted sword cleaves through the enemy!",37)
bow=Weapon(0.3,20,35,"Bow","Your bow shot hits! The enemy yelps at the arrow imbedded in it!","Your arrow wooshes through the air and embeds in your enemy!","Those archery classes really paid off!",75)
throwdarts=Weapon(0.3,75,135,"throwing darts","As the dart embedds into your enemy, you realize that they do way more damage then you thought.","Your accuracy is impeccable!","The enemy doesn't seem intimidated untill you sink a dart into them.",75)

weapons = [stick,sword,ensword,bow,throwdarts]
inv = [stick]

skeleton = Creature(20,0.1,bow,"Skeleton",100,20)
skeleton.fleechance = 0.4
zombie = Creature(120,0,stick,"Zombie",100,120)
zombie.fleechance = 0.1
zomknight = Creature(80,0.4,sword,"Zombie Knight",300,80)
zomknight.fleechance = 0.2
armoredskeleton = Creature(60,0.5,bow,"Armored Skeleton",250,60)
armoredskeleton.fleechance = 0.4
zomnin=Creature(100,0.1,throwdarts,"Zombie Ninja",500,100)
zomnin.feechance = 0.9
armoredninja=Creature(100,0.45,throwdarts,"Armored Zombie Ninja",1000,100)
armoredninja.fleechance=0.8
giant=Creature(500,0.5,sword,"Giant Zombie",2000,250)
giant.fleechance = 0.2
ghost=Creature(100,0.9,stick,"G h o s t",2500,50)
ghost.fleechance = 1
enghost=Creature(100,0.9,ensword,"G h o s t with enchanted sword",2500,50)
enghost.fleechance = 1
boss=Creature(1000,0,throwdarts,"Angry Elephant",100000000,100000000000000)
boss.fleechance = 1
enemies = [skeleton,zombie,zomknight,armoredskeleton,zomnin,armoredninja,giant,ghost,enghost,boss]
player = Creature(100,random.randint(10,25)/100,stick,input("name your hero\n"),0,100)
player.xp = 0
player.level = 1
player.food=3
if player.name == "sdccc":
	player.coins = 10000000
	print(green + "cash cash cash added ;)" + white)
	player.name = input("name your hero... again\n")
if player.name == "sdhrd":
	difficulty = 2
	print(red + "hard mod activated!" + white)
	player.name = input("name your hero... again\n")
else:
	difficulty = 1
print("your stats:")
print("health: " + str(player.hp))
print("armor class: " + str(player.ac))
print("weapon: " + str(player.weapon.name))

foodcost = 50

while True:
	combat = True
	enemymin = player.level - 3
	if enemymin < 0:
		enemymin = 0
	enemy = enemies[random.randint(enemymin,player.level)]
	print(green + "an " + enemy.name + " has engaged" + white)
	while combat:
		action = input("attack, flee, or heal\n")
		if action == "attack":
			print(green + player.weapon.attacktext[random.randint(0,2)] + white)
			combat = player.attack(enemy)
			player.weapon.dur -= 1 * difficulty
			if player.weapon != stick:
				print("your weapon has " + str(player.weapon.dur) + "/" + str(player.weapon.maxdur) + " durability left")
			if player.weapon.dur <= 0:
				print(red + player.name + "'s " + player.weapon.name + " broke!" + white)
				player.weapon.dur = player.weapon.maxdur
				inv.remove(player.weapon)
				player.weapon = inv[random.randint(0,len(inv)-1)]
				print(player.name + " equipped " + player.weapon.name + " from their inventory")
		if action == "heal":
			if player.food >= 1:
				player.food -= 1
				player.hp = player.maxhp
				print("the food was really good and healed you to full hp")
			else:
				print("you wasted your turn looking for food that you dont have")
		if action == "flee":
			flee = random.randint(player.level,100)
			if flee > (enemy.fleechance/100):
				combat = False
		if combat:
			combat = enemy.attack(player)
			print(enemy.name + "'s hp: " + str(enemy.hp))
			print(player.name + "'s hp: " + str(player.hp))
			print(player.name + " has " + str(player.food) + " food")
	if player.hp <=0:
		print(red + "Game Over" + white)
		break
	elif action != "flee":
		player.xp += enemy.maxhp
		if player.xp > player.level * 100:
			player.level += 1
			player.maxhp += player.level*10
			player.hp = player.maxhp
			print(green + player.name + " leveled up to level " + str(player.level) + white)
			player.xp = 0
			player.coins += 100*player.level
			player.ac += round(player.ac*0.1,2)
			print(player.name + "'s ac increased to " + str(player.ac))
			if player.level >= 10:
				print(green + "Congrates you won" + white)
				break
	shop = True
	while shop:
		print(player.name + " has " + str(player.coins) + "g")
		print("welcome to the shop would you like to buy something before the next fight?" + green)
		if player.weapon != sword:
			if sword in inv:
				print("equip sword")
			else:
				print("sword:200g")
		if player.weapon != ensword:
			if ensword in inv:
				print("equip enchanted sword")
			else:
				print("enchanted sword:400g ")
		if player.weapon != bow:
			if bow in inv:
				print("equip bow")
			else:
				print("bow:700g")
		if player.weapon != throwdarts:
			if throwdarts in inv:
				print("equip throwing darts")
			else:
				print("throwing darts:1250g")
		print("food: " + str(foodcost) + "g")
		print("exit" + white)
		action = input("")
		if action == "inv":
			print(inv)
		if action == "exit":
			shop = False
		if sword in inv:
			haveitem = True
		else:
			haveitem = False
		if action == "sword" and player.weapon != sword and (player.coins >= 200 or haveitem):
			player.weapon = sword
			if haveitem:
				print(green+"sword equipped"+white)
				player.weapon=sword
			else:
				player.coins -= 200
				print(green + "Perchased and equipped sword!"+white)
				inv.append(sword)
		if bow in inv:
			haveitem = True
		else:
			haveitem = False
		if action == "bow" and player.weapon != bow and (haveitem or player.coins >=700):
			player.weapon = bow
			if haveitem:
				print(green+"bow equipped"+white)
				player.weapon=bow
			else:
				player.coins -= 700
				print(green + "Perchased and equipped bow!"+white)
				inv.append(bow)
		if ensword in inv:
			haveitem=True
		else:
			haveitem=False
		if action == "enchanted sword" and player.weapon != ensword and (haveitem or player.coins >= 400):
			player.weapon = ensword
			if haveitem:
				print(green+"enchanted sword equipped"+white)
				player.weapon=ensword
			else:
				player.coins -= 400
				print(green + "Perchased and equipped enchanted sword!"+white)
				inv.append(ensword)
		if throwdarts in inv:
			haveitem=True
		else:
			haveitem=False
		if action == "throwing darts" and player.weapon != throwdarts and (haveitem or player.coins >= 1250):
			player.weapon = throwdarts
			if haveitem:
				print(green+"throwing darts equipped"+white)
				player.weapon=throwdarts
			else:
				player.coins -= 1250
				print(green + "Perchased and equipped throwing darts!"+white)
				inv.append(throwdarts)
		if action == "food" and player.coins >= foodcost:
			player.food += 1
			player.coins -= foodcost
			foodcost += int(foodcost / 2)*difficulty
			print(green + "Perchased a delicious meal!" + white)