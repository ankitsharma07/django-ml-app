from django.db import models


class Endpoint(models.Model):
    """
    The Endpoint object represents the ML API endpoint

    Attributes:
        name: The name of the endpoint, it will be used in the API URI,
        owner: The string with owner name,
        created_at: The date when endpoint was created
    """

    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
