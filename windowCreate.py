from tkinter import *
import hashlib

#	Copyright (C) 2020 Jordon Mitchell
#		This file is part of md5Toy.
#
#		md5Toy is free software: you can redistribute it and/or modify
#		it under the terms of the GNU General Public License as published by
#		the Free Software Foundation, either version 3 of the License.
#
#		md5Toy is distributed in the hope that it will be useful,
#		but WITHOUT ANY WARRANTY; without even the implied warranty of
#		MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#		GNU General Public License for more details.
#
#		You should have received a copy of the GNU General Public License
#		along with md5Toy.  If not, see <https://www.gnu.org/licenses/>.


# Create hash window

class windowCreate:
	
	# generate the hash
	def runHash(self, event=None):
		self.m = hashlib.md5()
		self.m.update(self.txtClear.get().encode('utf-8'))
		self.lblHash.configure(text=self.m.hexdigest())
		self.lblHash.grid(column=0, row=3, columnspan=3, padx=10, pady=10)

	# copy the hash to clip board
	def copyHash(self, event=None):
		self.windowCreate.clipboard_clear()
		self.windowCreate.clipboard_append(self.lblHash.cget("text"))
		self.windowCreate.update()

	# constructer
	def __init__ (self):
		# create window
		self.windowCreate = Tk()
		self.windowCreate.title("Create Hash")
		self.windowCreate.configure(bg="#000000")
		self.windowCreate.bind('<Return>', self.runHash)
	
	
		# create menu
		self.txtClear = Entry(self.windowCreate)
		self.btnGenHash = Button(self.windowCreate, text="Create md5 hash", font=("Bold", 20), fg="#00ff00", bg="#000000", command=self.runHash)
		self.btnCopyHash = Button(self.windowCreate, text="Copy md5 hash", font=("Bold", 20), fg="#00ff00", bg="#000000", command=self.copyHash)
		self.lblHash = Label(self.windowCreate, text="", fg="#00ff00", bg="#000000")

		# place menu
		self.txtClear.grid(column=0, row=0, columnspan=3, padx=10, pady=10)
		self.btnGenHash.grid(column=0, row=1, columnspan=3, padx=10, pady=10)
		self.btnCopyHash.grid(column=0, row=2, columnspan=3, padx=10, pady=10)
	
		self.windowCreate.mainloop()