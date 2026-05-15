import { ApplicationConfig, provideBrowserGlobalErrorListeners } from '@angular/core';
import { provideRouter } from '@angular/router';
import { authInterceptor } from './interceptors/auth-interceptor';
import { provideHttpClient, withInterceptors } from '@angular/common/http';

import { routes } from './app.routes';

export const appConfig: ApplicationConfig = {
  providers: [
    provideBrowserGlobalErrorListeners(),
    provideRouter(routes),
    provideHttpClient(withInterceptors([authInterceptor])) // Регистрируем HTTP-клиент и добавляем к нему наш authInterceptor, который будет автоматически добавлять токен доступа в заголовки всех исходящих HTTP-запросов, если токен присутствует в localStorage. Это позволяет обеспечить аутентификацию при взаимодействии с защищенными эндпойнтами на сервере.
  ]
};
