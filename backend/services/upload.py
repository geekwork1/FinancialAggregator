import sys

from pydantic.error_wrappers import ValidationError


def get_path_upload_photo(instance, file):
    """Построение пути к файлу
    format:
            (media)/photo/user_id/photo.jpg(png, tiff)
    """
    return f'photo/{instance.owner_id}/{file}'


def get_path_upload_avatar(instance, file):
    """Построение пути к файлу
    format:
            (media)/photo/user_id/photo.jpg(png, tiff)
    """
    return f'avatar/{instance.owner_id}/{file}'


def validate_size_image(file_obj):

    """
    Проверка размер файла
    :param megabyte_limit: maximum limit volume=100 mB file
    :param file_obj: file for checks
    :return: if it exceeds the limit, an exception is error
    """
    megabyte_limit = 100
    if sys.getsizeof(file_obj) > megabyte_limit*1024*1024:
        raise ValidationError(f'Максимальный размер файла {megabyte_limit} МБайт')