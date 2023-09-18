import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { MovieListComponent } from './movie-list/movie-list.component';
import { AuthGuardService } from './auth-guard.service';
import { MovieDetailsComponent } from './movie-details/movie-details.component';
import { MovieCreateComponent } from './movie-create/movie-create.component';
import { MovieEditComponent } from './movie-edit/movie-edit.component';


export const DEFAULT_ROUTE = '/movie-list';

const routes: Routes = [
  {path: '', redirectTo: DEFAULT_ROUTE, pathMatch: 'full'},
  {path: 'login', component: LoginComponent},
  {path: 'movie-list', component: MovieListComponent, canActivate: [AuthGuardService]},
  {path: 'movie-create', component: MovieCreateComponent},
  {path: 'movie-details/:id', component: MovieDetailsComponent, canActivate: [AuthGuardService]},
  {path: 'movie-edit/:id', component: MovieEditComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
