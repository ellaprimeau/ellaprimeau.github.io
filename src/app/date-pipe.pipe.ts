import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'datePipe',
})
export class DatePipePipe implements PipeTransform {

  transform(value: any): any {
    return new Date(value).toDateString();
  }

}
