from django.db import models


# Create your models here.
class PC(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID',
        db_index=True,
    )
    name = models.CharField(null=False, max_length=225, help_text='Compute name')
    host = models.CharField(null=False, max_length=225, help_text='Compute IP')

    laboratory = models.ForeignKey(
        'auto.Laboratory',
        related_name='laboratory',
        on_delete=models.CASCADE,
        null=True,
        help_text='laboratory id',
    )

    class Meta:
        db_table = 'pc'


class Laboratory(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID',
        db_index=True,
    )
    # 实验室名
    name = models.CharField(null=False, max_length=225, help_text='Laboratory name')
    compute_count = models.IntegerField(default=0)
    city = models.ForeignKey(
        'auto.City',
        related_name='city',
        on_delete=models.CASCADE,
        null=True,
        help_text='city id',
    )

    class Meta:
        db_table = 'laboratory'


class City(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID',
        db_index=True,
    )
    name = models.CharField(null=False, max_length=225, help_text='City name')
    compute_count = models.IntegerField(default=0)

    class Meta:
        db_table = 'city'


class RequestTime(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID',
        db_index=True,
    )
    path = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.DurationField()
    status_code = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.duration:
            self.duration = self.end_time - self.start_time
        super(RequestTime, self).save(*args, **kwargs)

    class Meta:
        db_table = 'timeRequest'
