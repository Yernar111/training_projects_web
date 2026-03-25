import { bootstrapApplication } from '@angular/platform-browser';
// import { appConfig } from './app/app.config';
import { App } from './app/app';
import { provideHttpClient } from '@angular/common/http';
import { provideRouter } from '@angular/router';
import { routes } from './app/app.routes';

bootstrapApplication(App, {
  providers: [
    provideHttpClient(), // This is a provider for the HttpClient service, which allows you to make HTTP requests in your Angular application. By including this provider, you can inject the HttpClient service into your components and services to perform HTTP operations such as GET, POST, PUT, DELETE, etc. It is essential for applications that need to communicate with backend APIs or fetch data from external sources.
    provideRouter(routes) // This is a provider for the Angular Router, which allows you to define and manage navigation within your application. By including this provider, you can set up routing in your Angular application, enabling you to navigate between different components and views based on the defined routes. The provideRouter function is used to configure the router at the application's root level, and it takes an array of route definitions as an argument.
    // Different from importProvidersFrom(RouterModule.forRoot(routes)), provideRouter is a more direct way to set up routing in Angular applications. It allows you to define your routes directly in the providers array without needing to import the entire RouterModule. This can lead to a more streamlined and efficient setup for routing in your Angular application, especially if you only need to configure a few routes and want to avoid importing unnecessary modules.
  ]
}).catch((err) => console.error(err));
