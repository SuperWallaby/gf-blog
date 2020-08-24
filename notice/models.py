from django.db import models
from share import models as share_models
from django.contrib.auth.models import User

# Create your models here.
class Notice(share_models.PostTypeModel):
    BOOKING = 'BOOKING'
    TEMPLATE_A = 'TEMPLATE_A'
    ALL = 'ALL'
    SUPER_CLASS = (
    ('BOOKING', 'BOOKING'),
    ('TIME_SPACE', 'TIME_SAPCE'),
    ('ALL', 'ALL'),
    )

    pin = models.BooleanField(default=False)
    notice_target = models.CharField(
        max_length=10,
        choices=SUPER_CLASS,
        default=ALL,
    )

    def __str__(self):
        return self.title 
