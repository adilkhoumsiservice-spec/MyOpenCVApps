[app]

# اسم التطبيق
title = MyOpenCVApp
# اسم الحزمة
package.name = myopencvapp
# نطاق الحزمة
package.domain = org.example
# نسخة التطبيق
version = 0.1
# المصدر الرئيسي
source.include_exts = py,txt

# المتطلبات الأساسية
requirements = python3,opencv-python-headless

# أي ملفات إضافية تريد تضمينها
source.include_patterns = input.jpg

# وضع التطبيق (لاستخدام الهاتف بوضع portrait)
orientation = portrait

# أيقونة التطبيق (اختياري)
icon.filename = %(source.dir)s/icon.png

# لاستخدام الشاشة الكاملة (اختياري)
fullscreen = 0

# لاستخدام رسائل تحذير Buildozer
log_level = 2

# إعدادات Android
[buildozer]

# نوع البناء
target = android
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.arch = armeabi-v7a
