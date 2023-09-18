import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Movie, MoviesService } from '../movies.service';

@Component({
  selector: 'app-movie-edit',
  templateUrl: './movie-edit.component.html',
  styleUrls: ['./movie-edit.component.scss'],
})
export class MovieEditComponent implements OnInit {
  movie: Movie = {
    id: 0,
    title: '',
    year: 0,
    cover: '',
    description: '',
    midia: '',
    age_rating: '',
    cast: '',
    director: '',
    genre: '',
    release_date: new Date(),
  };

  constructor(
    private movieService: MoviesService,
    private router: Router,
    private route: ActivatedRoute
  ) {}

  ngOnInit(): void {
    this.route.params.subscribe((params) => {
      const movieId = +params['id']; // Obtém o ID do filme da URL
      this.movieService.get(movieId).subscribe((movie) => {
        this.movie = movie;
      });
    });
  }

  onSubmit(): void {
    this.movieService.update(this.movie).subscribe(() => {
      this.router.navigate(['/movie-list']); // Redireciona de volta para a lista de filmes após a edição bem-sucedida
    });
  }
}
