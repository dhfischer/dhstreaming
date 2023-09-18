import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import {Movie, MoviesService} from '../movies.service';

@Component({
  selector: 'app-movie-create',
  templateUrl: './movie-create.component.html',
  styleUrls: ['./movie-create.component.scss']
})
export class MovieCreateComponent implements OnInit {
  newMovie: Movie = {
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
    release_date: new Date()
  };

  constructor(private movieService: MoviesService, private router: Router) {}

  ngOnInit(): void {
  }

  onSubmit(): void {
    this.movieService.create(this.newMovie).subscribe(() => {
      this.router.navigate(['/movie-list']); // Redireciona de volta para a lista de filmes após a criação bem-sucedida
    });
  }
}
