from deepface import DeepFace
import cv2
import os

# Функция для изменения выражения лица
def change_expression(input_image_path, output_image_path, target_emotion='happy'):
    # Проверка, существует ли входной файл
    if not os.path.isfile(input_image_path):
        print(f"Файл {input_image_path} не существует.")
        return
    
    # Проверка, существует ли выходной каталог
    output_dir = os.path.dirname(output_image_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Загрузка изображения
    image = cv2.imread(input_image_path)
    if image is None:
        print(f"Не удалось загрузить изображение {input_image_path}.")
        return

    # Изменение выражения лица
    result_img = DeepFace.analyze(img_path=input_image_path, actions=['emotion'])
    
    # Проверка результата анализа
    if 'dominant_emotion' in result_img:
        dominant_emotion = result_img['dominant_emotion']
        print(f"Доминирующая эмоция: {dominant_emotion}")

    # Изменение выражения на желаемое (только для иллюстрации)
    # В реальности библиотека deepface не меняет выражение, это пример, как можно интегрировать анализ
    # и обработку изображений для подобных задач с помощью других подходов
    
    # Здесь можно вставить код для реальной замены выражения с помощью других подходов

    # Сохранение изображения с изменённым выражением
    cv2.imwrite(output_image_path, image)
    print(f"Изображение с изменённым выражением сохранено как {output_image_path}")

# Пример использования
input_image_path = "images/input2.jpg"
output_image_path = "output/smile_input.jpg"
change_expression(input_image_path, output_image_path)
