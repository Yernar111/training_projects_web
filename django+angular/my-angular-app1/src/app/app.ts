import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';

import { ComponentOne } from './component-one/component-one';

@Component({
  selector: 'app-root',
  imports: [ComponentOne],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('my-angular-app1');
}
