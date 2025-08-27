import cv2
import os

# مجلد لحفظ الصور
output_folder = "output_images"
os.makedirs(output_folder, exist_ok=True)

# مثال: قراءة صورة وتحويلها إلى رمادية وحفظها
input_image_path = "input.jpg"  # ضع صورة داخل المشروع أو عدل المسار
output_image_path = os.path.join(output_folder, "output.jpg")

# قراءة الصورة
img = cv2.imread(input_image_path)

if img is None:
    print("لم يتم العثور على الصورة:", input_image_path)
else:
    # تحويل الصورة إلى رمادية
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # حفظ الصورة
    cv2.imwrite(output_image_path, gray)
    print("تم حفظ الصورة المعالجة في:", output_image_path)
