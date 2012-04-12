from tumblr_format import *

lines = []
lines.append("Non-bullet line.")
lines.append("- This is a bullet")
lines.append(" * bullet here")
lines.append("  + bullet here")
lines.append("1. Here is a numbered bullet. asdf")
lines.append("1234# Here is a fake numbered bullet.")
lines.append("873382568235. Here is an epic numbered bullet.")

for line in lines:
    print '-'*10
    print line
    print "Is bullet:", starts_with_bullet(line)
    print "Is numbered bullet:", starts_with_numbered_bullet(line)

print "----END----"
