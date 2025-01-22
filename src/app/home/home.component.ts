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

}
