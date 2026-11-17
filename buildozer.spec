
[app]

title = FF AI PLAYER
package.name = ffplayer
package.domain = org.nimsara

source.dir = .
source.include_exts = py,kv,png,jpg

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.archs = arm64-v8a, armeabi-v7a
android.api = 35
android.minapi = 23

[buildozer]

log_level = 2
warn_on_root = 1
