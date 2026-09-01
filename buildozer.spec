[app]

# -----------------------------------------------------------------------------
# APPLICATION
# -----------------------------------------------------------------------------

title = Mario Game

package.name = mariogame
package.domain = org.mariogame

version = 0.1

# -----------------------------------------------------------------------------
# SOURCE
# -----------------------------------------------------------------------------

source.dir = .

# Include all game asset types.
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,otf,json,mp3,wav,ogg,mp4

# IMPORTANT:
# Keep the .assets directory in the source tree.
# main.py already resolves assets through .assets.
source.exclude_dirs = .git,.github,.buildozer,bin

# -----------------------------------------------------------------------------
# PYTHON REQUIREMENTS
# -----------------------------------------------------------------------------

# pyjnius is NOT required by main.py.
#
# Explicitly pin Python so python-for-android does not select its newer
# Python 3.14 toolchain.
requirements = python3==3.12.10,kivy

# -----------------------------------------------------------------------------
# SCREEN
# -----------------------------------------------------------------------------

orientation = landscape
fullscreen = 1

# -----------------------------------------------------------------------------
# ANDROID
# -----------------------------------------------------------------------------

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk = 25b

android.archs = arm64-v8a,armeabi-v7a

android.androidx = True

# -----------------------------------------------------------------------------
# BUILD
# -----------------------------------------------------------------------------

[buildozer]

log_level = 2

bin_dir = bin

android.accept_sdk_license = True

android.skip_update = False
