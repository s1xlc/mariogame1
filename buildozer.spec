[app]

# (str) Title of your application
title = Mario Game

# (str) Package name
package.name = mariogame1

# (str) Package domain (needed for android packaging)
package.domain = org.s1xlc

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) List of permissions
#android.permissions = INTERNET

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning instead of aborting when buildozer is run as root (0 = False, 1 = to be equivariant|2 = ignore)
warn_on_root = 1
