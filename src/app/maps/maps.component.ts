import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ContentService } from '../content.service';
import { TypeMapPostSkeleton } from '../content-types';
import { documentToHtmlString } from '@contentful/rich-text-html-renderer'
import { Entry } from 'contentful';
import { RequestService } from '../request.service';
import { Routes } from '@angular/router';
import { ToHtmlPipe } from '../to-html.pipe';
import { DatePipePipe } from '../date-pipe.pipe';
import { PdfViewerModule } from 'ng2-pdf-viewer';

@Component({
  selector: 'app-maps',
  templateUrl: './maps.component.html',
  styleUrls: ['./maps.component.scss'],
})
export class MapsComponent {
  textBox = ``;
  text = '';
  array = [];
  constructor(public contentService: ContentService, public requestService: RequestService) {}

  ngOnInit(): void {
    this.contentService.getTextBoxes().subscribe(textBoxes => {
      textBoxes.items.forEach((element) => {
        console.log(element);
        this.array.push(element);
      })
      console.log(this.array);
    })
  }
}
