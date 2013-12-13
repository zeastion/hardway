#!/usr/bin/python
#-*- coding:utf-8 -*-
#GUNDAM Python Game V1.0 Design

from sys import exit
import time, os, sys, tty, termios

#global GOLD, NUMBER, NAME

def weapon_1():

	print "\n 获得武器：光束枪[白]\n"
	driver()
	print " | 光束枪[白]   >>>   已装备 |\n +---------------------------+"

def weapon_2():
	print "\n 获得武器：脉冲巨剑[蓝]\n"
        driver()
        print " | 脉冲巨剑[蓝] >>>   已装备 |\n +---------------------------+"

def weapon_3():
        print "\n 获得武器：强袭战戟[橙]\n"
        driver()
        print " | 强袭战戟[橙] >>>   已装备 |\n +---------------------------+"

def weapon_null():
	print "\n 未装备武器\n"
        driver()
        print " |    武  器    >>>       无 |\n +---------------------------+"

def equipwea():
	
	global GOLD, NAK, NDF
	weapon = raw_input("\n 输入所需购买的装备编号[1-3]，或随便敲点什么放弃购买：")

	if weapon == "1":
		weapon_1()
		time.sleep(1)
		GOLD -= 700
		print "\n 资    金：-700\n 账户余额：%d" % GOLD
		time.sleep(1)
		raw_input("\n 绑定完毕，攻击力 +120 \n\n 回车确定")
		NAK = 120
		
	elif weapon == "2":
		weapon_2()
		time.sleep(1)
		GOLD -= 800
		print "\n 资    金：-800\n 账户余额：%d" % GOLD
		time.sleep(1)
                raw_input("\n 绑定完毕，攻击力 +150 \n\n 回车确定")
                NAK = 150

	elif weapon == "3":
		weapon_3()
		time.sleep(1)
                GOLD -= 1000
                print "\n 资    金：-1000\n 账户余额：%d" % GOLD
		time.sleep(1)
                raw_input("\n 绑定完毕，攻击力 +210 \n\n 回车确定")
                NAK = 210

	else:
		weapon_null()
		time.sleep(1)
		print "\n 啥也不买，抠死了 =。=\n\n 账户余额：%d" % GOLD
		NAK = 0		


def armor_1():

	print "\n 获得防具：原子盾[白]\n"
        driver()
        print " | 原子盾[白]   >>>   已装备 |\n +---------------------------+"
	
def armor_2():

	print "\n 获得防具：纳米光罩[蓝]\n"
        driver()
        print " | 纳米光罩[蓝] >>>   已装备 |\n +---------------------------+"

def armor_null():

	print "\n 未装备防具\n"
        driver()
        print " |    防  具    >>>       无 |\n +---------------------------+"


def equiparmor():

	global GOLD, NAK, NDF
        armor = raw_input("\n 输入所需购买的装备编号[1-2]，或随便敲点什么放弃购买：")

        if armor == "1":
                armor_1()
                time.sleep(1)
                GOLD -= 600
                print "\n 资    金：-600\n 账户余额：%d" % GOLD
                time.sleep(1)
                raw_input("\n 绑定完毕，防御力 +90 \n\n 回车确定")
                NDF = 90

        elif armor == "2":
                armor_2()
                time.sleep(1)
                GOLD -= 700
                print "\n 资    金：-700\n 账户余额：%d" % GOLD
                time.sleep(1)
                raw_input("\n 绑定完毕，防御力 +120 \n\n 回车确定")
                NDF = 120

        else:
                armor_null()
                time.sleep(1)
                print "\n 啥也不买，抠死了 =。=\n\n 账户余额：%d" % GOLD
                NDF = 0
	
	
