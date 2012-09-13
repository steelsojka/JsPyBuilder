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

def print_line(insert_text="", length=40, symbol="-"):
  str = ""
  for i in range(0, length):
    if i == 5:
      str += insert_text
    str += symbol
  print '\n' + str + '\n'

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

def concat(file_list):
  str = ""
  for file_name in file_list:
    str += "\n" + open(file_name).read()
    print "Adding file " + file_name
  return str

def delete_file(path):
  if os.name == "posix":
    os.system("rm " + path)
  else:
    os.system("del " + path)
  print path + " deleted"

def output_file(name, content):
  new_file = open(name, 'w')
  print "Writing concatenated file... " + name
  new_file.write(content)

print_line("START", 40, "/")

for i, entry in enumerate(__FILES__):
  
  print_line("Entry #" + str(i + 1), 40, "=")

  entry_str = ""

  for path, files in entry['FILES'].iteritems():
    
    print_line(path, 20, "-")

    if "*" in files:
      file_list = glob.glob(os.path.join(path, files))
    else:
      file_list = [path + file for file in files]
    
    entry_str += concat(file_list)
    print "Added to " + entry['OUTPUT_CONCAT_FILE']

  output_file(entry["OUTPUT_CONCAT_FILE"], entry_str)
  
  if entry['COMPILE']:
    compile(entry['OUTPUT_CONCAT_FILE'], entry['OUTPUT_COMPILED_FILE'])
    if entry['REMOVE_CONCAT']:
      delete_file(entry['OUTPUT_CONCAT_FILE'])

print_line("END", 40, "/")
