from django.core.management.base import BaseCommand
from django.utils import timezone
from vendor_app.models import Vendor, HistoricalPerformance

class Command(BaseCommand):
    help = 'Update historical performance data for all vendors'

    def handle(self, *args, **kwargs):
        vendors = Vendor.objects.all()
        for vendor in vendors:
            HistoricalPerformance.objects.create(
                vendor=vendor,
                date=timezone.now(),
                on_time_delivery_rate=vendor.on_time_delivery_rate,
                quality_rating_avg=vendor.quality_rating_avg,
                average_response_time=vendor.average_response_time,
                fulfillment_rate=vendor.fulfillment_rate
            )
        self.stdout.write(self.style.SUCCESS('Successfully updated historical performance data'))
