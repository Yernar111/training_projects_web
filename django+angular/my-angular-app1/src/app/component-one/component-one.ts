import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ServiceOne, ServiceOneInterface } from '../service-one';
import { Observable } from 'rxjs';
import { CommonModule } from '@angular/common';



@Component({
  selector: 'app-component-one',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './component-one.html',
  styleUrl: './component-one.css',
})
export class ComponentOne {
  constructor (private serviceOne: ServiceOne) {}

  input1: string = '';
  input2: number | undefined;
  // input2: number = 0;

  data1: ServiceOneInterface = {id: 0, name: '', password: 0};

  onSubmit1(){
    this.data1.name = this.input1;
    this.data1.password = Number(this.input2);
    this.serviceOne.create_user2(this.data1).subscribe(data => console.log(data));
  }


  data1_1$!: Observable<ServiceOneInterface>;
  input3: string = '';

  onSubmit2(){
    this.data1_1$ = this.serviceOne.get_user1(this.input3);
    this.data1_1$.subscribe(data => console.log(data));
  //   this.serviceOne.get_user1(this.input3).subscribe(data => {
  //     // this.data1 = data;

  //     console.log(data);

  //   });
  }

  data1_2$!: Observable<ServiceOneInterface[]>;
  getAllUsers(){
    this.data1_2$ = this.serviceOne.get_users1();
    this.data1_2$.subscribe(data => console.log(data));
  }


}
