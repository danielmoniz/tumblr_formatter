import sys
#import os

# Get file from argument
filename = sys.argv[1]

from_file = open(filename, 'r')
to_file = open(filename + ".tumblr", 'w')

def remove_newline(line):
    return line[:-1]

def starts_with_numbered_bullet(line):
    """Returns True if the line begins with a numbered bullet, False
    otherwise."""
    line = line.strip()
    if len(line) < 2:
        return False
    if line[0].isdigit():
        for char in line[1:]:
            pass
            # Keep searching until a non-digit is found. If not a digit, only
            # the '.' character is acceptable. Otherwise, return False.
            if char.isdigit():
                continue
            else:
                if char == ".":
                    return True
                else:
                    return False

    return False


def starts_with_bullet(line):
    """Return True if a string starts with a bullet, and False otherwise."""
    list_of_bullets = ['*', '-', '+']
    line = line.strip()
    for bullet in list_of_bullets:
        if line.startswith(bullet):
            return True
    
    if starts_with_numbered_bullet(line):
        return True
    return False


# Remove the first two lines: these lines are generally titles
lines = from_file.readlines()
del lines[:2]

current_line = ""
line_num = 2
for line in lines:
    line_num += 1
    # Used for debugging purposes
    #print line_num, line
    # If a newline after we've stored content, print everything so far into one
    # line.
    if line == "\n" and len(current_line) > 0:
        to_file.write(current_line + "\n")
        current_line = ""
    # If a line starts with a bullet, let it have its own line.
    elif starts_with_bullet(line):
        to_file.write(line)
    # Otherwise, simply gather the current line for later writing.
    else:
        current_line += remove_newline(line)

# Add any remaining lines
to_file.write(current_line)

from_file.close()
to_file.close()