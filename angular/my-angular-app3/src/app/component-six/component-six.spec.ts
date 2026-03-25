import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ComponentSix } from './component-six';

describe('ComponentSix', () => {
  let component: ComponentSix;
  let fixture: ComponentFixture<ComponentSix>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ComponentSix]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ComponentSix);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