def wea():
	
	print "\n 武器库开启中 ...\n"
	time.sleep(0.8)
	print """ +---------------------------+
 | 1- 光束枪[白]             |
 -----------------------------
 |    攻击力             120 |
 -----------------------------
 |    价  格             700 |
 +---------------------------+
 |                           |
 +---------------------------+
 | 2- 脉冲巨剑[蓝]           |
 -----------------------------
 |    攻击力             150 |
 -----------------------------
 |    价  格             800 |
 +---------------------------+
 |                           |
 +---------------------------+
 | 3- 强袭战戟[橙]           |
 -----------------------------
 |    攻击力             210 |
 -----------------------------
 |    价  格            1000 |
 +---------------------------+\n"""
	
	equipwea()


def armor():
	
	print "\n 防具库开启中 ...\n"
	time.sleep(0.8) 
	print """+---------------------------+
 | 1- 原子盾[白]             |
 -----------------------------
 |    防御力              90 |
 -----------------------------
 |    价  格             600 |
 +---------------------------+
 |                           |
 +---------------------------+
 | 2- 纳米光罩[蓝]           |
 -----------------------------
 |    防御力             120 |
 -----------------------------
 |    价  格             700 |
 +---------------------------+\n"""

	equiparmor()

def nak_ndf():

	global NAK, NDF

	if NAK == 0 and NDF ==0:
		ans_2()
	elif NAK > 0 and NDF == 0:
		ans_3()
	elif NAK == 0 and NDF > 0:
		ans_4()
	else:
		ans_5()


def ans_2():
	
	ans_2 = raw_input("\n 确定要裸装出击？\n -----------------\n\n 1- 是的，我相信自己的实力\n 2- 呃，还是买点装备吧\n\n Type[1or2]:")
	if ans_2 == "1":
		Add()
	elif ans_2 == "2":
		shop()
	else:
		print "\n 指令出错"
		ans_2()

def ans_3():

	ans_3 = raw_input("\n 还未装备防具\n -----------------\n\n 1- 是的，我不需要\n 2- 呃，我还是买点吧\n\n Type[1or2]:")
	if ans_3 == "1":
		Add()
	elif ans_3 == "2":
		armor()
		nak_ndf()
	else:
		print "\n 指令出错"
		ans_3()

def ans_4():
	
	ans_4 = raw_input("\n 还未装备武器\n -----------------\n\n 1- 我不需要武器\n 2- 还是买一点吧\n\n Type[1or2]:")
	if ans_4 == "1":
		Add()
	elif ans_4 == "2":
		wea()
		nak_ndf()
	else:
		print "\n 指令出错"
		ans_4()

def ans_5():
	
	print "\n 装备齐全！\n -----------------"
	Add()


def Add():

	global ak, df, ATK, DEF 

	ATK = ak + NAK
	DEF = df + NDF

	time.sleep(0.5)
	print "\n 机体平衡性测试\n ------------------- 100%\n"
	time.sleep(0.5)
	print "\n 驾驶员体能检测\n ------------------- 100%\n"
	time.sleep(0.5)
	print "\n 启动 GundamOS \n ------------------- 100%\n\n"
	time.sleep(1)
	pass_1()

def pass_1():

	passw = raw_input("\n 输入GundamOS密码查看高达第二阶段状态：")

	if passw == PASSWORD:
		time.sleep(1)
		print "\n 密码正确！\n\n 第二阶段展开 ...\n"
		time.sleep(1)
		print "\n 基础攻击力 %d + 武器攻击附加 %d ---> 完全攻击力 %d\n\n 基础防御力 %d + 防具防御附加 %d ---> 完全防御力 %d\n" % (ak, NAK, ATK, df, NDF, DEF)
	else:
		time.sleep(1)
		print "\n 密码出错！"
		time.sleep(1)
		pass_1()

def shop():

	global NAK, NDF
	
	need = raw_input(" 我需要[武器or防具]：")

	if "武器" in need:
		time.sleep(0.5)
		wea()

	elif "防具" in need:
		time.sleep(0.5)
		armor()

	else:
		print "\n Jack >>> 喂，作为男人不要乱说些莫名其妙的话！"
		shop()
	
	nak_ndf()


