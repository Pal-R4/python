import time
from plyer import notification
if __name__=='__main__':
 while True:
    notification.notify(
        title="welcome",
        message="how are you?",
        timeout=5
    )
    time.sleep(15)