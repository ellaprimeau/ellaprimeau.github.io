import { Component, AfterViewInit, OnInit } from '@angular/core';
import { RequestService } from '../../request.service';
import {KeyValue} from '@angular/common'
import * as L from 'leaflet';
import 'leaflet-arrowheads';
import * as geojson from 'geojson';

@Component({
  selector: 'app-route-info',
  templateUrl: './route-info.component.html',
  styleUrls: ['./route-info.component.scss']
})
export class RouteInfoComponent implements AfterViewInit, OnInit {
  constructor(public requestService: RequestService) {}

  public routes: any;
  public services: any;
  private coords : any;
  public map : any;
  public trips: any;
  public tripGroups: any[] = [[],[],[]];
  public shapes: any[] = [];
  public mapLayer = L.geoJSON(null);
  public disabled = false;
  public colorIndex: number = 0;
  private geojsonFeature : any;
  private mapApiKey = import.meta.env.NG_APP_MAP_API_KEY;

  public tiles = L.tileLayer('https://api.maptiler.com/maps/basic-v2/{z}/{x}/{y}@2x.png?key='+this.mapApiKey, {
    tileSize: 512,
    zoomOffset: -1,
    maxZoom: 18,
    minZoom: 3,
    attribution: '<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>'
  });

  public async populateShapes(route_id: any): Promise<void> {
    const start = new Date().getTime();
    this.removeShapes();
    [this.shapes, this.trips] = await Promise.all([
      this.requestService.get('/api/shapes/'+route_id).toPromise(),
      this.requestService.get('/api/stop_times/byRoute/'+route_id).toPromise()]);

    let elapsed = new Date().getTime() - start;
    console.log(elapsed)
  }

  public removeShapes(): void {
    this.map.remove();
    this.colorIndex = 0;
    this.initMap();
  }

  public async plotShape(shape: string, color: string): Promise<void> {
    // this.mapLayer.remove();
    const start = new Date().getTime();
    this.disabled = true;
    [this.trips, this.coords] = await Promise.all([
      this.requestService.get('/api/stop_times/byShape/'+shape).toPromise(),
      this.requestService.get('/api/shape/'+shape).toPromise()]);

    // this.tripGroups = [[],[],[],[],[],[],[]];

    // for(let i = 0; i < this.trips.length; i++) {
    //   if(this.trips[i][0]=="Weekday"){
    //     this.tripGroups[0].push(this.trips[i]);
    //   } else if(this.trips[i][0]=="Saturday") {
    //     this.tripGroups[1].push(this.trips[i]);
    //   } else {
    //     this.tripGroups[2].push(this.trips[i]);        
    //   }
    // }

    this.geojsonFeature = {
        "type": "Feature",
        "geometry": {
            "type": "LineString",
            "coordinates": this.coords
        },
    };

    // @ts-ignore
    this.mapLayer = L.geoJSON(this.geojsonFeature, { arrowheads:{
      size: '14px',
      frequency: '300px',
      yawn: 40,
      fill: true,
      offsets: {start:'100m',end:'100m'}
    }});

    this.mapLayer.addTo(this.map);
    this.mapLayer.setStyle(()=>({ color: color, opacity: 0.8, weight: 5 }));
    this.colorIndex++; 
    this.map.fitBounds(this.mapLayer.getBounds());
    this.disabled=false;
    let elapsed = new Date().getTime() - start;
    console.log(elapsed)
  }

  public initMap(): void {
    this.map = L.map('map', {
      center: [45.424721, -75.695000],
      zoom: 12,

    });

    this.tiles.addTo(this.map);
  }

  async ngOnInit(): Promise<void> {
    [this.routes, this.services] = await Promise.all([
      this.requestService.get('/api/getRoutes').toPromise(),
      this.requestService.get('/api/getServices').toPromise()
    ]);

    this.initMap();
  }

  ngAfterViewInit(): void {

  }
}
