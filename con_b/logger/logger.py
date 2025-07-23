from datetime import datetime

class Logger:
    def __init__(self, file_path="log.txt"):
        self.file_path = file_path

    def log(self, message: str):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.file_path, "a", encoding="utf-8") as f:
            f.write(f"[{time}] {message}\n")
