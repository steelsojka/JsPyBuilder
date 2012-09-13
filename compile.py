# Build script for minifing javascript and css files
# Author Steven Sojka

import os
import glob
import config

__JS_COMPILER_PATH__     = config.settings['JS_COMPILER_PATH']
__JS_COMPILER_OPTIONS__  = config.settings['JS_COMPILER_OPTIONS']
__CSS_COMPILER_PATH__    = config.settings['CSS_COMPILER_PATH']
__CSS_COMPILER_OPTIONS__ = config.settings['CSS_COMPILER_OPTIONS']
__FILES__                = config.entries

# Print line to terminal
def print_line(insert_text="", length=40, symbol="-"):
  str = ""
  for i in range(0, length):
    if i == 5:
      str += insert_text
    str += symbol
  print '\n' + str + '\n'

# Compile the selected file
def compile(file, output):
  if ".js" in file:
    print "Minifying JS file... " + file
    os.system("java -jar " + __JS_COMPILER_PATH__ + " --js " + file + " --js_output_file " + output)
  elif ".css" in file:
    print "Minifying CSS file... " + file
    os.system("java -jar " + __CSS_COMPILER_PATH__ + " -o " + output + " " + file)
  else:
    print "File can not be compiled!"
  print "Done"

# Concatenate the list of files
def concat(file_list):
  str = ""
  for file_name in file_list:
    str += "\n" + open(file_name).read()
    print "Adding file " + file_name
  return str

# Delete a file
def delete_file(path):
  os.remove(path)
  print path + " deleted"

# Output content to new file
def output_file(name, content):
  new_file = open(name, 'w')
  print "Writing concatenated file... " + name
  new_file.write(content)

# Run function
def run():
  print_line("START COMPILE", 40, "/")

  # Loop through each entry
  for i, entry in enumerate(__FILES__):
    
    print_line("Entry #" + str(i + 1), 40, "=")

    entry_str = ""

    # Loop through each directory and file list
    for path, files in entry['FILES'].iteritems():
      
      print_line(path, 20, "-")

      # If wildcard grab all files that match in the directory
      if "*" in files:
        file_list = glob.glob(os.path.join(path, files))
      else:
        file_list = [path + file for file in files]
      
      entry_str += concat(file_list)
      print "Added to " + entry['OUTPUT_CONCAT_FILE']

    # Output concatenated file for entry
    output_file(entry["OUTPUT_CONCAT_FILE"], entry_str)
    
    # If true minify concatenated file
    if entry['COMPILE']:
      compile(entry['OUTPUT_CONCAT_FILE'], entry['OUTPUT_COMPILED_FILE'])

      # If true remove concatenated file after compile
      if entry['REMOVE_CONCAT']:
        delete_file(entry['OUTPUT_CONCAT_FILE'])

  print_line("END", 40, "/")
