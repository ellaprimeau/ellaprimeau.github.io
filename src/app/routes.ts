import { Routes } from '@angular/router';
import { MapsComponent } from './maps/maps.component';
import { RouteInfoComponent } from './maps/route-info/route-info.component';
import { HomeComponent } from './home/home.component';

const routeConfig: Routes = [
  {path: 'maps', component: MapsComponent},
  {path: 'maps/routeInfo', component: RouteInfoComponent},
  {path: 'home', component: HomeComponent},
  {path: '', redirectTo: '/home', pathMatch: 'full'},
];

export default routeConfig;