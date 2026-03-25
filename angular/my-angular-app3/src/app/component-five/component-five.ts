import { Component, OnInit } from '@angular/core';
import { Data3, ServiceThree } from '../service-three';
import { Observable } from 'rxjs';
import { RouterLink } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-component-five',
  imports: [CommonModule, RouterLink],
  templateUrl: './component-five.html',
  styleUrl: './component-five.css',
})
export class ComponentFive implements OnInit{
  // $ at the end of a variable name is a common convention in Angular to indicate that the variable is an Observable. This helps developers quickly identify that the variable is a stream of data that can be subscribed to, rather than a regular value.
  data3$!: Observable<Data3[]>; // Объявление свойства data3$ типа Observable, который будет использоваться для хранения потока данных типа Data3[].
  constructor(private serviceThree: ServiceThree) {}

  ngOnInit(): void {
    this.data3$ = this.serviceThree.get3(); // Инициализация свойства data3$ путем вызова метода get2 сервиса ServiceThree, который возвращает Observable с данными типа Data3[].
    // В отличие от обычного присваивания, здесь мы не подписываемся на Observable с помощью subscribe, а просто присваиваем его свойству data3$. Это позволяет использовать async pipe в шаблоне компонента для автоматической подписки на Observable и получения его данных через шаблон. Async pipe будет автоматически подписываться на Observable в шаблоне при каждом новом значении, получаемом от Observable, и также будет автоматически отписываться от Observable при уничтожении компонента, что помогает предотвратить утечки памяти.
  }

}
