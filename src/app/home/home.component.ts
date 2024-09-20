import { Component, OnInit } from '@angular/core';
import { ContentService } from '../content.service';
import { TypeTextBoxFields } from '../content-types';
import { documentToHtmlString } from '@contentful/rich-text-html-renderer'
import { Entry } from 'contentful';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {
  textBox = ``;
  constructor(public contentService: ContentService) {}
  ngOnInit(): void {
    this.contentService.getTextBoxes().subscribe(textBoxes => {
      textBoxes.items.forEach((element) => {
        this.textBox = documentToHtmlString(element.fields.body);
      })
    })
  } 
}
