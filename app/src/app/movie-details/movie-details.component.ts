import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from "@angular/router";
import {Movie, MoviesService} from '../movies.service';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';


@Component({
  selector: 'app-movie-details',
  templateUrl: './movie-details.component.html',
  styleUrls: ['./movie-details.component.scss']
})
export class MovieDetailsComponent implements OnInit {

  movie: Movie | undefined;
  showPlayIcon: boolean = false;
  safeVideoEmbedUrl: SafeResourceUrl | undefined;

  constructor(
    private route: ActivatedRoute,
    private movieSrv: MoviesService,
    private sanitizer: DomSanitizer
  ) { }

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.movieSrv.get(id).subscribe((movie) => {
      this.movie = movie;
      this.safeVideoEmbedUrl = this.sanitizer.bypassSecurityTrustResourceUrl(movie.midia);
    });
  }

}
