class DomainException(Exception):
    """Базовая ошибка для домена"""
    pass


class EmailAlreadyExistsException(DomainException):
    pass
