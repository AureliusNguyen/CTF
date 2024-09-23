from PIL import Image 
import cv2
import  numpy as np


class Interpreter:

    def __init__(self, rom):
        self.stack = cv2.imread("initial_state.png", 0)
        self.sp_x = 0 
        self.sp_y = 0
        self.last_jz = 0
        self.ip = 0
        self.prec = ""
        self.rom = rom

    def exec(self,a):
        if a == "👆":
            self.sp_y = (self.sp_y + 1) % 255
        elif a == "👇":
            self.sp_y = (self.sp_y - 1) % 255
        elif a == "👉":
            self.sp_x = (self.sp_x + 1) % 255
        elif a == "👈":
            self.sp_x = (self.sp_x - 1) % 255
        elif a == "👍":
            if self.stack[self.sp_y][self.sp_x] < 255:
                self.stack[self.sp_y, self.sp_x] =  self.stack[self.sp_y, self.sp_x] + 1
        elif a == "👎": 
            if self.stack[self.sp_y][self.sp_x] > 0:
                self.stack[self.sp_y, self.sp_x] =  self.stack[self.sp_y, self.sp_x] - 1
        elif a == '🫸':
            if self.stack[self.sp_y, self.sp_x] == 0:
                depth = 1
                while depth != 0:
                    self.ip += 1
                    if self.rom[self.ip] == '🫸':
                        depth += 1
                    elif self.rom[self.ip] == '🫷':
                        depth -= 1
        elif a == '🫷':
            if self.stack[self.sp_y, self.sp_x] != 0:
                depth = 1
                while depth != 0:
                    self.ip -= 1
                    if self.rom[self.ip] == '🫷':
                        depth += 1
                    elif self.rom[self.ip] == '🫸':
                        depth -= 1
        elif a == "💬":
            print(chr(self.stack[self.sp_y, self.sp_x]),end="")
        elif a == "🔁":
        	base12_mapping = {'🕛': 0, '🕐': 1, '🕑': 2, '🕒': 3, '🕓': 4, '🕔': 5, '🕕': 6, '🕖': 7, '🕗': 8, '🕘': 9, '🕙': 'a', '🕚': 'b'}
        	a = base12_mapping[self.rom[self.ip + 1]]
        	b = base12_mapping[self.rom[self.ip + 2]]
        	c = base12_mapping[self.rom[self.ip + 3]]
        	times = int(str(a) + str(b) + str(c), 12)
        	for _ in range(times):
        		self.exec(self.prec)
        	self.ip += 3
        else:
            print(">>>", ord(a), "<<<")

    def run(self):
        while self.ip < len(self.rom):
            self.exec(self.rom[self.ip])
            self.prec = self.rom[self.ip]
            self.ip += 1
        return -1
    

file = open("program.txt","r")
rom = file.read()
file.close()
interpreter = Interpreter(rom)

interpreter.run()

'''
for i in range(255):
	for j in range(255):
		if interpreter.stack[i][j] != 0:
			interpreter.stack[i][j] = 255
'''
cv2.imwrite("flag.png",interpreter.stack)