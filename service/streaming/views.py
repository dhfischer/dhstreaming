from django.contrib.auth import get_user_model
from django.http import Http404

from rest_framework import filters, permissions, views, viewsets, status
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from .controllers import is_movie_favourite, list_movies, mark_movie_as_favourite
from .serializers import FavouriteSerializer, MovieSerializer, MovieWatchedSerializer, UserSerializer
from .models import Favourite, Movie, MovieWatched


class UserViewSet(viewsets.ModelViewSet):
    """
    User viewset.
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class MovieViewSet(viewsets.ModelViewSet):
    """
    Movie viewset.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']


class FavouriteViewSet(viewsets.ModelViewSet):
    """
    Favourite viewset.
    """
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
    permission_classes = [permissions.IsAuthenticated]


class MovieWatchedViewSet(viewsets.ModelViewSet):
    """
    MovieWatched viewset.
    """
    queryset = MovieWatched.objects.all()
    serializer_class = MovieWatchedSerializer
    permission_classes = [permissions.IsAuthenticated]


class MovieView(views.APIView):
    """
    Movies view
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk=None):
        if pk is None:
            # Listar todos os filmes
            movies = list_movies()
            return Response(movies)
        else:
            # Buscar um filme por ID
            movie = self.get_object(pk)
            serializer = MovieSerializer(movie)
            return Response(serializer.data)

    def post(self, request):
        # Criar um novo filme
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        # Buscar um filme por ID
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        # Atualizar um filme por ID
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Excluir um filme por ID
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FavouriteView(views.APIView):
    """
    Favourite view
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Check if a given movie is favourite
        """
        # Get the movie
        movie_id = request.GET['id']
        movie = Movie.objects.get(id=movie_id)

        # Check if is favourite
        is_favourite = is_movie_favourite(movie, request.user)

        # Return the response data
        response_data = {
            'is_favourite': is_favourite
        }
        return Response(response_data)

    def post(self, request, *args, **kwargs):
        """
        Mark a movie as favourite (or not).
        """
        # Get the movie
        # if 'id' not in request.POST:
        #     raise APIException('The `id` must be informed')
        movie_id = request.data.get('movie_id')
        movie = Movie.objects.get(id=movie_id)

        # Get the desired state
        if 'state' not in request.POST:
            raise APIException('The `state` must be informed')
        state = request.POST['state'] == 'true'

        # Mark as favourite
        mark_movie_as_favourite(movie, state, request.user)

        # Return the response
        return Response({})
