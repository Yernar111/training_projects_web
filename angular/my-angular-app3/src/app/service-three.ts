import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

export interface Data3 {
  id: number;
  title: string;
}

@Injectable({
  providedIn: 'root',
})
export class ServiceThree {
  constructor(private http: HttpClient) {}

  get3(): Observable<Data3[]> {
    return this.http.get<Data3[]>('https://jsonplaceholder.typicode.com/todos');
  }

  post3(v1: Data3): Observable<Data3> {
    return this.http.post<Data3>('https://jsonplaceholder.typicode.com/todos', v1); // Так как данные в jsonplaceholder не сохраняются, то при каждом POST-запросе будет возвращаться один и тот же объект с id 201. Это связано с тем, что jsonplaceholder является фейковым API для тестирования и не сохраняет данные между запросами. Поэтому, независимо от того, какие данные вы отправляете в POST-запросе, вы всегда будете получать один и тот же ответ с id 201.
  }

  getById3(id: number): Observable<Data3> {
    return this.http.get<Data3>(`https://jsonplaceholder.typicode.com/todos/${id}`); // Метод getById3 принимает число id в качестве аргумента и возвращает Observable, который будет эмитировать объект типа Data3. Это позволяет компоненту, который вызывает этот метод, подписаться на него и получать данные асинхронно, когда они будут доступны после выполнения HTTP GET-запроса к указанному URL с добавлением id в конце. Этот запрос будет возвращать данные о задаче (todo) с указанным id.
  }

}
