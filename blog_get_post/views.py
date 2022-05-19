#import rest_framework
from rest_framework.views import Response, APIView
from .models import BLOGS


class BlogAPIView(APIView):
    def get(self, request):
        return Response(data=BLOGS)

    def post(self, request):
        new_blog = request.data
        BLOGS.append(new_blog)

        return Response(data=new_blog)

    def put(self, request):
        ...

