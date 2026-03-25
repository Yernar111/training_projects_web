import { TestBed } from '@angular/core/testing';

import { ServiceOne } from './service-one';

describe('ServiceOne', () => {
  let service: ServiceOne;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ServiceOne);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
