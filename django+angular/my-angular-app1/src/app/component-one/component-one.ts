import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ServiceOne, ServiceOneInterface } from '../service-one';
import { Observable } from 'rxjs';
import { CommonModule } from '@angular/common';

import { AuthService } from '../auth-service';



@Component({
  selector: 'app-component-one',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './component-one.html',
  styleUrl: './component-one.css',
})
export class ComponentOne {
  constructor (private serviceOne: ServiceOne, private authService: AuthService) {}

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
    this.data1_1$.subscribe(data =>console.log(data));
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


  username: string = '';
  password: string = '';
  login(){
    this.authService.login(this.username, this.password).subscribe(response => {
      localStorage.setItem('access', response.access); // Сохраняем токен доступа в localStorage. Теперь при каждом HTTP-запросе к защищенным эндпойнтам мы будем брать этот токен и отправлять его в заголовке Authorization, чтобы сервер понимал, что запрос исходит от аутентифицированного пользователя.
      localStorage.setItem('refresh', response.refresh); // Сохраняем токен обновления в localStorage. Токен обновления нужен для получения нового токена доступа, когда старый истечет. Обычно токен доступа имеет короткий срок действия (например, 5 минут), а токен обновления - более длительный (например, 7 дней). Когда токен доступа истекает, клиент может отправить запрос на специальный эндпойнт для обновления токена, предоставив токен обновления. Если токен обновления действителен, сервер выдаст новый токен доступа.

      console.log("Logged in");
    });
  }

  data1_3$!: Observable<ServiceOneInterface[]>;
  getAllUsersProtected(){
    this.data1_3$ = this.serviceOne.get_users2();
    this.data1_3$.subscribe(data => console.log(data));
    // this.serviceOne.get_users2().subscribe(data => console.log(data));
  }


}
