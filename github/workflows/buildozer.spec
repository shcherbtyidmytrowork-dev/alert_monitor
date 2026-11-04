[app]
title = Alert Monitor
package.name = alertmonitor
package.domain = ua.dnistrovskyi
source.dir = .
source.include_exts = py,png,jpg,kv,json
version = 1.0
requirements = python3,kivy==2.3.0,sqlite3,telethon,pyaes,rsa,pyasn1
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,WAKE_LOCK,POST_NOTIFICATIONS,REQUEST_IGNORE_BATTERY_OPTIMIZATIONS
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
