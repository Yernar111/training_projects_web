import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ComponentSeven } from './component-seven';

describe('ComponentSeven', () => {
  let component: ComponentSeven;
  let fixture: ComponentFixture<ComponentSeven>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ComponentSeven]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ComponentSeven);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
