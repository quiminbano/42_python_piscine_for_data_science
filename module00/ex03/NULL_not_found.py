# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: corellan <corellan@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 10:11:20 by corellan          #+#    #+#              #
#    Updated: 2024/06/10 11:14:56 by corellan         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def NULL_not_found(object: any) -> int:
	type_of_object = ""
	if object is None:
		type_of_object = "Nothing: None"
	elif type(object) is float and object != object:
		type_of_object = "Cheese: nan"
	elif type(object) is int and object == 0:
		type_of_object = "Zero: 0"
	elif type(object) is str and object == "":
		type_of_object = "Empty:"
	elif type(object) is bool and object == False:
		type_of_object = "Fake: False"
	else:
		print("Type not found")
		return 1
	print(type_of_object, type(object))
	return 0