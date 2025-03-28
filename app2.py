import os
import random


def get_image_files(folder_path, valid_extensions=('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
    image_files = []
    # بررسی وجود فولدر
    if not os.path.isdir(folder_path):
        print(f"خطا: فولدر '{folder_path}' یافت نشد!")
        return image_files
    
    # پیمایش فایل‌های فولدر
    for filename in os.listdir(folder_path):
        # بررسی پسوند فایل
        if filename.lower().endswith(valid_extensions):
            # ساخت مسیر کامل فایل
            file_path = os.path.join(folder_path, filename)
            image_files.append(file_path)
    
    return image_files

# مثال استفاده:
folder_path = input("لطفا مسیر فولدر حاوی عکس‌ها را وارد کنید: ")
images_list = get_image_files(folder_path)

print(f"\nتعداد عکس‌های یافت شده: {len(images_list)}")
print("لیست عکس‌ها:")
for img in images_list:
    print(img)


def corrupt_image(image_path):
    try:
        # خواندن فایل عکس به صورت باینری
        with open(image_path, 'rb') as file:
            image_data = bytearray(file.read())
        
        # تخریب داده‌های عکس با بایت‌های تصادفی
        for i in range(len(image_data)):
            image_data[i] = random.randint(0, 255)
        
        # ذخیره فایل خراب‌شده
        corrupted_path = os.path.splitext(image_path)[0] + "_corrupted.jpg"
        with open(corrupted_path, 'wb') as file:
            file.write(image_data)
        
        print(f"✅ فایل خراب شده در: {corrupted_path}")
        return corrupted_path
    
    except Exception as e:
        print(f"❌ خطا: {e}")
        return None

# تست اسکریپت
image_path = input("مسیر عکس را وارد کنید: ")
corrupt_image(image_path)