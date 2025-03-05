from celery.task.schedules import crontab
from celery.decorators import periodic_task
from auto.models import PC, Laboratory, City
from django.db import transaction


@periodic_task(run_every=crontab(minute=0, hour=0))
def time_task():
    with transaction.atomic():
        laboratory = Laboratory.objects.all()
        for lab in laboratory:
            compute_count = PC.objects.only('id').filter(laboratory=lab).count()
            lab.update(compute_count=compute_count)
        city = City.objects.all()
        for cy in city:
            laboratory = Laboratory.objects.only('id').filter(city=cy)
            count = 0
            for lab in laboratory:
                compute_count = PC.objects.only('id').filter(laboratory=lab).count()
                lab.update(compute_count=compute_count)
                count += compute_count
            cy.update(compute_count=count)

    return True



