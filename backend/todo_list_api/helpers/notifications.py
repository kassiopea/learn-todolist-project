class Notifications:
    def __init__(self, result_type):
        self.result_type = result_type
        self.result = {self.result_type: []}
        self.result_notification = {self.result_type: {}}

    def add_notification(self, field, message):
        self.result[self.result_type].append({field: message})

    def create_notification(self, field, message):
        self.result_notification[self.result_type][field] = message
        return self.result_notification

    def get_notifications(self):
        return self.result
