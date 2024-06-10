# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: corellan <corellan@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 10:39:28 by corellan          #+#    #+#              #
#    Updated: 2024/06/10 10:57:23 by corellan         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

sys.argv
number = 0
if len(sys.argv) == 1:
	sys.exit(0)
try:
	if len(sys.argv) != 2:
		raise AssertionError("AssertionError: more than one argument is provided")
	try:
		number = int(sys.argv[1])
	except ValueError:
		raise AssertionError("AssertionError: argument is not an integer")
except AssertionError as e:
	print(e)
	sys.exit(1)
if number % 2 == 0:
	print("I'm Even.")
else:
	print("I'm Odd.")
sys.exit(0)