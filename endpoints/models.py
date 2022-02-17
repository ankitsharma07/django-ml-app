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


class MLAlgorithm(models.Model):
    """
    The ML Algorithm represents the ML algorithm object

    Attributes:
        name: The name of the algorithm
        description: Short description abput how the algorithm works
        code: The code of the algorithm
        version: The version of the algorithm
        owner: The name of the owner
        created_at: The data when ML algorithm was created
        parent_endpoint: The reference to the endpoint
    """

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    code = models.TextField()
    version = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)


class MLAlgorithmStatus(models.Model):
    """
    Represents status of the ML Algorithms which can change during the time

    Attributes:
        status: The status of algorithm at the endpoint. Can be: testing, staging, production, ab_testing
        active: The boolean flag which point to currently active status
        created_by: The name of the creator
        created_at: The date of status creation
        parent_ml_algorithm: The reference to corresponding ML Algorithm
    """

    status = models.CharField(max_length=128)
    active = models.BooleanField()
    created_by = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_ml_algorithm = models.ForeignKey(
        MLAlgorithm, on_delete=models.CASCADE, related_name="status"
    )


class MLRequest(models.Model):
    """
    The MLRequest will keep information about all requests to ML algorithms

    Attributes:
        input_data: The input data to ML algorithm in JSON format
        full_response: The response of the ML Algorithm
        response: The response of the ML Algorithm in JSON format
        feedback: The feedback about the response in JSON format
        created_at: The date when request was created
        parent_ml_algorithm: The reference to ML algorithm used to compute response
    """

    input_data = models.TextField()
    full_response = models.TextField()
    response = models.TextField()
    feedback = models.CharField(max_length=2000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_ml_algorithm = models.ForeignKey(
        MLAlgorithm, on_delete=models.CASCADE
    )
