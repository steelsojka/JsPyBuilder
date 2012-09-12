# These settings are required to run

settings = {
  # Path to the Google Closure coompiler
  "COMPILER_PATH": "compiler.jar",

  # Google closure master output file name
  "OUTPUT_COMPILED_FILE": "output.min.js",
  
  # Master output for concatenated files
  "OUTPUT_CONCAT_FILE": "output.concat.js",
  
  # Compile the master output
  "COMPILE_MASTER_OUTPUT": True
}

# These are file entries that will be used to concatenate and compile files
# Each "entry" is a single directory
# 
# (R) = ## REQUIRED ##
# 
# PATH (R): The directory in which the files are located 
# ADD_TO_MASTER (R): Determines if these files should be added to the master feed 
#   or compiled seperately
# COMPILE: Only required if entry is NOT added to the master and compiled seperatly.
#   Determines whether the files get compiled
# OUTPUT_COMPILED_FILE: Only required if entry is NOT added to the master and compiled seperatly.
#   Output file for compiled code
# OUTPUT_CONCAT_FILE: Only required if entry is NOT added to the master and compiled seperatly.
#   Output file for concatenated files
# FILES (R): A list a files to be compiled. Can accept a string only if a wildcard is used.
#   Example 1: "FILES": "*.js" # All .js files in a directory
#   Example 2: [
#     "Base.js",  # These will compile in this order
#     "Alert.js",
#     "Class.js"
#   ]

entries = [
#  {
#    "PATH": "../js/Classes/",
#    "ADD_TO_MASTER": True,
#    "COMPILE": True,
#    "OUTPUT_COMPILED_FILE": "Classes.min.js",
#    "OUTPUT_CONCAT_FILE": "Classes.concat.js",
#    "FILES": "*.js"
#  },
#  {
#    "PATH": "../js/Modules/",
#    "ADD_TO_MASTER": True,
#    "COMPILE": False,
#    "OUTPUT_COMPILED_FILE": "Modules.min.js",
#    "OUTPUT_CONCAT_FILE": "Modules.concat.js",
#    "FILES": "*.js"
#  }
]