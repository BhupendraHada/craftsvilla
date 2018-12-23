from django.db import models
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
# Create your models here.


class LocationField(models.CharField):
    description = "Location formatted for mapping."

    def get_db_prep_value(self, value, *args, **kwargs):
        if value is None:
            return None
        return value

    def to_python(self, value):
        if value is None:
            return value
        try:
            return str(value)
        except (TypeError, ValueError):
            raise ValidationError("")

    def from_db_value(self, value, expression, connection, context):
        return self.to_python(value)


class Country(models.Model):
    class Meta:
        db_table = 'countries'

    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class State(models.Model):
    class Meta:
        db_table = 'states'

    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class City(models.Model):
    class Meta:
        db_table = 'cities'

    name = models.CharField(max_length=200)
    state = models.ForeignKey(State)
    is_active = models.BooleanField(default=True)


class Location(models.Model):
    class Meta:
        db_table = 'locations'

    name = models.CharField(max_length=200)
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300)
    landmark = models.CharField(max_length=300)
    city = models.ForeignKey(City, related_name='location_city')
    state = models.ForeignKey(State, related_name='location_state')
    country = models.ForeignKey(Country, related_name='location_country', null=True)
    pincode = models.CharField(verbose_name='PIN Code', max_length=10, null=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=8, null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=8, null=True)
    created_by = models.ForeignKey(User, related_name='location_added_by')
    modified_by = models.ForeignKey(User, related_name='location_modified_by')


class FoodFacilityPermits(models.Model):
    class Meta:
        db_table = 'food_facility_permits'

    location = models.ForeignKey(Location)
    applicant_name = models.CharField(verbose_name='Name of Permit Holder', max_length=200)
    facility_type = models.CharField(max_length=200)
    cnn = models.IntegerField()
    location_description = models.TextField()
    address = models.CharField(max_length=500)
    block_lot = models.CharField(max_length=200)
    block = models.CharField(max_length=200)
    lot = models.CharField(max_length=200)
    permit = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    food_items = models.CharField(max_length=500)
    x = models.IntegerField()
    y = models.IntegerField()
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    schedule = models.URLField()
    noi_sent = models.DateField()
    approved_date = models.DateField()
    received_date = models.DateField()
    prior_permit = models.BooleanField()
    expiration_date = models.DateField()
    location = LocationField()
    created_by = models.ForeignKey(User, related_name='permits_added_by')
    modified_by = models.ForeignKey(User, related_name='permits_modified_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
