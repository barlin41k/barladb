from datetime import datetime
class Log:
    @staticmethod
    def enter_log(message: str):
        current_time = datetime.now()
        name = current_time.strftime("%d.%m.%y")
        log_time = current_time.strftime("%H:%M.%S, %d.%m.%y")
        with open(f"log_{name}.txt", "a+", encoding="utf-8") as log:
            if not log.read():
                log.write(f"{log_time}: {message}\n")
            else:
                log.write(f"\n{log_time}: {message}")