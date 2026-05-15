import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  constructor (private http: HttpClient) {}

  login(username1: string, password1: string): Observable<any>{
    return this.http.post<any>(`http://127.0.0.1:8000/blog2/api/token/`,
      {
        username: username1,
        password: password1
      }
    );
  }
  logout() {
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
  }

}
