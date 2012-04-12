#!/usr/bin/env python
import sys

# Get file from argument
try:
    filename = sys.argv[1]
except IndexError:
    print "Need a target file! Enter the name of the file as a parameter."
    sys.exit(0)

try:
    from_file = open(filename, 'r')
except IOError:
    print "File does not exist!"
    sys.exit(0)

output_filename = filename + ".tumblr"
to_file = open(output_filename, 'w')

def remove_newline(line):
    return line[:-1]

def starts_with_numbered_bullet(line):
    """Returns True if the line begins with a numbered bullet, False
    otherwise."""
    # Strip the start of the line for whitespace in case of bullets like, " - "
    line = line.strip()
    if line[:1].isdigit():
        for char in line[1:]:
            # Keep searching until a non-digit is found. If not a digit, only
            # the '.' character is acceptable. Otherwise, return False.
            # Eg. "34." is okay, but "34b." is not.
            # @TODO Possibly allow single letter after the integer.
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
    # Strip the start of the line for whitespace in case of bullets like, " - "
    line = line.strip()
    for bullet in list_of_bullets:
        if line.startswith(bullet):
            return True
    
    if starts_with_numbered_bullet(line):
        return True
    return False


# Remove the first two lines: these lines are generally titles
lines = from_file.readlines()
try:
    if lines[1] == '\n':
        del lines[:2]
except IndexError:
    # Simply do not delete any lines.
    pass

# Keep track of a list of lines to be concatenated and written to the output
# file.
current_line_list = []
for line in lines:
    # If a newline after we've stored content, print everything so far into one
    # line.
    if line == "\n" and len(current_line_list) > 0:
        text = " ".join(current_line_list) + "\n"
        to_file.write(text)
        del current_line_list[:]
    # If a line starts with a bullet, let it have its own line.
    elif starts_with_bullet(line):
        to_file.write(line)
    # Otherwise, simply gather the current line for later writing.
    else:
        current_line_list.append(remove_newline(line))

# Add any remaining lines
text = " ".join(current_line_list)
to_file.write(text)

# Close files and output a final message.
from_file.close()
to_file.close()
print "Output tumblr-formatted file to {}.".format(output_filename)

