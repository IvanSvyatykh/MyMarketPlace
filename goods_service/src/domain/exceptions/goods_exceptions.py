class DomainException(Exception):
    """Базовая ошибка для домена"""
    pass


class CategoryNotFound(DomainException):
    """Ошибка если  категория товара не найдена"""


class CategoryAlreadyExists(DomainException):
    """Ошибка если категория товара уже существует"""
