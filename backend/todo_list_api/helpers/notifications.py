class Notifications:
    def __init__(self, result_type):
        self.result_type = result_type
        self.result = {self.result_type: []}

    def add_notification(self, field, message):
        self.result[self.result_type].append({field: message})

    def get_notifications(self):
        return self.result
