import random, time, json,os
from encode import ec
try:
	os.system("clear")
except:
	os.system("cls")
del os

#see message.txt!

combat = False
green = "\033[32m "
white = '\033[37m '
red = '\033[31m '

def sprint(text, wait=0.05):
	for i in text:
		print(i,end="",flush = True)
		time.sleep(wait)
	print("")

achievements = []
class Acheivment:
	def __init__(self,maxprogress,name):
		self.acheivmentpoints = 0 + acheivments * 5
		self.progress = 0
		self.maxprogress = maxprogress
		self.name = name
		self.completed = False
		achievements.append(self)
	def maxachive(self, acheivmentpoints):
		if acheivmentpoints == 50:
			maxachievments = True
	def checkachieved(self,currpoints):
		if self.progress >= self.maxprogress and not self.completed:
			print(green + "you got an achivement: " + self.name,end = "\n\n")
			currpoints += self.acheivmentpoints
			player.coins += 100
			saveach(self.name)
			self.completed = True
			return currpoints
		else:
			return currpoints

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
	def __init__(self,hp,ac,weapon,name,coins,maxhp, player=False):
		self.hp = hp
		self.ac = ac
		self.weapon = weapon
		self.name = name
		self.maxhp = maxhp
		self.coins = coins
		self.player = player
	def attack(self,enemy):
		if combat == True:
			damage = random.randint(self.weapon.mindamage,self.weapon.maxdamage)
			if self.player == True:
				for i in achievements:
					if i.completed == True:
						damage += 1#gift 1 pts damage for every achievement
			if random.randint(5,50) == 1:
				damage *= 3
				print(green + "CRITICAL HIT!" + white)#crits
			if enemy.ac > self.weapon.hitchance:
				enemy.hp -= round(damage - (damage * enemy.ac),1)
			else:
				enemy.hp -= round(damage - ((damage * enemy.ac)/2),1)
			if enemy.hp <= 0:
				if enemy == player:
					sprint("Game Over")
				else:
					enemy.hp = enemy.maxhp
				sprint(enemy.name + " defeated")
				self.hp += round((self.maxhp - self.hp)/2,1)
				sprint(self.name + " healed half the lost hp back for winning the fight (" + str(round(self.hp,1)) +"hp)")
				self.coins += enemy.coins
				return False
			else:
				return True

foods = []

class Food:
	def __init__(self,hp,name,text,cost,perc=False):
		self.hp = hp
		self.name = name
		self.text = text
		self.perc = perc
		self.cost = cost
		self.ammount = 0
		if perc == True:
			hp //= 100
		foods.append(self)

steak = Food(100,"steak","The steak was cooked perfectly.",300,True)
steak.ammount = 3
apple = Food(20,"apple","The apple was good but isn't very satisfying.",50)
pork = Food(75,"porkchop","The pork was amazing!",150,True)
chicken = Food(75,"chicken leg","The chicken leg was great and satisfying!",100)
rsteak = Food(75,"raw steak","The raw steak was not very good for you.",150)
rpork = Food(-30,"raw pork","It is not good for you at all, maybe cook it next time.",50)
rchicken = Food(-50,"Raw chicken leg","Salmanila is not very health...",35)
cookie = Food(10,"cookie","The cookie was really good but not very satisfying.",10,True)

cg = input("see change log?(y/n)\n")
print("")
if cg == "y":
	cg = open('change.txt', "r")
	changed = cg.read()
	print(changed)
	cg.close()
	print("")

