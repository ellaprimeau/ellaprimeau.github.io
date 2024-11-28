import { Component, OnInit } from '@angular/core';
import { ContentService } from '../content.service';
import { TypeTextBoxFields } from '../content-types';
import { documentToHtmlString } from '@contentful/rich-text-html-renderer'
import { Entry } from 'contentful';
import { RequestService } from '../request.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {
  textBox = ``;
  text = '';
  constructor(public contentService: ContentService, public requestService: RequestService) {}

  ngOnInit(): void {
    this.contentService.getTextBoxes().subscribe(textBoxes => {
      textBoxes.items.forEach((element) => {
        this.textBox = documentToHtmlString(element.fields.body);
      })
    })
    this.requestService.get('/api/getShapes').subscribe(data => {
      this.text = JSON.stringify(data);
      console.log(data);
    })
  }
}
