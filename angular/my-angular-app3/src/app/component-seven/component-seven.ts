import { Component, input, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ServiceThree, Data3 } from '../service-three';
import { Observable } from 'rxjs';

@Component({ 
  selector: 'app-component-seven',
  standalone: true,
  imports: [FormsModule], // Импортирование FormsModule для использования функциональности форм в шаблоне компонента. Это позволяет использовать директивы и функциональность, связанные с формами, такие как ngModel, для двусторонней привязки данных между компонентом и шаблоном.
  templateUrl: './component-seven.html',
  styleUrl: './component-seven.css',
})
export class ComponentSeven implements OnInit {
  constructor(private serviceThree: ServiceThree) {}

  input1: number = 0;
  input2: string = '';

  data4: Data3 = { id: 0, title: '' }; // Переменной обязательно нужно присвоить начальное значение, чтобы избежать ошибки "Variable 'data3' is used before being assigned". В данном случае, мы инициализируем data3 объектом с id 1 и title 'Initial Title'. Это гарантирует, что переменная data3 будет иметь значение до того, как она будет использована в коде компонента.
  data4_1$!: Observable<Data3[]>;
  // data4!: Data3; // Еще один способ решения проблемы "Variable 'data3' is used before being assigned" - это использовать оператор "!" (non-null assertion operator) при объявлении переменной. Это говорит TypeScript, что мы гарантируем, что переменная data3 будет инициализирована до того, как она будет использована, и позволяет избежать ошибки компиляции. Однако, при использовании этого подхода, важно убедиться, что переменная действительно будет инициализирована перед использованием, иначе это может привести к ошибкам во время выполнения.
  // data4: Data3 | null = null; // Объявление переменной data3 типа Data3 или null. Это позволяет переменной data3 быть null, что может быть полезно в случаях, когда данные еще не загружены или не доступны. При использовании этой переменной в коде компонента, необходимо учитывать возможность того, что она может быть null и обрабатывать этот случай соответствующим образом.

  ngOnInit(): void {
    this.data4_1$ = this.serviceThree.get3(); // Инициализация свойства data4_1$ путем вызова метода get3 сервиса ServiceThree, который возвращает Observable с данными типа Data3[]. Это позволяет использовать async pipe в шаблоне компонента для автоматической подписки на Observable и получения его данных через шаблон. Async pipe будет автоматически подписываться на Observable в шаблоне при каждом новом значении, получаемом от Observable, и также будет автоматически отписываться от Observable при уничтожении компонента, что помогает предотвратить утечки памяти.
    this.serviceThree.get3().subscribe(data => {
      this.input1 = data[0].id;
    });
  }
  // Метод для обработки отправки формы. Когда форма будет отправлена, этот метод будет вызван, и он может использовать значения input1 и input2 для выполнения определенных действий, таких как отправка данных на сервер или выполнение логики внутри компонента.
  onSubmit() {
    console.log('Input 1:', this.input1);
    console.log('Input 2:', this.input2);
    //// Здесь можно добавить дополнительную логику для обработки данных из формы, например, отправку их на сервер или выполнение других действий внутри компонента.

    this.data4.id = Number(this.input1);
    this.data4.title = this.input2;

    console.log('Data4:', this.data4);
    
    this.serviceThree.post3(this.data4).subscribe(response => { 
      console.log('Response:', response);
    });


  }

} //