def say_bye():

	global GOLD
	
	ans_one = raw_input("\n Type[1or2]：")

	if ans_one == "1":
		print "\n Zeastion >>> 不用客气，这里有你的启动资金，后会有期！\n"
		raw_input(" 按下回车接过钱袋 >>>")
		print "\n *** 得到2000金币 ***"
		time.sleep(0.5)
		GOLD = 2000
		print "\n 账户余额： %d\n\n 前往武器店 ...\n" % GOLD
		time.sleep(1)
	
	elif ans_one == "2":
		print "\n Zeastion >>> 呵呵！\n"
		time.sleep(0.5)
		print "\n 系统提示：获得新手金币奖励 --- 1000\n"
		GOLD = 1000
		print " 账户余额： %d\n" % GOLD
		raw_input(" 按下回车离开")
		print "\n 前往武备店 ...\n"

	else:
		print "\n 指令出错，重新输入"
		time.sleep(0.5)
		say_bye()

	print "\n Jack >>> 你好，勇士\n Jack >>> 我是这家店的老板，我们提供 \033[1;31;40m武器\033[0m 和 \033[1;31;40m防具\033[0m，你需要哪一个？\n 系统提示：武器和防具都只能装备一件，请仔细挑选\n"
	shop()


def driver():

	information()
	print " |    驾驶员          %s |\n +---------------------------+" % NAME


def getgundam():
	
	#获取高达

	global GOLD, NUMBER
	
	print " Zeastion >>> 现在你已了解这些机体数据，选择哪一台？\n"
	NUMBER = raw_input(" 请输入选择的机体编号[1-4]：")
	#number = int(NUMBER)

	if int(NUMBER) in range (0, 5): 

		print "\n 高达信息更新\n 绑定驾驶员\n 请稍侯 ..."
		time.sleep(1.2)
	
		driver()
		time.sleep(0.5)
		raw_input("\n 绑定完毕，敲击回车确定")

		print "\n Zeastion >>> 好了 %s，接下来需要给你的高达配备各种装备\n Zeastion >>> 具体事宜武备店老板 Jack 会给你做详细介绍，再会！\n\n 1- \"多谢老Z！\"\n 2- \"真是受够你了，快走吧！\"" % NAME
		
		say_bye()
	else:
	
		print "\n 指令出错\n"
		getgundam()

def information():
	
	global NUMBER, hp, mp, ak, df	
	
	if NUMBER == "1":
		print "\n +---------------------------+\n | 1- GAT-X105 Strike Gundam |\n -----------------------------\n |    初始HP             550 |\n -----------------------------\n |    初始MP             150 |\n -----------------------------\n |    攻击力              75 |\n -----------------------------\n |    防御力              30 |\n +---------------------------+"
		hp = 500
		mp = 150
		ak = 75
		df = 30

	elif NUMBER == "2":
		print "\n +---------------------------+\n | 2- MSZ-008 ZII GUNDAM ZII |\n -----------------------------\n |    初始HP             450 |\n -----------------------------\n |    初始MP             200 |\n -----------------------------\n |    攻击力              65 |\n -----------------------------\n |    防御力              45 |\n +---------------------------+"
               	hp = 450
               	mp = 200
               	ak = 65
               	df = 45

	elif NUMBER == "3":
		print "\n +---------------------------+\n | 3- ZM-S08G ZOLO           |\n -----------------------------\n |    初始HP             500 |\n -----------------------------\n |    初始MP             180 |\n -----------------------------\n |    攻击力              70 |\n -----------------------------\n |    防御力              35 |\n +---------------------------+"
               	hp = 500
               	mp = 180
               	ak = 70
               	df = 35

	elif NUMBER == "4":
		print "\n +---------------------------+\n | 4- GN-001 Gundam Exia     |\n -----------------------------\n |    初始HP             600 |\n -----------------------------\n |    初始MP             200 |\n -----------------------------\n |    攻击力              80 |\n -----------------------------\n |    防御力              35 |\n +---------------------------+"
               	hp = 600
               	mp = 200
               	ak = 80
               	df = 35

	else:
		print "\n 输入出错\n"


