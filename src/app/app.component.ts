import {OnInit, Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})

export class AppComponent implements OnInit {
  title = 'ellasite';

  draw(): void {
    document.getElementById('anim')!.classList.add('active')
    console.log('done')
  }

  ngOnInit(): void {
    setTimeout(() => {
      this.draw();
    }, 300)
  }
}
