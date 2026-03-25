import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ComponentTwo } from './component-two';

describe('ComponentTwo', () => {
  let component: ComponentTwo;
  let fixture: ComponentFixture<ComponentTwo>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ComponentTwo]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ComponentTwo);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
