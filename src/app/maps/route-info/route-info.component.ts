import { Component, AfterViewInit } from '@angular/core';
import { RequestService } from '../../request.service';
import * as L from 'leaflet';
import * as geojson from 'geojson';

@Component({
  selector: 'app-route-info',
  templateUrl: './route-info.component.html',
  styleUrls: ['./route-info.component.scss']
})
export class RouteInfoComponent implements AfterViewInit {
  constructor(public requestService: RequestService) {}

  private coords : any;
  private map : any;
  private mapApiKey = import.meta.env.NG_APP_MAP_API_KEY;
  private async initMap(): Promise<void> {
    this.map = L.map('map', {
      center: [45.424721, -75.695000],
      zoom: 12
    });

    const tiles = L.tileLayer('https://api.maptiler.com/maps/basic-v2/{z}/{x}/{y}@2x.png?key='+this.mapApiKey, {
      tileSize: 512,
      zoomOffset: -1,
      maxZoom: 18,
      minZoom: 3,
      attribution: '<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>'
    });

    tiles.addTo(this.map);

    this.coords = await this.requestService.get('/api/shape/shp-110-52').toPromise();

    console.log(this.coords)

    var geojsonFeature: geojson.Feature = ({
        "type": "Feature",
        "properties": {
            "name": "Coors Field",
            "amenity": "Baseball Stadium",
            "popupContent": "This is where the Rockies play!"
        },
        "geometry": {
            "type": "LineString",
            "coordinates": this.coords
        }
    });

    console.log(geojsonFeature);

    function onEachFeature(feature: any, layer: any) {
        // does this feature have a property named popupContent?
        if (feature.properties && feature.properties.popupContent) {
            layer.bindPopup(feature.properties.popupContent);
        }
    }

    L.geoJSON(geojsonFeature, {
      onEachFeature: onEachFeature
    }).addTo(this.map);


  }

  ngAfterViewInit(): void {
    this.initMap()
  }
}