stick=Weapon(0.1,5,20,"Stick","You poke it with a stick! It was slightly annoyed.","You plunge the stick into its flesh! It wasnt impressed.","As the stick went into its chest, it laughed at you!",10000000)
sword=Weapon(0.3,15,35,"Sword","You swing your sword peircing its skin!","As you plunge your blade into its stomach, it yells at you!","You swing the sword with all your might! The hit proved effective.",25)
ensword=Weapon(0.3,30,50,"Enchanted Sword","The sword seems to cut the enemy unusually well.","It seems that the enchanted sword cuts flesh and bone with little effort.","With a mighty strike the enchanted sword cleaves through the enemy!",37)
bow=Weapon(0.3,20,35,"Bow","Your bow shot hits! The enemy yelps at the arrow imbedded in it!","Your arrow wooshes through the air and embeds in your enemy!","Those archery classes really paid off!",75)
throwdarts=Weapon(0.3,75,135,"throwing darts","As the dart embedds into your enemy, you realize that they do way more damage then you thought.","Your accuracy is impeccable!","The enemy doesn't seem intimidated untill you sink a dart into them.",50)
adambow=Weapon(0.5,80,145,"adamantium bow","You hit the enemy with the arrow, It seemed effective","your arrow peirces them with little effort!","the enemy was mortally wounded by your attack",100)
powersword=Weapon(0.5, 100, 150, "power sword","You swing the Power sword and dig it into the creature.","The enemy is impaled by your sword.","The sword goes into your enemy's chest, it's injured.", 100)
tnt=Weapon(1,300,650,"tnt","You feel the shockwave pulse through your body!","Your ears ring at the massive explosion.","You chuck the tnt at the enemy, you shield your eyes from the bright blast.",0)
hsknife = Weapon(1,30,50,"Heat seeking knife","You miss but the knife htis anyway.","How does this even work!","You almost strike yourself, but the knife guides your hand to the enemy!",30)
luckystick=Weapon(0.7,300,1000,"lucky stick","Your stick feels lucky!","You feel the luck in your bones!","Does fortune favor you?",random.randint(10,15))#this stick cant be bought, it can be found every combat, but its only a very slim chance of finding it. its a fun thing that can make each run just that extra bit unique.

weapons = [sword,ensword,bow,throwdarts,adambow,powersword]
inv = [stick]
foodinv = []

acheivments = 0
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
giantskeleton=Creature(200,0.5,sword,"Giant Skeleton", 1500, 300)
giantskeleton.fleechance = 2
phantom=Creature(500,0.75,sword,"Phantom", 1000, 500)
phantom.fleechance = 0.2
assasain=Creature(750,0.75,ensword,"Assasain", 750, 1000)
assasain.fleechance = 0.5
elephant=Creature(1000,0,throwdarts,"Angry Elephant",2000,
1000)
elephant.fleechance = 1
crazedbear=Creature(750,0.5, powersword, "Crazed Bear", 3000, 750)
crazedbear.fleechance = 0.1
madman=Creature(1000,0.6, powersword, "Mad Man", 5000, 1000)
madman.fleechance = 0.2
wrestler = Creature(1250, 0, sword, "Wrestler", 7500, 1250)
wrestler.fleechance = 0.1
enemies = [skeleton,zombie,zomknight,armoredskeleton,zomnin,armoredninja,giant,ghost,enghost, giantskeleton, phantom, assasain,wrestler, elephant, crazedbear, madman]
maxlevel = len(enemies)-1



player = Creature(100,random.randint(10,25)/100,stick,input("name your hero\n"),0,100,True)
player.ring = None
player.xp = 0
player.level = 1
foodinv = [steak]

cheat = True
cheated = False
difficulty = 1
while cheat:
	cheat = False
	if player.name == "sdccc":
		player.coins = 100000000000000000000000
		sprint(green + "cash cash cash added ;)" + white)
		player.name = input("name your hero... again\n")
		cheat = True
		cheated = True
	if player.name == "sdhrd":
		difficulty = 2
		sprint(red + "hard mode activated! >:)" + white)
		player.name = input("name your hero... again\n")
		cheat = True
	if player.name == "sddqd":
		player.ac = 1
		sprint(green + 'degrelessness mode activated' + white)
		player.name = input("name your hero... again\n")
		cheat = True
		cheated = True
	if player.name == "sddark":
		white = '\033[30m'
		sprint(white + "dark mode activated")
		player.name = input("name your hero... again\n")
		cheat = True
	if player.name == "sdkfa":
		sprint(green + "weapons added" + white)
		inv += weapons 
		player.name = input("name your hero... again\n")
		cheat = True
		cheated = True
	if player.name == "sdclev":
		player.level = int(input("type a number for your level\n"))
		if player.level > (maxlevel-1):
			player.level = maxlevel-1
		if player.level < 0:
			player.level = 0
		for i in range(0,player.level):
			player.maxhp += i*10
		player.hp = player.maxhp
		player.xp = 0
		player.coins += 100*player.level
		sprint("you are now level "+str(player.level))
		player.name = input("name your hero... again\n")
		cheat = True
		cheated = True
	if player.name == "sdbjd":
		player.weapon = hsknife
		inv.append(player.weapon)
		sprint(green + "Futuristic tech equipped." + white)
		player.name = input("name your hero... again\n")
		cheat = True

