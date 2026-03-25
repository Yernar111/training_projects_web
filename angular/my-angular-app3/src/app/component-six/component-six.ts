import { Component } from '@angular/core';
import { Observable } from 'rxjs';
import { Data3, ServiceThree } from '../service-three';
import { ActivatedRoute } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-component-six',
  imports: [CommonModule],
  templateUrl: './component-six.html',
  styleUrl: './component-six.css',
})
export class ComponentSix {
  // data3_1$: Observable<Data3> | undefined; // Объявление свойства data3_1$ типа Observable, который будет использоваться для хранения потока данных типа any. Это может быть использовано для получения данных из сервиса и отображения их в шаблоне компонента.
  data3_1$!: Observable<Data3>;
  

  constructor(private serviceThree: ServiceThree, private route: ActivatedRoute) {} // Внедрение зависимостей(DI): сервис ServiceThree для получения данных и ActivatedRoute для доступа к параметрам маршрута внутри компонента.

  ngOnInit(): void {
    const id = this.route.snapshot.paramMap.get('id'); // Получение параметра id из маршрута. Это позволяет использовать этот id для получения конкретных данных из сервиса.
    this.data3_1$ = this.serviceThree.getById3(Number(id)); // Инициализация свойства data3_1$ путем вызова метода getById2 сервиса ServiceThree с полученным id. Это позволяет получить данные, связанные с этим id, и использовать их в шаблоне компонента.
  }

}
