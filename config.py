# These settings are required to run

settings = {
  # Path to the Google Closure coompiler
  "JS_COMPILER_PATH": "compiler.jar",
  "JS_COMPILER_OPTIONS": "",
  "CSS_COMPILER_PATH": "yuicompressor-2.4.7.jar",
  "CSS_COMPILER_OPTIONS": "",
  "RUN_COMPILER": True,
  "RUN_VERSIONING": True
}

version = {
  "FILES": ["../index.html"],
  "JS_PATTERN": "main.[0-9]+.js",
  "CSS_PATTERN": "main.[0-9]+.css",
  "JS_VERSION": "main.74.js",
  "CSS_VERSION": "main.72.css"

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
  {
    "COMPILE": True,
    "OUTPUT_COMPILED_FILE": "Classes.min.js",
    "OUTPUT_CONCAT_FILE": "Classes.concat.js",
    "REMOVE_CONCAT": True,
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
    "REMOVE_CONCAT": True,
    "FILES": {
      "../stylesheets/": ["bootstrap.css", "style.css"]
    }
  }
]