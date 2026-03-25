import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ComponentFive } from './component-five';

describe('ComponentFive', () => {
  let component: ComponentFive;
  let fixture: ComponentFixture<ComponentFive>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ComponentFive]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ComponentFive);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
