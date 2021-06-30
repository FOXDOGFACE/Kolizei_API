import requests
from json import loads
import re
import logging

logging.basicConfig(format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt="%d-%b-%y %H:%M:%S")


class KolizeiSecretKeyException(Exception):
    """Kolizei secret key is missing or incorrect."""

    def __init__(self, case=None):
        self.case = case
        if self.case == "missing":
            self.message = "Kolizei secret key is missing."
            logging.error("Kolizei secret key is missing.")
        elif self.case == "incorrect":
            self.message = "Kolizei secret key is incorrect."
            logging.error("Kolizei secret key is incorrect.")
        elif case == 2:
            self.message = "Kolizei secret key not found."
            logging.error("Kolizei secret key not found.")
        elif case == 3:
            self.message = "Kolizei secret key is not valid."
            logging.error("Kolizei secret key is not valid.")
        elif case is None:
            self.message = "Unknown problem with kolizei secret key."
            logging.error("Unknown problem with kolizei secret key.")
        super(Exception, self).__init__(self.message)


class GroupIDException(Exception):
    """Group id is missing."""

    def __init__(self):
        logging.error("Group id is missing.")
        super(Exception, self).__init__("Group id is missing.")


class NumberRequestsError(Exception):
    """To much requests in one time."""

    def __init__(self):
        logging.error("To much requests in one time.")
        super(Exception, self).__init__("To much requests in one time.")


class Kolizei_api(object):
    secret_key = None
    group_id = None

    def __init__(self, secret_token=None, group_id=None):
        if secret_token is not None and group_id is not None:
            self.secret_key = secret_token
            self.group_id = group_id
        elif secret_token is None:
            raise KolizeiSecretKeyException("missing")
        else:
            raise GroupIDException

    def get_rating(self, count=1000, offset=0):
        data = {
            "count": count,
            "offset": offset,
            "group_id": self.group_id,
            "secret_key": self.secret_key
        }
        with requests.post(f"https://appcm.ru/api/rating.get", data=data) as r:
            content = r.content.decode("utf-8")
            json = loads(re.sub("(\w+):", r'"\1":', content))
            if 'error' not in json:
                logging.info('Get_rating method was successfully completed.')
                return json
            else:
                self.raise_exeption(json['error']['error_code'], "get_rating")

    def get_by_id(self, user_id:int):
        data = {
            "user_id": user_id,
            "group_id": self.group_id,
            "secret_key": self.secret_key
        }
        with requests.post(f"https://appcm.ru/api/rating.getById?", data=data) as r:
            content = r.content.decode("utf-8")
            json = loads(re.sub("(\w+):", r'"\1":', content))
        if json['response'] == 1:
            logging.info('get_by_id method was successfully completed.')
            return 1
        else:
            self.raise_exeption(json['error']['error_code'], "get_by_id")

    def users_changePoints(self, points: list, user_ids: list):
        data = {
            "points": ",".join(map(str, points)),
            "user_ids": ",".join(map(str, user_ids)),
            "group_id": self.group_id,
            "secret_key": self.secret_key
        }
        with requests.post(f"https://appcm.ru/api/users.changePoints", data=data) as r:
            content = r.content.decode("utf-8")
            json = loads(re.sub("(\w+):", r'"\1":', content))
        if json['response'] == 1:
            logging.info('users_changePoints method was successfully completed.')
            return 1
        else:
            self.raise_exeption(json['error']['error_code'], "users_changePoints")

    def users_resetPoints(self, user_ids: list):
        data = {
            "user_ids": ",".join(map(str, user_ids)),
            "group_id": self.group_id,
            "secret_key": self.secret_key
        }
        with requests.post(f"https://appcm.ru/api/users.resetPoints", data=data) as r:
            content = r.content.decode("utf-8")
            json = loads(re.sub("(\w+):", r'"\1":', content))
        if json['response'] == 1:
            logging.info('users.resetPoints method was successfully completed.')
            return 1
        else:
            self.raise_exeption(json['error']['error_code'], "users_resetPoints")

    def users_ban(self, user_ids: list):
        data = {
            "user_ids": ",".join(map(str, user_ids)),
            "group_id": self.group_id,
            "secret_key": self.secret_key
        }
        with requests.post(f"https://appcm.ru/api/users.ban", data=data) as r:
            content = r.content.decode("utf-8")
            json = loads(re.sub("(\w+):", r'"\1":', content))
        if json['response'] == 1:
            logging.info('users.ban method was successfully completed.')
            return 1
        else:
            self.raise_exeption(json['error']['error_code'], "users_ban")

    def users_unban(self, user_ids: list):
        data = {
            "user_ids": ",".join(map(str, user_ids)),
            "group_id": self.group_id,
            "secret_key": self.secret_key
        }
        with requests.post(f"https://appcm.ru/api/users.unban", data=data) as r:
            content = r.content.decode("utf-8")
            json = loads(re.sub("(\w+):", r'"\1":', content))
        if json['response'] == 1:
            logging.info('users.unban method was successfully completed.')
            return 1
        else:
            self.raise_exeption(json['error']['error_code'], "users_unban")

    def raise_exeption(self, error_code, function):
        if error_code == 1:
            logging.error(f"Some of obligatory arguments are missing. Method: {function}")
            raise ValueError(f"Some of obligatory arguments are missing. Method: {function}")
        elif error_code == 2:
            raise KolizeiSecretKeyException(2)
        elif error_code == 3:
            raise KolizeiSecretKeyException(3)
        elif error_code == 4:
            logging.error(f"One of arguments is missing or invalid. Method: {function}")
            raise ValueError(f"One of arguments is missing or invalid. Method: {function}")
        elif error_code == 1000:
            raise NumberRequestsError
        elif error_code == 100:
            logging.error(f"Unknown error has occurred while completing {function} method.")
            raise Exception(f"Unknown error has occurred while completing {function} method.")
