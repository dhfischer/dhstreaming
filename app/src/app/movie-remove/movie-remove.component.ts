import { Component, OnInit, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { MoviesService } from '../movies.service';

@Component({
  selector: 'app-movie-remove',
  templateUrl: './movie-remove.component.html',
  styleUrls: ['./movie-remove.component.scss']
})
export class MovieRemoveComponent implements OnInit {

  constructor(
    @Inject(MAT_DIALOG_DATA) public data: any,
    private dialogRef: MatDialogRef<MovieRemoveComponent>,
    private moviesService: MoviesService,
  ) { }

  ngOnInit(): void {
  }

  confirmRemoval(): void {
    const movieId = this.data.movie.id;

    this.moviesService.remove(movieId).subscribe(() => {
      this.dialogRef.close(true);
    });
  }

}
