import { Injectable } from '@angular/core';
import { createClient } from 'contentful';
import { from } from 'rxjs';
// import { environment } from '../environments';
import { TypeTextBoxFields } from './content-types';
import { TypeTextBoxSkeleton } from './content-types';

@Injectable({
  providedIn: 'root'
})
export class ContentService {

  client = createClient({
    // space: environment.contentful.spaceId,
    space: process.env.CONTENTFUL_SPACE_ID!,
    // accessToken: environment.contentful.accessToken,
    accessToken: process.env.CONTENTFUL_ACCESS_TOKEN!,
    // environment: environment.contentful.environment
  });

  constructor() { }

  getTextBoxes(query?: object){
    return from(
      this.client.getEntries<TypeTextBoxSkeleton>()
    );
  }
}
