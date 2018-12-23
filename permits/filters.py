import django_filters
from rest_framework import filters
from datetime import datetime
from .models import FoodFacilityPermits

class FoodFacilityPermitsFilter(filters.FilterSet):
    expiration_date = django_filters.MethodFilter()
    location_description = django_filters.MethodFilter()

    class Meta:
        model = FoodFacilityPermits
        fields = ['applicant_name', 'expiration_date', 'location_description']

    def filter_expiration_date(self, queryset, value):
        if value:
            try:
                expiration_date = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                expiration_date = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            return queryset.filter(expiration_date__lte=expiration_date)
        return queryset

    def filter_location_description(self, queryset, value):
        if value:
            queryset.filter(location_description__icontains=value)
        return queryset
