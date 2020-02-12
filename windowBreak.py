from tkinter import *
from hashBreaker import hashBreaker
import hashlib

#	Copyright (C) 2020 Jordon Mitchell
#		This file is part of md5Toy.

#		md5Toy is free software: you can redistribute it and/or modify
#		it under the terms of the GNU General Public License as published by
#		the Free Software Foundation, either version 3 of the License.

#		md5Toy is distributed in the hope that it will be useful,
#		but WITHOUT ANY WARRANTY; without even the implied warranty of
#		MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#		GNU General Public License for more details.

#		You should have received a copy of the GNU General Public License
#		along with md5Toy.  If not, see <https://www.gnu.org/licenses/>.


# Break hash window

class windowBreak:

	# breaker thread done. reset the display
	def breakerDone(self, hashFound, clearText) :
		self.clearText = clearText
		self.hashFound = hashFound
		for self.buttons in self.rbtn:
			self.buttons.configure(state = 'normal')

		self.btnBreakHash.configure(text="Break md5 hash", command=self.startBreaker)
		self.btnCopyClearText.configure(state='normal')
		self.txtHash.configure(state='normal')

		if self.hashFound :
			self.lblClearText.configure(text=self.clearText, fg="#00ff00")
		else :
			self.lblClearText.configure(text="No match found", fg="#ff0000")

		self.lblClearText.grid(column=0, row=5, columnspan=3, padx=10, pady=10)

	# breaker finished charSet and added another char
	def breakerUpdate(self, clearText) :
		self.lblClearText.configure(text="Running: " + str(clearText) + " char", fg="#00ffff")

	# start hash breaker and disable display
	def startBreaker(self, event=None):
		for self.buttons in self.rbtn:
			self.buttons.configure(state='disabled')

		self.btnBreakHash.configure(text="stop running", command=self.stopBreaker)
		self.btnCopyClearText.configure(state='disabled')
		self.txtHash.configure(state='disabled')
		self.targetHash = self.txtHash.get()
		self.lblClearText.configure(text="Running", fg="#0000ff")
		self.lblClearText.grid(column=0, row=5, columnspan=3, padx=10, pady=10)

		# create hashBreaker thread
		self.hashSmash = hashBreaker(self.charSet[self.charSetCurrent.get()], self.targetHash, parent=self)
		self.hashSmash.setDaemon(True)
		# start hashBreaker thread
		self.hashSmash.start()

	# stop hashBreaker thread
	def stopBreaker(self, event=None):
		self.hashSmash.join()


	# copy clear text to clip board
	def copyClearText(self, event=None):
		self.windowBreak.clipboard_clear()
		self.windowBreak.clipboard_append(self.lblClearText.cget("text"))
		self.windowBreak.update()

		print(str(self.charSet[self.charSetCurrent.get()]))

	# constructor
	def __init__ (self):

		# create window
		self.windowBreak = Tk()
		self.windowBreak.title("Break Hash")
		self.windowBreak.configure(bg="#000000")
		self.windowBreak.bind('<Return>', self.startBreaker)
		self.hashFound = False
		self.clearText = ""
		self.charSet = [[" ", "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[", "\\", "]", "^", "_", "`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~"], ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"], ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"], ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"], ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]]
		self.charSetCurrent = IntVar(self.windowBreak, value=0)
		self.charSetOptions = [("Printable", 0,  0, 1), ("Alfa Numeric", 1,  1, 1), ("Alfa Full", 2, 2, 1), ("Alfa Upper", 3, 0, 2), ("Alfa Lower", 4, 1, 2), ("Numeric", 5, 2, 2)]
	
	
		# create menu
		self.txtHash = Entry(self.windowBreak)
		self.rbtn = []

		for text, value, column, row in self.charSetOptions :
			self.rbtn.append(Radiobutton(self.windowBreak, text=text, variable=self.charSetCurrent, value=value, indicatoron=0))
			self.rbtn[len(self.rbtn) - 1].grid(column=column, row=row)

		self.btnBreakHash = Button(self.windowBreak, text="Break md5 hash", font=("Bold", 20), fg="#00ff00", bg="#000000", command=self.startBreaker)
		self.btnCopyClearText = Button(self.windowBreak, text="Copy clear text", font=("Bold", 20), fg="#00ff00", bg="#000000", command=self.copyClearText)
		self.lblClearText = Label(self.windowBreak, text="", fg="#00ff00", bg="#000000")

		# place menu
		self.txtHash.grid(column=0, row=0, columnspan=3, padx=10, pady=10)
		self.btnBreakHash.grid(column=0, row=3, columnspan=3, padx=10, pady=10)
		self.btnCopyClearText.grid(column=0, row=4, columnspan=3, padx=10, pady=10)
	
		self.windowBreak.mainloop()