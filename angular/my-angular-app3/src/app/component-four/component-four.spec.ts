import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ComponentFour } from './component-four';

describe('ComponentFour', () => {
  let component: ComponentFour;
  let fixture: ComponentFixture<ComponentFour>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ComponentFour]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ComponentFour);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
