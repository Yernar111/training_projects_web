import { Component, signal } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import { ComponentFour } from './component-four/component-four';
import { ComponentFive } from './component-five/component-five';
import { ComponentSeven } from './component-seven/component-seven';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, ComponentFour, RouterLink, ComponentSeven], // Импортирование RouterLink для использования директивы routerLink в шаблоне компонента. Это позволяет создавать ссылки для навигации между различными маршрутами в приложении.
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('my-angular-app3');
}
