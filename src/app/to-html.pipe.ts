import { Pipe, PipeTransform } from '@angular/core';
import { ContentService } from './content.service'
import { documentToHtmlString } from '@contentful/rich-text-html-renderer'

@Pipe({
  name: 'toHtml',
})
export class ToHtmlPipe implements PipeTransform {
  constructor(private contentful: ContentService) {}
  transform(value: any): any {
    return documentToHtmlString(value);
  }

}
