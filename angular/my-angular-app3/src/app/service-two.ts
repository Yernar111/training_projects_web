import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

export interface Data2 {
  id: number;
  title: string;
}

export const datas2: Data2[] = [
  {
    id: 1,
    title: "Tom"
  },
  {
    id: 2,
    title: "Tim"
  }
]

@Injectable({
  providedIn: 'root',
})
export class ServiceTwo {
  constructor(private http: HttpClient) {} // Внедрение зависимости HttpClient в конструктор сервиса. Это позволяет использовать HttpClient для выполнения HTTP-запросов внутри этого сервиса.

  // Observable - это объект, который может эмитировать данные асинхронно. Он позволяет подписаться на него и получать данные, когда они будут доступны. Это особенно полезно для работы с HTTP-запросами, так как они выполняются асинхронно и могут занять некоторое время для получения ответа от сервера.

  get2(): Observable<Data2[]> { // Метод возвращает Observable, который будет эмитировать массив объектов типа Data2. Это позволяет компоненту, который вызывает этот метод, подписаться на него и получать данные асинхронно, когда они будут доступны.
    return this.http.get<Data2[]>('https://jsonplaceholder.typicode.com/todos/2'); // Выполнение HTTP GET-запроса к указанному URL(возвращая Observable) и ожидание получения данных в формате массива объектов типа Data2. HttpClient автоматически преобразует полученные данные в нужный формат, если указано типизацию <Data2[]>.
  }

  post2(v1: Data2): Observable<Data2> { // Метод post1 принимает объект типа Data2 в качестве аргумента и возвращает Observable, который будет эмитировать объект типа Data2. Это позволяет компоненту, который вызывает этот метод, подписаться на него и получать данные асинхронно, когда они будут доступны после выполнения HTTP POST-запроса.
    return this.http.post<Data2>('https://jsonplaceholder.typicode.com/users', v1);
  }

  
} //
