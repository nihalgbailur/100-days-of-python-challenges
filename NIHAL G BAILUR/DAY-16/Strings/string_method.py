message ="hello world"
# lowercase ,uppercase, titlecase
lower_case = message.lower()
upper_case = message.upper()
title_case = message.title()
# count = message.count()
# TypeError: count expected at least 1 argument, got 0
count = message.count("l")
print(count)