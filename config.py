# These settings are required to run

settings = {
  # Path to the Google Closure coompiler
  "JS_COMPILER_PATH": "compiler.jar",
  "JS_COMPILER_OPTIONS": "",
  "CSS_COMPILER_PATH": "yuicompressor-2.4.7.jar",
  "CSS_COMPILER_OPTIONS": ""
}

# Each entry outputs a concat and/or compiled file
# Files are dictionary entry with the key being the directory and the files
# being a list or a string with a wildcard in it
# Example: "FILES:" {
#   "directory1": [
#     "file1.js",
#     "file2.js"
#   ],
#   "directory2": "*.js"  # All .js files in directory 2
# }
# 
# COMPILE: Whether to run the output concat file through the compiler
# OUTPUT_COMPILED_FILE: Compiled file output name
# OUTPUT_CONCAT_FILE: Concatenated file output name
# REMOVE_CONCAT: Remove concatenated file after compile only if file is compiled
# FILES: Dictionary of file paths as keys and a list of files

entries = [
<<<<<<< HEAD
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
=======
  {
    "COMPILE": True,
    "OUTPUT_COMPILED_FILE": "Classes.min.js",
    "OUTPUT_CONCAT_FILE": "Classes.concat.js",
    "REMOVE_CONCAT": False,
    "FILES": {
      "../js/Classes/": [
        "Base.js",
        "Alert.js"
      ]
    }
  },
  {
    "COMPILE": True,
    "OUTPUT_CONCAT_FILE": "stylesheets.concat.css",
    "OUTPUT_COMPILED_FILE": "stylesheets.min.css",
    "REMOVE_CONCAT": False,
    "FILES": {
      "../stylesheets/": ["bootstrap.css", "style.css"]
    }
  }
>>>>>>> Update functionality
]