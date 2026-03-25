import { Routes } from '@angular/router'; // Routes is an array of route objects that define the mapping between URL paths and components in an Angular application. Each route object typically contains a path property (the URL path) and a component property (the component to display when the path is accessed). This allows for navigation within the application based on the URL.
import { ComponentFive } from './component-five/component-five'; 
import { ComponentSix } from './component-six/component-six';
import { ComponentFour } from './component-four/component-four';

export const routes: Routes = [
    { path: '', component: ComponentFour }, // Маршрут для компонента component-five. Когда пользователь переходит по этому маршруту, будет отображаться компонент ComponentFive. Этот маршрут является корневым маршрутом (потому что path: ''), что означает, что он будет отображаться при загрузке приложения без указания дополнительного пути в URL.
    { path: 'component-five', component: ComponentFive },
    { path: 'todos/:id', component: ComponentSix } // Маршрут для компонента component-six с параметром id. Когда пользователь переходит по этому маршруту, будет отображаться компонент ComponentSix, и значение параметра id будет доступно внутри этого компонента для получения конкретных данных, связанных с этим id.
];
