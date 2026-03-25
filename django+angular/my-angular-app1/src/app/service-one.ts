import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

export interface ServiceOneInterface {
  id: number,
  name: string,
  password: number
}

@Injectable({
  providedIn: 'root',
})
export class ServiceOne {
  constructor (private http: HttpClient) {}

  create_user1(v1: ServiceOneInterface): Observable<ServiceOneInterface>{ // Плохой вариант
    return this.http.get<ServiceOneInterface>(`http://127.0.0.1:8000/create_user/${v1.name}/${v1.password}`);
  }

  create_user2(v1: ServiceOneInterface): Observable<ServiceOneInterface>{ // Более надежный вариант
    return this.http.post<ServiceOneInterface>(`http://127.0.0.1:8000/create_user/`, v1);
  }

  get_users1(): Observable<ServiceOneInterface[]> {
    return this.http.get<ServiceOneInterface[]>(`http://127.0.0.1:8000/get_users/`);
  }

  get_user1(name: string): Observable<ServiceOneInterface> {
    return this.http.get<ServiceOneInterface>(`http://127.0.0.1:8000/get_user/${name}/`);
  }
}
