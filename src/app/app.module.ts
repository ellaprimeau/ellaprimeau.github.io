import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { BrowserModule } from '@angular/platform-browser';
import { Routes, RouterModule, provideRouter } from '@angular/router';
import routeConfig from './routes';
import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { MapsComponent } from './maps/maps.component';
import { HomeComponent } from './home/home.component';
import { MapBarComponent } from './maps/map-bar/map-bar.component';
import { RouteInfoComponent } from './maps/route-info/route-info.component';
import { provideHttpClient } from '@angular/common/http';
import { ToHtmlPipe } from './to-html.pipe';
import { DatePipePipe } from './date-pipe.pipe';
import { PdfViewerModule } from 'ng2-pdf-viewer';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    MapsComponent,
    HomeComponent,
    MapBarComponent,
    RouteInfoComponent,
    ToHtmlPipe,
    DatePipePipe
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(routeConfig),
    PdfViewerModule
  ],
  providers: [
    provideRouter(routeConfig),
    provideHttpClient()
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
  
}
