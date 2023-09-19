import os
import django
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service.settings")
django.setup()

from streaming.models import Favourite, Movie, MovieWatched, User

print('Starting populate script')

# Remove existing data
print('- Removing existing data')
User.objects.all().delete()
Movie.objects.all().delete()
Favourite.objects.all().delete()
MovieWatched.objects.all().delete()


# Generate some users
print('- Generating some user')
User.objects.create(
    username='pedro.carvalho',
    email='pedro@mail.com',
    first_name='Pedro',
    last_name='Carvalho',
    birth_date=date(1987, 4, 17),
)
User.objects.create(
    username='jorge.campos',
    email='jorge@mail.com',
    first_name='Jorge',
    last_name='Campos',
    birth_date=date(1992, 11, 5),
)
User.objects.create(
    username='julia.martins',
    email='julia@mail.com',
    first_name='Julia',
    last_name='Martins',
    birth_date=date(1989, 7, 23),
    type=User.Type.ADMIN
)
for user in User.objects.all():
    user.set_password('fgv123')
    user.save()

# Generate some movies
print('- Generating some movies')
Movie.objects.create(
    title='The Shawshank Redemption',
    year=1994,
    cover='https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVy'
          'MTMxODk2OTU@._V1_UY400_CR0,0,270,400_AL_.jpg',
    description='O idoso patriarca de uma dinastia do crime organizado na cidade de Nova Iorque do '
                'pós-guerra transfere o controlo do seu império clandestino para o seu relutante filho mais novo.',
    midia='https://www.youtube.com/embed/PLl99DlL6b4',
    age_rating='16+',  
    cast='Al Pacino, Marlon Brando',
    director='Francis Ford Coppola',
    genre='Ação, Drama',
    release_date=date(2023, 9, 15)
)
Movie.objects.create(
    title='The Godfather',
    year=1972,
    cover='https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyN'
          'zkwMjQ5NzM@._V1_UY400_CR1,0,280,400_AL_.jpg',
    description='O idoso patriarca de uma dinastia do crime organizado na cidade de Nova Iorque do pós-guerra  '
                'transfere o controlo do seu império clandestino para o seu relutante filho mais novo.',
    midia='https://www.youtube.com/embed/UaVTIH8mujA',
    age_rating='14+',
    cast='Al Pacino, Marlon Brando', 
    director='Francis Ford Coppola',
    genre='Ação, Drama', 
    release_date=date(1972, 7, 7) 
)
Movie.objects.create(
    title='The Dark Knight',
    year=2008,
    cover='https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UY400_CR0,0,270,'
          '400_AL_.jpg',
    description='When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept '
                'one of the greatest psychological and physical tests of his ability to fight injustice.',
    midia='https://www.youtube.com/embed/kmJLuwP3MbY',
    age_rating='16+',
    cast='Morgan Freeman, Tim Robbins', 
    director='Frank Darabont',
    genre='Drama', 
    release_date=date(1995, 3, 17) 
)
Movie.objects.create(
    title='The Lord of the Rings: The Return of the King',
    year=2003,
    cover='https://m.media-amazon.com/images/M/MV5BNzA5ZDNlZWMtM2NhNS00NDJjLTk4NDItYTRmY2EwMWZlMTY3XkEyXkFqcGdeQXVyN'
          'zkwMjQ5NzM@._V1_UY400_CR0,0,270,400_AL_.jpg',
    description='Gandalf e Aragorn lideram o Mundo dos Homens contra o exército de Sauron para desviar o olhar de '
                'Frodo e Sam enquanto eles se aproximam da Montanha da Perdição com o Um Anel.',
    midia='https://www.youtube.com/embed/zckJCxYxn1g',
    age_rating='14+',
    cast='Elijah Wood, Ian McKellen', 
    director='Peter Jackson',
    genre='Ação, Aventura', 
    release_date=date(2003, 12, 25) 
)
Movie.objects.create(
    title='Pulp Fiction',
    year=1994,
    cover='https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNz'
          'kwMjQ5NzM@._V1_UY400_CR0,0,270,400_AL_.jpg',
    description='As vidas de dois assassinos da máfia, um boxeador, um gangster e sua esposa, '
                'e uma dupla de bandidos de restaurante se entrelaçam em quatro histórias de violência e redenção.',
    midia='https://www.youtube.com/embed/tGpTpVyI_OQ',
    age_rating='18+',
    cast='John Travolta, Samuel L. Jackson', 
    director='Quentin Tarantino',
    genre='Ação', 
    release_date=date(1995, 3, 3) 
)
Movie.objects.create(
    title='Forrest Gump',
    year=1994,
    cover='https://m.media-amazon.com/images/M/MV5BNWIwODRlZTUtY2U3ZS00Yzg1LWJhNzYtMmZiYmEyNmU1NjMzXkEyXkFqcGdeQXVyMT'
          'QxNzMzNDI@._V1_UY400_CR0,0,270,400_AL_.jpg',
    description='As presidências de Kennedy e Johnson, a Guerra do Vietname, o escândalo Watergate e '
                'outros acontecimentos históricos desenrolam-se a partir da perspectiva de um homem do Alabama com um QI '
                'de 75, cujo único desejo é reencontrar a sua namorada de infância.',
    midia='https://www.youtube.com/embed/bLvqoHBptjg',
    age_rating='16+',
    cast='Tom Hanks, Robin Wright', 
    director='Robert Zemeckis',
    genre='Drama', 
    release_date=date(1994, 12, 7) 
)
Movie.objects.create(
    title='Inception',
    year=2010,
    cover='https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_UY400_CR0,0,'
          '270,400_AL_.jpg',
    description='Um ladrão que rouba segredos corporativos através do uso de '
                'tecnologia de compartilhamento de sonhos recebe a tarefa inversa de plantar uma ideia '
                'na mente de um CEO, mas seu passado trágico pode condenar o projeto e sua equipe ao desastre.',
    midia='https://www.youtube.com/embed/hstBN0Qkqhc',
    age_rating='16+',
    cast='Nome do Ator, Outro Ator', 
    director='Nome do Diretor',
    genre='Ação, Drama', 
    release_date=date(2023, 9, 15) 
)
Movie.objects.create(
    title='The Matrix',
    year=1999,
    cover='https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqc'
          'GdeQXVyNjU0OTQ0OTY@._V1_UY400_CR0,0,260,400_AL_.jpg',
    description='When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he discovers the '
                'shocking truth--the life he knows is the elaborate deception of an evil cyber-intelligence.',
    midia='https://www.youtube.com/embed/nUEQNVV3Gfs',
    age_rating='16+',
    cast='Keanu Reeves, Carrie-Anne Moss', 
    director='Lana Wachowski, Lilly Wachowski',
    genre='Ação, Aventura', 
    release_date=date(1999, 5, 21) 
)
Movie.objects.create(
    title='Saving Private Ryan',
    year=1998,
    cover='https://m.media-amazon.com/images/M/MV5BZjhkMDM4MWItZTVjOC00ZDRhLThmYTAtM2I5NzBmNmNlMzI1XkEyXkFqcGdeQXVy'
          'NDYyMDk5MTU@._V1_UY400_CR0,0,270,400_AL_.jpg',
    description='Following the Normandy Landings, a group of U.S. soldiers go behind enemy lines to retrieve a '
                'paratrooper whose brothers have been killed in action.',
    midia='https://www.youtube.com/embed/9CiW_DgxCnQ',
    age_rating='16+',
    cast='Nome do Ator, Outro Ator', 
    director='Nome do Diretor',
    genre='Ação, Drama', 
    release_date=date(2023, 9, 15) 
)

# Create some favourite movies for each user
print('- Creating favourite movies for each user')
for user in User.objects.all():
    from random import randint
    num_favourite_movies = randint(1, 3)
    movies = Movie.objects.order_by('?')[:num_favourite_movies]
    for movie in movies:
        Favourite.objects.create(
            user=user,
            movie=movie
        )

print('Finished!')
