[app]
# Anaran'ny App
title = Coupe du Monde 2026
# Anarana ampiasain'ny Android (tsy mahazo misy habaka)
package.name = coupe2026
# Domain (ho an'ny Play Store)
package.domain = org.franco.coupe
# Ity no tena ilaina mba tsy hisy error (source.dir = .)
source.dir = .
# Inona avy ny file ho tafiditra
source.include_exts = py,png,jpg,kv,atlas
# Version
version = 0.1
# Inona no ilaina (python3 sy kivy)
requirements = python3,kivy
# Orientation
orientation = portrait
# Fullscreen (0 = tsia, 1 = eny)
fullscreen = 0
# Android settings
android.api = 33
android.minapi = 21
android.sdk = 23
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.presplash_color = #FFFFFF

[buildozer]
log_level = 2
warn_on_root = 1
