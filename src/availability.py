```python
import time
from src.config import Config

class Availability:
    def __init__(self):
        self.config = Config()
        self.is_available = False

    def check_availability(self):
        try:
            response = self.config.get('SSO_SERVICE_URL')
            if response.status_code == 200:
                self.is_available = True
            else:
                self.is_available = False
        except Exception as e:
            print(f"Error checking availability: {e}")
            self.is_available = False

        return self.is_available

    def retry_availability(self, retries=3, delay=5):
        for i in range(retries):
            if self.check_availability():
                return True
            time.sleep(delay)
        return False
```