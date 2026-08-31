[app]

# Application name
title = Mario Game NPC

# Package name
package.name = mariogame

# Package domain
package.domain = org.mariogame

# Version
version = 0.1

# Source directory
source.dir = .

# Files included in the APK
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,otf,json,mp3,wav,ogg,mp4

# Python requirements
requirements = python3,kivy,pyjnius

# Screen orientation
orientation = portrait

# Internet permission
android.permissions = INTERNET

# Android API
android.api = 33

# Minimum Android API
android.minapi = 21

# Android NDK
android.ndk = 25b

# AndroidX
android.androidx = True

# CPU architectures
android.archs = arm64-v8a,armeabi-v7a


[buildozer]

# Logging
log_level = 2

# APK output directory
bin_dir = bin

# Accept Android SDK licenses
android.accept_sdk_license = True

# Allow dependency updates
android.skip_update = False
