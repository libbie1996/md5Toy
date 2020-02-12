from tkinter import *
from windowCreate import windowCreate
from windowBreak import windowBreak
import random
import hashlib

                                                                                                                          
#	                                    dddddddd                                                                              
#	                                    d::::::d555555555555555555TTTTTTTTTTTTTTTTTTTTTTT                                     
#	                                    d::::::d5::::::::::::::::5T:::::::::::::::::::::T                                     
#	                                    d::::::d5::::::::::::::::5T:::::::::::::::::::::T                                     
#	                                    d:::::d 5:::::555555555555T:::::TT:::::::TT:::::T                                     
#	   mmmmmmm    mmmmmmm       ddddddddd:::::d 5:::::5           TTTTTT  T:::::T  TTTTTTooooooooooo yyyyyyy           yyyyyyy
#	 mm:::::::m  m:::::::mm   dd::::::::::::::d 5:::::5                   T:::::T      oo:::::::::::ooy:::::y         y:::::y 
#	m::::::::::mm::::::::::m d::::::::::::::::d 5:::::5555555555          T:::::T     o:::::::::::::::oy:::::y       y:::::y  
#	m::::::::::::::::::::::md:::::::ddddd:::::d 5:::::::::::::::5         T:::::T     o:::::ooooo:::::o y:::::y     y:::::y   
#	m:::::mmm::::::mmm:::::md::::::d    d:::::d 555555555555:::::5        T:::::T     o::::o     o::::o  y:::::y   y:::::y    
#	m::::m   m::::m   m::::md:::::d     d:::::d             5:::::5       T:::::T     o::::o     o::::o   y:::::y y:::::y     
#	m::::m   m::::m   m::::md:::::d     d:::::d             5:::::5       T:::::T     o::::o     o::::o    y:::::y:::::y      
#	m::::m   m::::m   m::::md:::::d     d:::::d 5555555     5:::::5       T:::::T     o::::o     o::::o     y:::::::::y       
#	m::::m   m::::m   m::::md::::::ddddd::::::dd5::::::55555::::::5     TT:::::::TT   o:::::ooooo:::::o      y:::::::y        
#	m::::m   m::::m   m::::m d:::::::::::::::::d 55:::::::::::::55      T:::::::::T   o:::::::::::::::o       y:::::y         
#	m::::m   m::::m   m::::m  d:::::::::ddd::::d   55:::::::::55        T:::::::::T    oo:::::::::::oo       y:::::y          
#	mmmmmm   mmmmmm   mmmmmm   ddddddddd   ddddd     555555555          TTTTTTTTTTT      ooooooooooo        y:::::y           
#	                                                                                                       y:::::y            
#	                                                                                                      y:::::y             
#	                                                                                                     y:::::y              
#	                                                                                                    y:::::y               
#	                                                                                                   yyyyyyy                


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


# Create Generator Window
def createHashWindow():
	hashMaker = windowCreate()


# Create Hash Breaker Window
def breakHashWindow():
	hashBreaker = windowBreak()
	return

	

# create md5Toy window
md5Toy = Tk()
md5Toy.title("md5 Toy")
#md5Toy.geometry('270x120')
md5Toy.configure(bg="#000000")

# create main menu
btnCreate = Button(text="Create md5 hash", font=("Bold", 20), fg="#00ff00", bg="#000000", command=createHashWindow)
btnBreak = Button(text="Break md5 Hash", font=("Bold", 20), fg="#00ff00", bg="#000000", command=breakHashWindow)

#place main menu on md5Toy window
btnBreak.grid(column=0, row=1, padx=10, pady=10)
btnCreate.grid(column=0, row=0, padx=10, pady=10)

md5Toy.mainloop()