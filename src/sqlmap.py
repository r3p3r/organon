#!/usr/bin/python
#coding=utf-8

#This script makes the download, compilation and install of 
#sqlmap on systems Debian/like
#This script only automates the things

__AUTHOR__	=	"Fnkoc"
__DATE__	=	"06/02/2015"

import os

comandos = [
   "mv sqlmap /opt/",
   "./generator sqlmap python sqlmap.py"]

for a in comandos:
	os.system(a)

print("\n\n")
print("-"*80)
print("\n All clear\n Enjoy!")
print("""
  write \"sqlmap\" without the quotes on your terminal
  and hit ENTER to run the application
  sqlmap can be found at /opt
""")
print("-"*80)
