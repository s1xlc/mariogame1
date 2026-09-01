[app]

title = Mario Game

package.name = mariogame
package.domain = org.mariogame

version = 0.1

source.dir = .

source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,otf,json,mp3,wav,ogg,mp4

source.exclude_dirs = .git,.github,.buildozer,bin,.assets,android_assets

requirements = python3,kivy

orientation = landscape
fullscreen = 1

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk = 25b

android.archs = arm64-v8a,armeabi-v7a

android.androidx = True

p4a.branch = v2024.01.21
p4a.commit = 957a3e5

p4a.bootstrap = sdl2


[buildozer]

log_level = 2

bin_dir = bin

android.accept_sdk_license = True

android.skip_update = False
