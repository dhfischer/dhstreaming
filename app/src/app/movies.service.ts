import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {environment} from '../environments/environment';

export interface Movie {
  id: number;
  title: string;
  year: number;
  cover: string;
  description: string;
  midia: string;
  age_rating: string;
  cast: string;
  director: string;
  genre: string;
  release_date: Date;
}

@Injectable({
  providedIn: 'root'
})
export class MoviesService {

  constructor(
    private http: HttpClient
  ) { }

  list(searchPattern: string): Observable<Array<Movie>> {
    let url = `${environment.apiURL}/movies`;
    if (searchPattern) {
      url += `?search=${searchPattern}`;
    }
    return this.http.get<Array<Movie>>(url);
  }

  get(id: number): Observable<Movie> {
    let url = `${environment.apiURL}/movies/${id}`;
    return this.http.get<Movie>(url);
  }

  create(movieData: Movie): Observable<Movie> {
    const url = `${environment.apiURL}/movies/`;
    return this.http.post<Movie>(url, movieData);
  }

  update(movieData: Movie): Observable<Movie> {
    const url = `${environment.apiURL}/movies/${movieData.id}/`;
    return this.http.put<Movie>(url, movieData);
  }

  remove(id: number): Observable<void> {
    const url = `${environment.apiURL}/movies/${id}/`;
    return this.http.delete<void>(url);
  }
}
