from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from status.models import Status
from .serializers import StatusSerializers

    # Process - 1: Single function for only Get and Post methods

'''
class StatusListSearchAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, format = None):
        qs = Status.objects.all()
        serializer = StatusSerializers(qs, many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        qs = Status.objects.all()
        serializer = StatusSerializers(qs, many=True)
        return Response(serializer.data)
'''
    # Process - 2: CRUD using 4 difference Function
'''
class StatusAPIView(generics.ListAPIView):  # Get methods
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializers
    
    # queryset = Status.objects.all()
    #             or
    # def get_queryset(self):
    #     qs = Status.objects.all()
    #     query = self.request.GET.get('q')
    #     if query is not None:
    #         qs = qs.filter(image=query)
    #     return qs


class StatusCreateAPIView(generics.CreateAPIView):  # Post Methods
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializers


class StatusDetailAPIView(generics.RetrieveAPIView):  # Get with ID methods
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializers

    # if pass the id as parameter, then get_object function object need to call
    # def get_object(self, *args, **kwargs):
    #     kwargs = self.kwargs
    #     kw_id = kwargs.get('id')
    #     return Status.objects.get(id=kw_id)


class StatusUpdateAPIView(generics.UpdateAPIView):  # Put methods
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializers


class StatusDeleteAPIView(generics.DestroyAPIView):     # Delete Methods
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializers
'''

    # Process - 3: CRUD using 2 difference Function
'''
class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView):  # Get methods
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializers

    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(image=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StatusDetailAPIView(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):  # Get with ID methods
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class = StatusSerializers

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
'''


    # Process - 4: On API Endpoint for CRUDL / CRUD using single Function
class StatusAPIView(
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.RetrieveModelMixin,
                    generics.ListAPIView):  # Get methods
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializers

    def get_queryset(self):
        request = self.request
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(image=query)
        return qs

    def get_object(self):
        request = self.request
        passed_id = request.GET.get('id', None)
        queryset = self.get_queryset()
        obj = None
        if passed_id is not None:
            obj = get_object_or_404(queryset, id=passed_id)
            self.check_object_permissions(self, obj)
        return obj

    def get(self, request, *args, **kwargs):
        passed_id = request.GET.get('id', None)
        if passed_id is not None:
            return self.retrieve(request, *args, **kwargs)
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


