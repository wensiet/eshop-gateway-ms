import datetime
import logging

import requests


class LokiHandler(logging.Handler):
    def __init__(self, url, repeat=True):
        super().__init__()
        self.url = url
        self.repeat = repeat

    def emit(self, record):
        log_entry = self.format(record)
        if self.repeat:
            print(f"{datetime.datetime.utcnow()} \t {record.levelname} \t\t {log_entry}")
        self.send_to_loki(record)

    def send_to_loki(self, log_entry):
        if log_entry is not None:
            level = "DEBUG"
            if log_entry.levelname == "INFO":
                level = "INFO"
            elif log_entry.levelname == "ERROR":
                level = "ERROR"
            elif log_entry.levelname == "CRITICAL":
                level = "ERROR"
            elif log_entry.levelname == "WARNING":
                level = "WARN"
            headers = {"Content-Type": "application/json"}
            payload = {
                "streams": [
                    {
                        "stream":
                            {
                                "environment": "local",
                                "level": level,
                                "service": "eshop-gateway-ms",
                            },
                        "values":
                            [
                                [str(int(datetime.datetime.now().timestamp()))
                                 + "000000000", log_entry.message]
                            ]
                    }
                ]
            }
            try:
                response = requests.post(self.url, headers=headers, json=payload)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"Error sending log entry to Loki: {e}")


def get_logger(loki_url: str, repeat: bool = True) -> logging.Logger:
    logger = logging.getLogger("fastapi")
    logger.setLevel(logging.DEBUG)
    loki = LokiHandler(loki_url, repeat)
    logger.addHandler(loki)
    return logger
