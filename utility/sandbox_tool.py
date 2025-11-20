import os
from koyeb import Sandbox
import dotenv

dotenv.load_dotenv()


class Sandbox:
    def __init__(self):
        self.token = os.getenv("KOYEB_API_TOKEN")
