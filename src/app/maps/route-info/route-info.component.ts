import { Component, AfterViewInit, OnInit } from '@angular/core';
import { RequestService } from '../../request.service';
import * as L from 'leaflet';
import * as geojson from 'geojson';

@Component({
  selector: 'app-route-info',
  templateUrl: './route-info.component.html',
  styleUrls: ['./route-info.component.scss']
})
export class RouteInfoComponent implements AfterViewInit, OnInit {
  constructor(public requestService: RequestService) {}

  public shapes: any;
  private coords : any;
  public map : any;
  public trips: any;
  public tripGroups: any[] = [[],[],[]];
  public mapLayer = L.geoJSON(null);
  public disabled = false;
  private geojsonFeature : any;
  private mapApiKey = import.meta.env.NG_APP_MAP_API_KEY;

  public tiles = L.tileLayer('https://api.maptiler.com/maps/basic-v2/{z}/{x}/{y}@2x.png?key='+this.mapApiKey, {
    tileSize: 512,
    zoomOffset: -1,
    maxZoom: 18,
    minZoom: 3,
    attribution: '<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>'
  });

  private async populateSelectList(): Promise<void> {
    this.shapes = await this.requestService.get('/api/shapeNames').toPromise();
  }

  public async plotShape(shape: string): Promise<void> {
    this.disabled = true
    // this.trip = "test";
    this.mapLayer.remove();
    this.trips = await this.requestService.get('/api/trip/'+shape).toPromise();
    this.tripGroups = [[],[],[]];

    for(let i = 0; i < this.trips.length; i++) {
      if(this.trips[i][0]=="Weekday"){
        this.tripGroups[0].push(this.trips[i]);
      } else if(this.trips[i][0]=="Saturday") {
        this.tripGroups[1].push(this.trips[i]);
      } else {
        this.tripGroups[2].push(this.trips[i]);        
      }
    }
    this.coords = await this.requestService.get('/api/shape/'+shape).toPromise();

    this.geojsonFeature = ({
        "type": "Feature",
        "geometry": {
            "type": "LineString",
            "coordinates": this.coords
        }
    });

    this.mapLayer = L.geoJSON(this.geojsonFeature);
    this.mapLayer.addTo(this.map);
    this.map.fitBounds(this.mapLayer.getBounds());
    this.disabled=false;
  }

  public initMap(): void {
    this.map = L.map('map', {
      center: [45.424721, -75.695000],
      zoom: 12,

    });

    this.tiles.addTo(this.map);
  }

  async ngOnInit(): Promise<void> {
    await this.populateSelectList();
    this.initMap();
  }

  ngAfterViewInit(): void {

  }
}
