import hashlib
import threading

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


# Hash Breaking Thread

class hashBreaker(threading.Thread):
	
	# thread main function.
	# starts when thread.start() is ran
	def run(self) :

		# check empty string
		self.m = hashlib.md5()
		self.m.update(("").encode('utf-8'))
		if self.targetHash == self.m.hexdigest() :
			# end loop
			self.notDone = False
			self.notNextLetter = False
			self.foundHash = True
			# save clear text
			self.clearText = ""
			# print to terminal
			print(self.clearText + " : " + str(self.m.hexdigest()) )

		# main loop : ends when thread is done
		while self.notDone :
			self.notNextLetter = True
			# next letter loop : ends when string needs another char
			while self.notNextLetter :
				# reset currentString
				self.currentString = ""
				self.countLetter = len(self.currentIndex) - 1
				# currentString loop : rebuild currentString
				for x, currentChar in enumerate(self.currentIndex) :
					self.currentString = self.currentString + self.charSetCurrent[self.currentIndex[x]]
				
				# lastChar loop : build and check hash foreach last char
				for lastChar in self.charSetCurrent :
					# reset hashlib
					self.m = hashlib.md5()
					# build and encode string in hashlib
					self.m.update((self.currentString + lastChar).encode('utf-8'))
					# run hash and check against target
					if self.targetHash == self.m.hexdigest() :
						# end loop
						self.notDone = False
						self.notNextLetter = False
						self.foundHash = True
						# save clear text
						self.clearText = self.currentString + lastChar
						# print to terminal
						print(self.clearText + " : " + str(self.m.hexdigest()) )
						break

				self.resettingString = True
				# currentIndex loop : used to increment currentIndex to build currentString for next itteration
				while self.resettingString :
					# if more letters :
					if self.countLetter >= 0 :
						# if letter does not carry over
						if self.currentIndex[self.countLetter] < len(self.charSetCurrent) - 1 :
							# increment letter and end currentIndex loop
							self.currentIndex[self.countLetter] = self.currentIndex[self.countLetter] + 1
							self.countLetter = len(self.currentIndex) - 1
							self.resettingString = False
							
						# if letter does carry over
						else :
							# reset letter to 0 and move to next letter in currentIndex
							self.currentIndex[self.countLetter] = 0
							self.countLetter = self.countLetter - 1

					# if no more letters
					else :
						# end current index loop and next letter loop
						self.notNextLetter = False
						self.resettingString = False


			# add another char for next itteration
			self.currentIndex.insert(0, 0)
			# update display
			self.parent.breakerUpdate(len(self.currentIndex) + 1)

		self.threadDone()


	# thread finished reset display
	def threadDone(self) :
		if not self.foundHash :
			self.clearText = "no match found"
		self.parent.breakerDone(self.foundHash, self.clearText)

	# thread stop
	def join(self) :
		self.notDone = False
		self.notNextLetter = False



	# constructor
	def __init__ (self, charSet, targetHash, parent=None, group=None, target=None, name=None, args=(), kwargs=None) : 
		super().__init__()		
		self.parent = parent
		self.charSetCurrent = charSet
		self.targetHash = targetHash
		self.currentIndex =[]
		self.clearText = ""
		self.foundHash = False
		self.notDone = True
		self.notNextLetter = True
		self.resettingString = True
		self.currentString = ""
		self.countLetter = len(self.currentIndex) - 1