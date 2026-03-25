import { TestBed } from '@angular/core/testing';

import { ServiceTwo } from './service-two';

describe('ServiceTwo', () => {
  let service: ServiceTwo;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ServiceTwo);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
