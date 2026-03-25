// Service is a class that contains some logic/data and can be used in other classes
import { Injectable } from '@angular/core'; // Means this class can be injected into other classes

export interface Data1 { // Interface is a structure that defines the shape of an object. export means it can be imported in other files
  id: number;
  name: string;
}

export const datas1: Data1[] = [
  {
    id: 1,
    name: "Tom"
  },
  {
    id: 2,
    name: "Tim"
  }
]

@Injectable({
  providedIn: 'root', // Service is common for the entire app
})
export class ServiceOne {
  lll: Data1[] = datas1;
  check3(){
    return this.lll;
  }
  
} //
