# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: corellan <corellan@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 10:10:45 by corellan          #+#    #+#              #
#    Updated: 2024/06/10 14:52:15 by corellan         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"
ft_tuple = ("Hello", "Finland!")
ft_set.remove("tutu!")
ft_set.add("Helsinki!")
ft_dict["Hello"] = "HIVE Helsinki!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)