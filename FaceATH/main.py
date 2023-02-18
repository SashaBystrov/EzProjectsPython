# импорт библиотек
import os
import face_recognition

# составляем список всех доступных изображений
images = os.listdir('images')

# загружаем ваше изображение
image_to_be_matched = face_recognition.load_image_file('my_image.jpg')

# преобразуем загруженное изображение в вектор признаков
image_to_be_matched_encoded = face_recognition.face_encodings(
    image_to_be_matched)[0]

# итерация для каждого изображения
for image in images:
    # загружаем изображение
    current_image = face_recognition.load_image_file("images/" + image)
    # преобразуем загруженное изображение в вектор признаков
    current_image_encoded = face_recognition.face_encodings(current_image)[0]
    # проверяем соответствие изображений
    result = face_recognition.compare_faces(
        [image_to_be_matched_encoded], current_image_encoded)
    # проверка совпадения
    if result[0] == True:
        print("Matched: " + image)
    else:
        print("Not matched: " + image)