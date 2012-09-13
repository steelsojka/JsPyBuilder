# Versions multiple files using regualr expressions
# Used to update a version in JS or CSS includes 
# Example: 
# <script src="myjsfile.25.js"></script>

import config
import re

__FILES__       = config.version['FILES']
__JS_PATTERN__  = config.version['JS_PATTERN']
__CSS_PATTERN__ = config.version['CSS_PATTERN']
__JS_VERSION__  = config.version['JS_VERSION']
__CSS_VERSION__ = config.version['CSS_VERSION']


def replace_version(pattern, version, text):
  return re.sub(pattern, version, text)

def run():
  print "\nUpdating versions...\n"
  for file in __FILES__:
    opened_file = open(file, "r")
    file_text = opened_file.read()
    opened_file.close()

    file_text = replace_version(__JS_PATTERN__, __JS_VERSION__, file_text)
    file_text = replace_version(__CSS_PATTERN__, __CSS_VERSION__, file_text)

    write_file = open(file, "w")
    print "Writing output file... " + file
    write_file.write(file_text)
  print "Done"
