import pytest
from dotenv import load_dotenv
import os
from kolizei_api import kolizei_api

def load_env_variables():
    load_dotenv(".env")
    GROUP_ID = os.environ.get("GROUP_ID")
    KOLIZEI_TOKEN = os.environ.get("KOLIZEI_TOKEN")


def test_incorrect_group_id():
    with pytest.raises(kolizei_api.KolizeiSecretKeyException):
        kolizei_api.Kolizei_api


if __name__ == "__main__":
    load_env_variables()