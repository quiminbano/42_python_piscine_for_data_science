# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: corellan <corellan@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 10:10:59 by corellan          #+#    #+#              #
#    Updated: 2024/06/10 10:11:01 by corellan         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from time import time
from datetime import datetime

print(f"Seconds since January 1, 1970: {time():,.3f} or {time():,.3} in scientific notation")
today = datetime.today()
print(today.strftime('%B %d %Y'))