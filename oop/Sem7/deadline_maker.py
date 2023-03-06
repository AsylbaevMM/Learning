from datetime import datetime, timedelta


class DeadlineMaker():
    def deadline(self, days_before_deadline):
        return datetime.now() + timedelta(days=days_before_deadline)