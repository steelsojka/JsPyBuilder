JsPyBuilder
===========

JsPyBuilder concatenates and minifies (compiles) files and spits out the output.  This script was originally written for JS and CSS files for web (hence the name) but can be used to concatenate any file type.

Uses
====
JsPyBuilder uses "Entries" for its files intake.  Each entry is equal to one concatenated and compiled file.  Each entry can have any number of files and directories added to it.  Only JS files and CSS files can be compiled.  JS files are compiled using Google Closure and CSS files use YUI Compressor.

Example
=======

Entries
-------

Entries look like the following.  The "FILES" dictionary has the file directory as the keys and a list of files as the data.

```python
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
```
 A directory can take a string ONLY if a wild card is used

 ```python
entries = [
  {
    "COMPILE": True,
    "OUTPUT_COMPILED_FILE": "Classes.min.js",
    "OUTPUT_CONCAT_FILE": "Classes.concat.js",
    "REMOVE_CONCAT": True,
    "FILES": {
      "../js/Classes/": "*.js"  # Grab all js files in the directory 
    }
  }
]
```

Versioning
----------

Versioning is just a simple regular expression replace of strings where static files with version numbers are located in the code

```python
version = {
  "FILES": ["../html_top.cfm"],  # List of files to look in
  "JS_PATTERN": "main.[0-9]+.js",  # Pattern to replace for JS
  "CSS_PATTERN": "main.[0-9]+.css", # Pattern to replace for CSS
  "JS_VERSION": "main.74.js", # What to replace JS with
  "CSS_VERSION": "main.72.css"  # What to replace CSS with
}
```

How to
======

Run script from the command line by running build.py

```
>> python build.py
```

License
=======
MIT Licensed