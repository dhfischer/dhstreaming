import { Component, OnInit } from '@angular/core';
import {Movie, MoviesService} from '../movies.service';
import {AuthService, User} from '../auth.service';
import { Router } from '@angular/router';


@Component({
  selector: 'app-movie-list',
  templateUrl: './movie-list.component.html',
  styleUrls: ['./movie-list.component.scss']
})
export class MovieListComponent implements OnInit {
  user: User = {
    id: 0,
    url: '',
    username: '',
    email: '',
    type: '',
    first_name: '',
    last_name: '',
    birth_date: '',
    address: '',
  };

  movies: Array<Movie> | undefined;
  searchPattern: string = '';
  isUserAdmin: boolean = true;

  constructor(
    private moviesSrv: MoviesService,
    private authService: AuthService,
    private router: Router,
    // private dialog: MatDialog,
  ) { }

  ngOnInit(): void {
    this.loadMovies();
  }

  loadMovies() {
    this.moviesSrv.list(this.searchPattern).subscribe((movies) => {
      this.movies = movies;
    });
  }

  clearSearch(): void {
    this.searchPattern = '';
  }

  onSearchChange(): void {
    this.loadMovies();
  }

  isAdminUser(): boolean {
    return this.isUserAdmin;
  }

  private loadUserInfo(): void {
    // Chame o serviço de autenticação para obter informações do usuário.
    this.authService.getUserInfo(this.user.id).subscribe((user: User) => {
      // Verifique se o usuário é um administrador com base nas informações do usuário.
      if(user.type === "Regular") {
        this.isUserAdmin = false;
      } else {
        this.isUserAdmin = true;
      }
    });
  }
}
