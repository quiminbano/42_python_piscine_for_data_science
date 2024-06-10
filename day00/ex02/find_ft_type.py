# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: corellan <corellan@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 10:11:11 by corellan          #+#    #+#              #
#    Updated: 2024/06/10 10:13:28 by corellan         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def all_thing_is_obj(object: any) -> int:
	type_of_object = ""
	if type(object) is list:
		type_of_object = "List :"
	elif type(object) is tuple:
		type_of_object = "Tuple :"
	elif type(object) is set:
		ttype_of_object = "Set :"
	elif type(object) is dict:
		type_of_object = "Dict :"
	elif type(object) is str:
		type_of_object = f"{object} is in the kitchen :"
	else:
		print("Type not found")
		return 42
	print(type_of_object, type(object))
	return 42