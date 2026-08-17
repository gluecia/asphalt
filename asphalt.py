#!/usr/bin/env python3

import os
import sys

tarmak_one = """
[ids]

*

[main]
e = j
j = n
k = e
n = k
"""

tarmak_two = """
[ids]

*

[main]
e = f
t = g
f = t
g = j
j = n
k = e
n = k
"""

tarmak_three = """
[ids]

*

[main]
e = f
r = j
t = g
s = r
d = s
f = t
g = d
j = n
k = e
n = k
"""

tarmak_four = """
[id]

*

[main]
e = f
r = p
t = g
y = j
o = y
p = ;
s = r
d = s
f = t
g = d
j = n
k = e
; = o
n = k
"""

def main():
  if os.getuid() != 0:
    print("asphalt must be run as a super user!")
    sys.exit(-1)

  print("!! asphalt will override your /etc/keyd/default.conf !!")
  selection = input("Select Tarmak variant (1-4): ")

  write_contents = ""
  if selection == "1":
    write_contents = tarmak_one
  elif selection == "2":
    write_contents = tarmak_two
  elif selection == "3":
    write_contents = tarmak_three
  elif selection == "4":
    write_contents = tarmak_four
  else:
    print("Invalid input.")
    sys.exit(-1)

  with open("/etc/keyd/default.conf", "w") as file:
    file.write(write_contents)

  print("[+] Successfully wrote file! Restart the keyd daemon to apply effects.");


if __name__ == "__main__":
  main()
