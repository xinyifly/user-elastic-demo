from django.conf import settings
import requests
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


class UserViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                  mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SearchUserViewSet(viewsets.ViewSet):
    """
    Keywords: username, first_name, last_name, address, birthday, description
    """
    def list(self, request):
        params = request.query_params
        limit = params.get('limit', 100)
        offset = params.get('offset', 0)
        search_body = {'from': offset, 'size': limit, 'sort': [{'id': 'asc'}]}

        keywords = [
            'username', 'first_name', 'last_name', 'address', 'birthday',
            'description'
        ]
        term = {key: params[key] for key in params if key in keywords}

        if term:
            search_body['query'] = {'term': term}

        response = requests.post(settings.ELASTIC_URL + '/users/_search',
                                 json=search_body)

        hits = response.json()['hits']['hits']
        users = [hit['_source'] for hit in hits]

        total = response.json()['hits']['total']

        return Response(users,
                        status.HTTP_200_OK,
                        headers={'X-Total-Count': total})
