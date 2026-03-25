import { Component } from '@angular/core';
import { ComponentOne } from './component-one/component-one';
import { CommonModule } from '@angular/common';
import { ComponentTwo } from './component-two/component-two';
import { ComponentThree } from './component-three/component-three';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, ComponentOne, ComponentTwo, ComponentThree], // Импортирование класса дочернего компонента. Теперь App родительский компонент для ComponentOne, ComponentTwo и ComponentThree
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App { // Класс родительского компонента. Нужно для того чтобы описать логику работы родительского компонента, а также для передачи данных в дочерний компонент и получения данных от него
  a: string = "abcd";
  b: string = "e";
  n: number = 1;
  check1_1(i: string){ // 4) Функция реагирующая на событие
    this.b=i;
    console.log("efgh!");
  }

  g: string[] = ["a","b","c"];

  check3(){
      if (this.g?.length){
        return 2;
      }
      else{
        return 3;
      }
  }
}
