import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { Routes, RouterModule, provideRouter } from '@angular/router';
import routeConfig from './routes';
import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { MapsComponent } from './maps/maps.component';
import { HomeComponent } from './home/home.component';
import { MapBarComponent } from './maps/map-bar/map-bar.component';
import { RouteInfoComponent } from './maps/route-info/route-info.component';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    MapsComponent,
    HomeComponent,
    MapBarComponent,
    RouteInfoComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(routeConfig)
  ],
  providers: [
    provideRouter(routeConfig)
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
  
}
