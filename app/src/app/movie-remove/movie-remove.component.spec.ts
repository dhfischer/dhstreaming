import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MovieRemoveComponent } from './movie-remove.component';

describe('MovieRemoveComponent', () => {
  let component: MovieRemoveComponent;
  let fixture: ComponentFixture<MovieRemoveComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MovieRemoveComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MovieRemoveComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
