import pyjokes
from core.serializers import JokesSerializer
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from rest_framework import exceptions
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

JOKES_CATEGORIES = ["neutral", "chuck", "all", "twister"]
JOKES_LANGUAGES = ["en", "de", "es", "gl", "eu", "it"]


@extend_schema_view(
    get=extend_schema(
        parameters=[
            OpenApiParameter(
                "category",
                OpenApiTypes.STR,
                enum=JOKES_CATEGORIES,
                description="Jokes category.",
                default="neutral",
            ),
            OpenApiParameter(
                "language",
                OpenApiTypes.STR,
                enum=JOKES_LANGUAGES,
                description="Jokes language.",
                default="en",
            ),
        ],
    ),
)
class GetJokes(GenericAPIView):
    serializer_class = JokesSerializer

    def get_query_params(self) -> dict[str, str]:
        category = self.request.query_params.get("category", JOKES_CATEGORIES[0])
        language = self.request.query_params.get("language", JOKES_LANGUAGES[0])

        if category not in JOKES_CATEGORIES:
            raise exceptions.ValidationError(f"Invalid Jokes category. Available categories: {JOKES_CATEGORIES}")

        if language not in JOKES_LANGUAGES:
            raise exceptions.ValidationError(f"Invalid Jokes language. Available languages: {JOKES_LANGUAGES}")

        return {"category": category, "language": language}

    def get(self, request: Request, **kwargs):
        try:
            jokes = pyjokes.get_jokes(**self.get_query_params())
            return Response({"jokes": jokes})
        except exceptions.ValidationError as err:
            raise err
