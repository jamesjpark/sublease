from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics

class GetPostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = PostSerializer

class PostListApiView(APIView):
    # add permission to check if user is authenticated
    def get(self, request, *args, **kwargs):
        '''
        List all the post items for given requested user
        '''
        permission_classes = (AllowAny)
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        permission_classes = (IsAuthenticated)

        data = {
            'title': request.data.get('title'), 
            'text': request.data.get('text'),
            'address': request.data.get('address'),
            'price': request.data.get('price'), 
            'user': request.user.id
        }
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)