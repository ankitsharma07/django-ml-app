"""
# author: Ankit Sharma [@nezubn]
# filename: serializers.py
# Copyright 2022-07-26
"""

"""
Serializers will help with packing and unpacking database objects into JSON objects.
In `Endpoints` and `MLAlgorithm` serializers, we defined all read-only fields.
This is because, we will create and modify our objects only on the server-side.
For `MLAlgorithmStatus`, fields `status`, `created_by`, `created_at` and `parent_mlalgorithm`
are in read and write mode, we will use the to set algorithm status by REST API.
For `MLRequest` serializer there is a `feedback`field that is left in read and
write mode - it will be needed to provide feedback about predictions to the server.
"""

from django_ml_app.endpoints.models import (
    Endpoint,
    MLAlgorithm,
    MLAlgorithmStatus,
    MLRequest,
)
from rest_framework import serializers


class EndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endpoint
        read_only_fields = ("id", "name", "owner", "created_at")
        fields = read_only_fields


class MLAlgorithmSerializer(serializers.ModelSerializer):
    current_status = serializers.SerializerMethodField(read_only=True)

    def get_current_status(self, mlalgorithm):
        return (
            MLAlgorithmStatus.objects.filter(parent_ml_algorithm=mlalgorithm)
            .latest("created_at")
            .status
        )

    class Meta:
        model = MLAlgorithm
        read_only_fields = (
            "id",
            "name",
            "description",
            "code",
            "version",
            "owner",
            "created_at",
            "parent_endpoint",
            "current_status",
        )
        fields = read_only_fields
