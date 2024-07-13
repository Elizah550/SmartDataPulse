from django.apps import AppConfig


class HomepageConfig(AppConfig):
    name = 'homepage'

    def ready(self):
        from jobs import cron_schedule
        cron_schedule.start()
