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

# Include all game assets.
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,otf,json,mp3,wav,ogg,mp4

# Keep the asset directory available to the application.
source.exclude_dirs = .git,.github,.buildozer,bin

# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------

# DO NOT pin Python to 3.12 here.
# python-for-android's hostpython3 and python3 must match.
requirements = python3,kivy

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
