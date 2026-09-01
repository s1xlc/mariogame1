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

source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,otf,json,mp3,wav,ogg,mp4

source.exclude_dirs = .git,.github,.buildozer,bin,.assets,android_assets

# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------

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
# PYTHON-FOR-ANDROID
# -----------------------------------------------------------------------------

# Pin to the verified pre-Python-3.14 p4a release.
p4a.branch = v2024.01.21
p4a.commit = 957a3e5

# Use the SDL2 bootstrap required by Kivy.
p4a.bootstrap = sdl2

# -----------------------------------------------------------------------------
# BUILD
# -----------------------------------------------------------------------------

[buildozer]

log_level = 2

bin_dir = bin

android.accept_sdk_license = True

android.skip_update = False
