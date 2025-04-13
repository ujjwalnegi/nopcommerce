import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")


class Read_Config:
    @staticmethod
    def get_admin_page_url():
        url = config.get('admin login info', 'admin_page_url')
        return url

    @staticmethod
    def get_valid_username():
        valid_username = config.get('admin login info', 'valid_username')
        return valid_username

    @staticmethod
    def get_password():
        password = config.get('admin login info', 'valid_password')
        return password

    @staticmethod
    def get_invalid_username():
        invalid_username = config.get('admin login info', 'invalid_username')
        return invalid_username