def inquire():
	
	#查询高达机体信息
	
	global NUMBER

	while True:

		print " +---------------------------\n | 1- GAT-X105 Strike Gundam\n ----------------------------\n | 2- MSZ-008 ZII GUNDAM ZII\n ----------------------------\n | 3- ZM-S08G ZOLO\n ----------------------------\n | 4- GN-001 Gundam Exia\n +---------------------------\n\n"
		
		NUMBER = raw_input(" 输入所需查看的机体编号：")
		print "\n \033[5;31;47m%s\033[0m 号机体数据载入中 ...\n" % NUMBER
		time.sleep(1)
		
		information()

		again = raw_input("\n 是否查看其他机型？(y/n)")
		
		if again == "y":
			print "\n 好的，请稍候 ...\n"
			time.sleep(0.8)
		elif again == "n":
			print "\n 明白\n"
			time.sleep(0.5)
			
			getgundam()
		else:
			print "\n 指令出错，重新查看信息 \n"


def pwd_input():

	#密码收集
	
	sys.stdout.write(" 初始化GundamOS - 请设定密码：")
	pwd = []
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)	
	while True:
		try:
			tty.setraw(fd)
			newChar = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

		if newChar in '\r\n':
			break
		elif newChar in '\x7f':
			if pwd:
				del pwd[-1]
				sys.stdout.write('\b\b')
				sys.stdout.flush()

		else:
			pwd.append(newChar)
			sys.stdout.write('*')
	
	pwd = ''.join(pwd)
	print
	return pwd


def start():

	print """\n **************************
 * 欢迎来到GUNDAM设计工厂 *
 **************************\n"""

	print """ 既然你来到这里 说明你准备好了为和平而战
 下面让我们的首席教官Zeastion.Lee为你做具体说明
 ----------------------------------------------
 ----------------------------------------------
 Zeastion >>> 你好，恭喜你成为Gundam预备驾驶员,
	      接下来我需要记录你的相关信息!"""
	
	time.sleep(0.5)
	#global GOLD
	global NAME, NAK, NDF, GOLD
	GOLD = 0
	NAK = 0
	NDF = 0
	NAME = raw_input(" Zeastion >>> 姓名？")
	age = raw_input(" Zeastion >>> 年龄？")
	nationality = raw_input(" Zeastion >>> 国籍？")
	print " ----------------------------------------------\n ----------------------------------------------\n Zeastion >>> 好的，资料记录完毕，请确认后设定GundamOS启动密码"
	time.sleep(0.5)

	print """\n +---------
 | NAME    %s   
 | AGE     %s   
 | NATI    %s   
 +---------\n
 驾驶员信息记录中 ...\n""" % (NAME, age, nationality)

	time.sleep(0.5)
	global PASSWORD
	PASSWORD = pwd_input()
	
	print "\n 写入启动密码 ...\n"
	time.sleep(1)
	print " 绑定身份信息：\n"
	time.sleep(1)
	print "  指纹 --> OK\n"
	time.sleep(0.8)
	print "  血型 --> OK\n"
	time.sleep(0.6)
	print "  密码 --> OK\n"
	time.sleep(1)
	print " ---------------\n 记录完毕\n ---------------\n"   
	raw_input(" 按下回车确认以上信息\n\n ----------------------------------------------")

	print "\n Zeastion >>> 恭喜你 \033[5;31;47m%s\033[0m ，你获得了Gundam的驾驶权\n Zeastion >>> 这边是我们的仓库\n " % NAME
	time.sleep(0.5)
	print " 仓库开启中 ...\n\n"
	time.sleep(1)

	inquire()
	

start()

