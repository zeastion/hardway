#!/usr/bin/python
#-*- coding:utf-8 -*-
#GUNDAM Python Game V1.0 Design

from sys import exit
import time, os, sys, tty, termios

global GOLD, NUMBER, NAME


def say_bye():

	ans_one = raw_input("\n Type[1or2]：")

	if ans_one == "1":
		print "\n Zeastion >>> 不用客气，这里有你的启动资金，后会有期！\n"
		raw_input(" 按下回车接过钱袋 >>>")
		print "\n *** 得到2000金币 ***"
		time.sleep(0.5)
		GOLD = 2000
		print "\n 账户余额： %d\n 前往武器店 ...\n" % GOLD
		time.sleep(1)
	
	elif ans_one == "2":
		print "\n Zeastion >>> 呵呵！\n"
		time.sleep(0.5)
		print "\n 系统提示：获得新手金币奖励 --- 1000\n"
		GOLD = 1000
		print " 账户余额： %d\n" % GOLD
		raw_input(" 按下回车离开")
		print "\n 前往武备店 ...\n"


def getgundam():
	
	#获取高达

	#global GOLD, NUMBER
	
	print " Zeastion >>> 现在你已了解这些机体数据\n 那么，选择哪一台？\n"
	NUMBER = raw_input(" 请输入选择的机体编号[1-4]：")
	#number = int(NUMBER)

	if int(NUMBER) in range (0, 5): 

		print "\n 高达信息更新\n 绑定驾驶员\n 请稍侯 ...\n\n"
		time.sleep(1.2)
	
		information()
	
		print " |    驾驶员          %s |\n +---------------------------+\n" % NAME
		time.sleep(0.5)
		raw_input(" 绑定完毕，敲击回车确定")

		print " Zeastion >>> 好了 \033[5;31;47m%s\033[0m 接下来需要给你的高达配备各种装备\n 具体事宜武备店老板 Jack 会给你做详细介绍，再会！\n 1- \"多谢老Z！\"\n 2- \"真是受够你了，快走吧！\"" % NAME
		
		say_bye()	

def information():
	
	#global NUMBER, HP, MP, AK, DF	
	
	if NUMBER == "1":
		print "\n +---------------------------+\n | 1- GAT-X105 Strike Gundam |\n -----------------------------\n |    初始HP             550 |\n -----------------------------\n |    初始MP             150 |\n -----------------------------\n |    攻击力              75 |\n -----------------------------\n |    防御力              30 |\n +---------------------------+\n"
		hp = 500
		mp = 150
		ak = 75
		df = 30

	elif NUMBER == "2":
		print "\n +---------------------------+\n | 2- MSZ-008 ZII GUNDAM ZII |\n -----------------------------\n |    初始HP             450 |\n -----------------------------\n |    初始MP             200 |\n -----------------------------\n |    攻>击力              65 |\n -----------------------------\n |    防御力              45 |\n +---------------------------+\n"
               	hp = 450
               	mp = 200
               	ak = 65
               	df = 45

	elif NUMBER == "3":
		print "\n +---------------------------+\n | 3- ZM-S08G ZOLO           |\n -----------------------------\n |    初始HP             500 |\n -----------------------------\n |    初始MP             180 |\n -----------------------------\n |    攻>击力              70 |\n -----------------------------\n |    防御力              35 |\n +---------------------------+\n"
               	hp = 500
               	mp = 180
               	ak = 70
               	df = 35

	elif NUMBER == "4":
		print "\n +---------------------------+\n | 4- GN-001 Gundam Exia     |\n -----------------------------\n |    初始HP             600 |\n -----------------------------\n |    初始MP             200 |\n -----------------------------\n |    攻>击力              80 |\n -----------------------------\n |    防御力              35 |\n +---------------------------+\n"
               	hp = 600
               	mp = 200
               	ak = 80
               	df = 35

	else:
		print "\n 输入出错\n"


def inquire():
	
	#查询高达机体信息
	
	#global NUMBER

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
	#global NAME 
	NAME = raw_input(" Zeastion >>> 姓名？")
	age = raw_input(" Zeastion >>> 年龄？")
	nationality = raw_input(" Zeastion >>> 国籍？")
	print " ----------------------------------------------\n ----------------------------------------------"
	raw_input(" Zeastion >>> 好的，资料记录完毕，请确认后设定GundamOS启动密码。\n")
	
	print """ +---------
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
	raw_input(" 按下回车确认以上信息\n\n ----------------------------------------------\n ----------------------------------------------\n\n")

	print " Zeastion >>> 恭喜你 \033[5;31;47m%s\033[0m ，你获得了Gundam的驾驶权\n" % NAME
	time.sleep(0.5)
	print " 仓库开启中 ...\n\n"
	time.sleep(1)

	inquire()
	

start()