#achievements
#get 100 kills
kill100 = Acheivment(100,"Super Killer")
#get 1000 kills
kill1000 = Acheivment(1000,"Mega Killer,")#I wonder if this is even possible...
#get all weapons
Arsenal = Acheivment(len(weapons),"A Mighty Arsenal!")
#win the Game
Champion = Acheivment(1,"You are the champion, my friend.")
#win the game (hard mode)
Hwin = Acheivment(1,"Escaping Doom!")

print("use the same name next time to load acheivment progress.\n type del before the name with no space in between the name and the del to delete progress")
with open("saves.json","r") as f:
	saves = json.loads(f.read())
if "del" in player.name:
	delete = input("are you sure you want to delete progress (y/n)\n")
	if delete == "y":
		tobedel = player.name
		tobedel = ec(tobedel.replace("del",""))
		if tobedel in saves:
			del saves[tobedel]
			with open("saves.json","w") as f:
				f.write(json.dumps(saves))
			print("progress deleted")
		else:
			raise NameError("No file by that name exists.")
	else:
		print("progress not deleted")
	sprint("ending program",0.1)
	exit()
if ec(player.name) in saves:
	save = saves[ec(player.name)]
	for i in range(len(achievements)):
		if achievements[i].name in save:
			an = achievements[i].name
			if save[an] == True:
				achievements[i].completed = True
				player.coins += 100
		else:
			save[achievements[i]] = False
	if not cheated:
		dosave = "y"
	else:
		print(red + "This game will not count toward progress as cheats have been\n used!" + white)
		dosave = "n"
	sprint("welcome back " + player.name,0.2)
else:
	if not cheated:
		dosave = input("save your acheivment progress? (y/n)\n")
		if dosave == "y":
			saves[ec(player.name)] = {}
			for i in range(len(achievements)):
				saves[ec(player.name)][achievements[i].name] = False
			with open("saves.json","w") as f:
				f.write(json.dumps(saves))
			print(green + "save file made!" + white)
		else:
			print("this game will not count toward progress then")
	else:
		print(red + "This game will not count toward progress as cheats have been\n used!" + white)
		dosave = "n"
achievedpoints = 0

def saveach(ach):
	if dosave == "y":
		with open("saves.json","w") as f:
			saves[ec(player.name)][ach] = True
			f.write(json.dumps(saves))
print(green)
sprint("your stats:")
sprint("health: " + str(player.hp))
sprint("armor class: " + str(player.ac))
sprint("weapon: " + str(player.weapon.name))
sprint(white)
repaircost = 5

