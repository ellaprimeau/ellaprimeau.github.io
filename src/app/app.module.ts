import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { Routes, RouterModule, provideRouter } from '@angular/router';
import routeConfig from './routes';
import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { MapsComponent } from './maps/maps.component';
import { HomeComponent } from './home/home.component';

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    MapsComponent,
    HomeComponent
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
