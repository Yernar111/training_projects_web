import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ServiceOne } from '../service-one'; // Импортирование сервиса ServiceOne для использования его методов и данных внутри этого компонента. Это позволяет компоненту взаимодействовать с логикой и данными, предоставляемыми ServiceOne, что может быть полезно для выполнения различных задач и отображения информации в шаблоне компонента.
import { Data2, ServiceTwo } from '../service-two';

@Component({
  selector: 'app-component-four',
  standalone: true,
  imports: [CommonModule], // Импортирование CommonModule для использования общих директив и функциональности Angular в шаблоне компонента.
  templateUrl: './component-four.html',
  styleUrl: './component-four.css',
})
export class ComponentFour implements OnInit { // Реализация интерфейса OnInit для использования метода ngOnInit, который вызывается при инициализации компонента.
  data2: Data2[] = [
    {id: 3, title: "Ben"},
    {id: 4, title: "Jim"}
  ];

  // constructor(private serviceOne: ServiceOne) {} // Внедрение сервиса ServiceOne в конструктор компонента. Это позволяет использовать методы и данные из ServiceOne внутри этого компонента.
  // Если нужно использовать оба сервиса, то их нужно указать в одном конструкторе
  constructor(private serviceOne: ServiceOne, private serviceTwo: ServiceTwo) {} // Внедрение обоих сервисов в конструктор компонента. Это позволяет использовать методы и данные из обоих сервисов внутри этого компонента.

  ngOnInit() { //
    const m = this.serviceOne.check3();
    console.log(m);

    // console.log(this.serviceTwo.getHttpData1()); // Выведет Observable(то есть в консоли ничего не будет выведено если это http), а не данные, так как getHttpData1 возвращает Observable. Чтобы получить данные, нужно подписаться на Observable с помощью subscribe.

    // this.serviceTwo.getHttpData1().subscribe(data => { // Подписка на Observable, возвращаемый методом getHttpData1. Когда данные будут получены, функция внутри subscribe будет вызвана с этими данными.
    //   console.log(data);
    // });

    this.serviceTwo.get2().subscribe(data => { // Подписка на Observable, возвращаемый методом get1. Когда данные будут получены, функция внутри subscribe будет вызвана с этими данными. data - это данные, которые были получены от сервера в ответ на HTTP GET-запрос, выполненный внутри метода get1 сервиса ServiceTwo. Эти данные могут быть массивом объектов типа Data2, который был определен в сервисе ServiceTwo и возвращается в ответ на запрос.
      this.data2 = data; // Сохранение полученных данных в свойстве data2 для дальнейшего использования в шаблоне компонента.
      console.log(this.data2); // Вывод полученных данных в консоль для проверки.
    });

    this.serviceTwo.post2(this.data2[1]).subscribe(response => { // Вызов метода post1 для отправки данных на сервер. Подписка на Observable, возвращаемый методом post1, для получения ответа от сервера после выполнения HTTP POST-запроса. Ответом сервера будет объект типа Data2, который был отправлен на сервер, возможно с добавлением дополнительных данных, таких как id, если сервер их генерирует.
      console.log(response); // Вывод ответа от сервера в консоль для проверки.
    });

  }
}