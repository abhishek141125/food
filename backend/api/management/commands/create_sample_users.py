from django.core.management.base import BaseCommand
from django.conf import settings
import csv
from pathlib import Path


class Command(BaseCommand):
    help = 'Create sample users from backend/data/users.csv'

    def handle(self, *args, **options):
        data_dir = Path(settings.BASE_DIR) / 'data'
        csv_file = data_dir / 'users.csv'
        if not csv_file.exists():
            self.stdout.write(self.style.ERROR(f'CSV file not found: {csv_file}'))
            return

        import django
        django.setup()
        from django.contrib.auth.models import User

        created = 0
        skipped = 0
        with csv_file.open(newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader, None)
            for row in reader:
                if not row or len(row) < 3:
                    continue
                username, email, pwd = row[0].strip(), row[1].strip(), row[2].strip()
                if not username:
                    continue
                if User.objects.filter(username=username).exists():
                    self.stdout.write(self.style.NOTICE(f'Skipped existing: {username}'))
                    skipped += 1
                    continue
                User.objects.create_user(username=username, email=email or None, password=pwd)
                self.stdout.write(self.style.SUCCESS(f'Created: {username}'))
                created += 1

        self.stdout.write(self.style.SUCCESS(f'Done. Created: {created}, Skipped: {skipped}'))
