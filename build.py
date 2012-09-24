#!/usr/bin/env python
# Make executable with
# >> chmod +x build.py

# Main run file

import config
import compile
import version

if config.settings['RUN_COMPILER']:
  compile.run()

if config.settings['RUN_VERSIONING']:
  version.run()
