// This file defines an HTTP interceptor that adds an Authorization header with a Bearer token to outgoing HTTP requests if a token is present in localStorage. This allows the application to authenticate requests to protected endpoints on the server using the token obtained during user authentication.
import { HttpInterceptorFn } from '@angular/common/http';

export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const token = localStorage.getItem('access'); // Получаем токен доступа из localStorage. Когда пользователь успешно аутентифицируется, мы сохраняем токен доступа в localStorage. Теперь при каждом HTTP-запросе к защищенным эндпойнтам мы будем брать этот токен и отправлять его в заголовке Authorization, чтобы сервер понимал, что запрос исходит от аутентифицированного пользователя.
  if (token) {
    // const headers = req.headers.set('Authorization', `Bearer ${token}`); // Формируем заголовок Authorization с токеном доступа. Обычно токен доступа отправляется в виде Bearer-токена, то есть в формате "Bearer <токен>". Это стандартный способ передачи токена доступа в HTTP-заголовке.
    // req = req.clone({ headers });
    const cloneReq = req.clone({ // Клонируем исходный запрос и добавляем к нему заголовок Authorization с токеном доступа. В Angular HttpClient запросы являются неизменяемыми, поэтому для изменения запроса нужно создать его копию с помощью метода clone() и указать новые заголовки.
      setHeaders: {
        Authorization: `Bearer ${token}`
      }
    });
    return next(cloneReq);
  }
  return next(req);
};
