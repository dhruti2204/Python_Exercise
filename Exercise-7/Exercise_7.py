"""You are given a list of email addresses. Filter out the validate emails."""
import re
emails = [ "abc@gmail.com", "123$tt*@xyz.com", "good@bad@uk.in", "nasa@usa12.space", "no-reply@domain.in", "ramhanuman@saketa.lok", "ruhi.mohan@exter123.123", "fake@fake123.fakercom"]
Valid = []
for i in emails:
    valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,7}$', i)
    if(valid):
        Valid.append(i)

print(Valid)

