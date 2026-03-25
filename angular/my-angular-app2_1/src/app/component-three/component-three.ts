import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';

@Component({
  selector: 'app-component-three',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './component-three.html',
  styleUrl: './component-three.css',
})
export class ComponentThree {
  k1: string = "yes";
  k2: string = "no";
  isK: boolean = false;
  check2(): string{ // Если функция возвращает что-то, то у нее должен быть тип данных
    if (this.isK){
      console.log("yes!!");
    }
    else{
      console.log("no!!");
    }
    return "value";
  }
}
