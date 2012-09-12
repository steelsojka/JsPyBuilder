# Build script for minifing javascript and css files
# Author Steven Sojka

import os
import glob
import config

__COMPILERPATH__           = config.settings['COMPILER_PATH']
__COMPILED_MASTER_OUTPUT__ = config.settings['OUTPUT_COMPILED_FILE']
__CONCAT_MASTER_OUTPUT__   = config.settings['OUTPUT_CONCAT_FILE']
__MASTER_COMPILE__         = config.settings['COMPILE_MASTER_OUTPUT']
__FILES__                  = config.entries 

def print_line(insert_text=""):
  str = ""
  for i in range(0, 40):
    if i == 5:
      str += insert_text
    str += "-"
  print '\n' + str + '\n'

def compile(file, output):
  if ".js" in file:
    print "Minifying JS file... " + file
    os.system("java -jar " + __COMPILERPATH__ + " --js " + file + " --js_output_file " + output)
  elif ".css" in file:
    print "Minifying CSS file... " + file
  else:
    print "File can not be compiled!"
  print "Done"

def concat(file_list):
  str = ""
  for file_name in file_list:
    str += "\n" + open(file_name).read()
    print "Adding file " + file_name
  return str

def output_file(name, content):
  new_file = open(name, 'w')
  print "Writing concatenated file... " + name + "\n"
  new_file.write(content)

master_str = ""

print_line("START")

for entry in __FILES__:

  path = entry['PATH']
  files = entry['FILES']
  
  if path == "":
    print_line("root")
  else:
    print_line(path)

  if "*" in files:
    file_list = glob.glob(os.path.join(path, files))
  else:
    file_list = []
    for file in files:
      file_list.append(path + file)

  if entry['ADD_TO_MASTER']:
    master_str += concat(file_list)
    print "Added to " + __CONCAT_MASTER_OUTPUT__
  else:
    output_file(entry["OUTPUT_CONCAT_FILE"], concat(file_list))
    if entry['COMPILE']:
      compile(entry['OUTPUT_CONCAT_FILE'], entry['OUTPUT_COMPILED_FILE'])

# Output the master string 
output_file(__CONCAT_MASTER_OUTPUT__, master_str) 

print "Done"
if __MASTER_COMPILE__:
  compile(__CONCAT_MASTER_OUTPUT__, __COMPILED_MASTER_OUTPUT__)

print_line("END")
