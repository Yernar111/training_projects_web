# Конфигурация подключения к БД
from configparser import ConfigParser

def load_config(filename='database.ini', section='postgres'):
    parser = ConfigParser()
    parser.read(filename)
    if not parser.has_section(section):
        raise Exception(f'Section {section} not found in {filename}')
    return dict(parser.items(section)) # Превращает список кортежей в словарь одной командой



# Способ если использовать .env для подключения к базе данных
# from pydantic_settings import BaseSettings, SettingsConfigDict

# class Settings(BaseSettings):
#     db_name: str = ""
#     db_user: str = ""
#     db_password: str = ""
#     db_host: str = ""
#     db_port: int = 

    
#     model_config = SettingsConfigDict(env_file="database.env") # Указываем, откуда брать данные

# settings = Settings() # Создаем один экземпляр настроек для всего приложения




# Дополнительная проверка
# import configparser
# def load_config(filename='database.ini', section='postgres'):
#     parser = configparser.ConfigParser()
#     try:
#         parser.read(filename)
#     except Exception as e:
#         raise Exception(f'Failed to read {filename}: {e}')

#     if not parser.has_section(section):
#         raise Exception(f'Section {section} not found in {filename}')

#     return parser[section]





# Старый способ
# def load_config(filename='database.ini', section='postgres'):
#     parser = ConfigParser() 
#     parser.read(filename)
#     config = {}
#     if parser.has_section(section):
#         params = parser.items(section)
#         for param in params:
#             config[param[0]] = param[1]
#     else:
#         raise Exception('Section {0} not found in the {1} file'.format(section, filename))
#     return config


# if __name__ == '__main__':
#     config = load_config()
#     print(config)