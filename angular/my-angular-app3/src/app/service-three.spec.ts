import { TestBed } from '@angular/core/testing';

import { ServiceThree } from './service-three';

describe('ServiceThree', () => {
  let service: ServiceThree;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ServiceThree);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
