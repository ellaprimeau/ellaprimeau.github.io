import { Component, OnInit } from '@angular/core';
import { ContentService } from '../content.service';
import { TypeMapPostSkeleton } from '../content-types';
import { documentToHtmlString } from '@contentful/rich-text-html-renderer'
import { Entry } from 'contentful';
import { RequestService } from '../request.service';
import { Routes } from '@angular/router';

@Component({
  selector: 'app-maps',
  templateUrl: './maps.component.html',
  styleUrls: ['./maps.component.scss']
})
export class MapsComponent {
  textBox = ``;
  text = '';
  array = [];
  constructor(public contentService: ContentService, public requestService: RequestService) {}

  ngOnInit(): void {
    this.contentService.getTextBoxes().subscribe(textBoxes => {
      textBoxes.items.forEach((element) => {
        console.log(element.fields);
        var fields = element.fields;
        this.array.push(element.fields);
      })
    })
  }
}
