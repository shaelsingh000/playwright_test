import os

ENV = os.getenv("ENV", "qa")

CONFIG = {
    "qa": {
        "base_url": "https://www.saucedemo.com/",
        "headless": True
    },
    "dev": {
        "base_url": "https://www.saucedemo.com/",
        "headless": False
    }
}