while True:
	combat = True
	enemymin = player.level - 3
	if enemymin < 0:
		enemymin = 0
	enemy = enemies[random.randint(enemymin,player.level)]
	sprint(green + "an " + enemy.name + " has engaged" + white)
	while combat:
		action = input("attack, flee, change weapon, or heal\n")
		action = action.lower()
		if action == "attack":
			sprint(green + player.weapon.attacktext[random.randint(0,2)] + white)
			combat = player.attack(enemy)
			if player.weapon != tnt:
				player.weapon.dur -= 1 * difficulty
				if player.weapon != stick:
					sprint("your weapon has " + str(player.weapon.dur) + "/" + str(player.weapon.maxdur) + " durability left")
			else:
				player.weapon.dur -= 1
				print("you have " + str(tnt.dur) + " tnt left")
			if player.weapon.dur <= 0:
				if player.weapon != tnt:
					sprint(red + player.name + "'s " + player.weapon.name + " broke!" + white)
				else:
					sprint(red + player.name + " ran out of tnt" + white)
				player.weapon.dur = player.weapon.maxdur
				inv.remove(player.weapon)
				player.weapon = inv[random.randint(0,len(inv)-1)]
				sprint(player.name + " equipped " + player.weapon.name + " from their inventory")
		if action == "heal":
			if len(foodinv) > 0:
				for i in foodinv:
					print(i.name + ": " + str(i.ammount))
				action = input("which food?\n")
				for i in foodinv:
					if i.name.lower() == action.lower():
						i.ammount -= 1
						if i.ammount < 0:
							foodinv.remove(i)
					
					player.hp += i.hp
					print(i.text)
			else:
				sprint("you wasted your turn looking for food that you dont have")
		if action == "flee":
			flee = random.randint(player.level,100)
			if flee > (enemy.fleechance*100):
				combat = False
				print(green + "you ran away gaining no xp" + white)
			else:
				print(red + "your attempts at running fall short." + white)
		if action == "change weapon":
			print("\nyour inventory: ",end="")
			for i in range(len(inv)):
				if i < len(inv)-1:
					print(inv[i].name,end=", ")
				else:
					print(inv[i].name,end="\n")
			action = input("which weapon to equip?\n")
			for i in inv:
				if action.lower() == i.name:
					player.weapon = i
					print(green + "equipped " + i.name + white,end="\n\n")
					break
				if i == inv[-1]:
					print(red + "you ruffle through your bag for a weapon that doesn't exist...\n" + white)
		if combat:
			combat = enemy.attack(player)
			sprint(enemy.name + "'s hp: " + str(enemy.hp))
			sprint(player.name + "'s hp: " + str(player.hp))
	if player.hp <=0:
		sprint(red + "Game Over" + white)
		break
	elif action != "flee":
		if random.randint(1,100) > 98:
			inv.append(luckystick)
			print(green + "You found the lucky stick!" + white)
		kill100.progress += 1
		achievedpoints = kill100.checkachieved(achievedpoints)
		kill1000.progress += 1
		achievedpoints = kill1000.checkachieved(achievedpoints)
		player.xp += enemy.maxhp
		if player.xp > player.level * 100:
			player.level += 1
			player.maxhp += player.level*10
			player.hp = player.maxhp
			sprint(green + player.name + " leveled up to level " + str(player.level) + white)
			player.xp = 0
			player.coins += 100*player.level
			player.ac += round(player.ac*0.1,2)
			sprint(player.name + "'s ac increased to " + str(player.ac))
			if player.level >= maxlevel:
				sprint(green + "Congrats you won" + white)
				Champion.progress += 1
				achievedpoints = Champion.checkachieved(achievedpoints)
				if difficulty == 1:
					sprint(red + "next time try hard mode >:D (name your hero sdhrd!). durability goes away twice as fast and food cost grows way quicker! Are you up to the challenge?" + white)
				if difficulty == 2:
					Hwin.progress = 1
					achievedpoints = Hwin.checkachieved(achievedpoints)
					sprint(green + "great job! Have some fun with a lot of money just name yourself sdccc! you can even make it hard mode and give yourself the money cheat! have fun :)" + white)
				break
	shop = True
	while shop:
		print(player.name + " has " + str(player.coins) + "g")
		sprint("welcome to the shop would you like to buy something before the next fight?" + green)
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
		if player.weapon != adambow:
			if adambow in inv:
				print("equip adamantium bow")
			else:
				print(adambow.name + ":1375g")
		if player.weapon != powersword:
			if powersword in inv:
				print("equip power sword")
			else:
				print(powersword.name + ":2000g")
		print("tnt: 650g (you have: " + str(tnt.dur) + " tnt)")
		if player.weapon != luckystick:
			if luckystick in inv:
				print("equip lucky stick!")
		print("achievements")
		print("food")
		if player.weapon != stick and player.weapon != tnt:
			print("repair weapon: " + str(repaircost * (player.weapon.maxdur-player.weapon.dur)) + "g")
		print("exit" + white)
		action = input("")
		action = action.lower()
		if action == "inv":
			sprint(inv)
		if action == "exit":
			shop = False
		if sword in inv:
			haveitem = True
		else:
			haveitem = False
		if action == "sword" and player.weapon != sword and (player.coins >= 200 or haveitem):
			player.weapon = sword
			if haveitem:
				sprint(green+"sword equipped"+white)
				player.weapon=sword
			else:
				player.coins -= 200
				sprint(green + "Perchased and equipped sword!"+white)
				inv.append(sword)
		if bow in inv:
			haveitem = True
		else:
			haveitem = False
		if action == "bow" and player.weapon != bow and (haveitem or player.coins >=700):
			player.weapon = bow
			if haveitem:
				sprint(green+"bow equipped"+white)
				player.weapon=bow
			else:
				player.coins -= 700
				sprint(green + "Perchased and equipped bow!"+white)
				inv.append(bow)
		if ensword in inv:
			haveitem=True
		else:
			haveitem=False
		if action == "enchanted sword" and player.weapon != ensword and (haveitem or player.coins >= 400):
			player.weapon = ensword
			if haveitem:
				sprint(green+"enchanted sword equipped"+white)
				player.weapon=ensword
			else:
				player.coins -= 400
				sprint(green + "Perchased and equipped enchanted sword!"+white)
				inv.append(ensword)
		if throwdarts in inv:
			haveitem=True
		else:
			haveitem=False
		if action == "throwing darts" and player.weapon != throwdarts and (haveitem or player.coins >= 1250):
			player.weapon = throwdarts
			if haveitem:
				sprint(green+"throwing darts equipped"+white)
				player.weapon=throwdarts
			else:
				player.coins -= 1250
				sprint(green + "Perchased and equipped throwing darts!"+white)
				inv.append(throwdarts)
		if adambow in inv:
			haveitem=True
		else:
			haveitem=False
		if action == "adamantium bow" and player.weapon != adambow and (haveitem or player.coins >= 1375):
			player.weapon = adambow
			if haveitem:
				sprint(green+adambow.name+" equipped"+white)
			else:
				player.coins -= 1375
				sprint(green + "Perchased and equipped Adamantium bow!"+white)
				inv.append(adambow)
		if powersword in inv:
			haveitem=True
		else:
			haveitem=False
		if action == "power sword" and player.weapon != powersword and (haveitem or player.coins >= 2000):
			player.weapon = powersword
			if haveitem:
				sprint(green+powersword.name+" equipped"+white)
			else:
				player.coins -= 2000
				sprint(green + "Perchased and equipped power sword!"+white)
				inv.append(powersword)
		if action == "tnt" and player.coins >= 650:
			if not tnt in inv:
				inv.append(tnt)
			tnt.dur += 1
			player.coins -= 650
		if action == "food":
			perchaseFood = True
			while perchaseFood:
				for i in foods:
					print(green + i.name + ": " + str(i.cost) + "g" + white)
				print("exit")
				action = input("")
				for h in foods:
					if action.lower() == h.name.lower() and player.coins > h.cost:
						if not h in foodinv:
							foodinv.append(h)
						h.ammount += 1
						player.coins -= h.cost
						print("perchased " + h.name)
					if action == "exit":
						perchaseFood = False
		if (action == "repair" or action == "repair weapon") and player.coins > repaircost * (player.weapon.maxdur-player.weapon.dur) and player.weapon != stick:
			player.coins -= repaircost * (player.weapon.maxdur-player.weapon.dur)
			player.weapon.dur = player.weapon.maxdur
			repaircost *= random.randint(11,19)/10
			sprint(green + "weapon repaired to full durability!" + white)
		if action == "lucky stick":
			if luckystick in inv:
				player.weapon = luckystick
		if action == "achievements":
			print("")
			for i in achievements:
				if i.completed == True:
					print(green + i.name + white)
				else:
					print(i.name + ": " + str(i.progress) + "/" + str(i.maxprogress))
			print("")
	Arsenal.progress = len(inv)
	achievedpoints = Arsenal.checkachieved(achievedpoints)