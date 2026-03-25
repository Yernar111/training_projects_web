import { CommonModule } from '@angular/common';
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-component-two',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './component-two.html',
  styleUrl: './component-two.css',
})
export class ComponentTwo {
  @Input() f!: string;
}
