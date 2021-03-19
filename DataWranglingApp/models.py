# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Airlines(models.Model):
    carrier = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Airlines'

    def __str__(self):
            return self.name

class Airports(models.Model):
    faa = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    lat = models.CharField(max_length=255)
    lon = models.CharField(max_length=255)
    alt = models.IntegerField()
    tz = models.IntegerField()
    dst = models.CharField(max_length=255)
    tzone = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Airports'


class Flights(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    dep_time = models.IntegerField()
    flight = models.IntegerField()
    origin = models.ForeignKey(Airports, models.DO_NOTHING, db_column='origin')
    dest = models.CharField(max_length=255)
    schd_dep_time = models.IntegerField()
    dep_delay = models.IntegerField()
    arr_time = models.IntegerField()
    sched_arr_time = models.IntegerField()
    arr_delay = models.IntegerField()
    carrier = models.ForeignKey(Airlines, models.DO_NOTHING, db_column='carrier')
    tailnum = models.CharField(max_length=255)
    air_time = models.IntegerField()
    distance = models.IntegerField()
    hour = models.IntegerField()
    minute = models.IntegerField()
    time_hour = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Flights'


class Planes(models.Model):
    tailnum = models.CharField(primary_key=True, max_length=255)
    year = models.IntegerField()
    type = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    engines = models.IntegerField()
    seats = models.IntegerField()
    speed = models.CharField(max_length=255)
    engine = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'Planes'


class Weather(models.Model):
    origin = models.OneToOneField(Airports, models.DO_NOTHING, db_column='origin', primary_key=True)
    year = models.IntegerField()
    day = models.IntegerField()
    hour = models.IntegerField()
    temp = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    dewp = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    humid = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    wind_dir = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    wind_speed = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    wind_gust = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    precip = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    pressure = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    visib = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    time_hour = models.DateTimeField()
    month = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Weather'
        unique_together = (('origin', 'year', 'day', 'hour', 'month'),)


class WeatherWith3Doublons(models.Model):
    origin = models.OneToOneField(Airports, models.DO_NOTHING, db_column='origin', primary_key=True)
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    hour = models.IntegerField()
    temp = models.DecimalField(max_digits=10, decimal_places=0)
    dewp = models.DecimalField(max_digits=10, decimal_places=0)
    humid = models.DecimalField(max_digits=10, decimal_places=0)
    wind_dir = models.IntegerField(blank=True, null=True)
    wind_speed = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    wind_gust = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    precip = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    pressure = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    visib = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    time_hour = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Weather_with_3_doublons'
        unique_together = (('origin', 'year', 'month', 'day', 'hour'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
