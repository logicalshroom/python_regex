# Task 1: Fix the regex pattern to explide emails addresses from "[exclude.com](http://exclude.com/"

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@(?!exclude)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text) #reverse negative lookup, (make sure to put it AFTER the @ sign)
print(emails)
