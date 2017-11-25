#!/usr/bin/python
#-*-coding:utf-8-*-

# 0001: 读一个文件，每次读两行，并打印出来

def readFile(filepath):
	f = open(filepath, 'r')
	lines = ''
	count = 0
	for line in f:
		lines += line
		count += 1
		if count % 2 == 0:
			print('-------------')
			print(lines)
			lines = ''

if __name__ == '__main__':
	filepath = '0001/words.txt'
	readFile(filepath)