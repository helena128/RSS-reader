import {Component, OnInit} from '@angular/core';
import {DataserviceService} from '../dataservice.service';
import {Router} from '@angular/router';
import {RssModel} from '../models/rss.model';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.scss']
})
export class SidebarComponent implements OnInit {
  public rssChannels: Array<RssModel>;
  public newRssChannelLink: string;

  constructor(private ds: DataserviceService,
              private router: Router) { }

  ngOnInit() {
    this.ds.getRssChannels().subscribe(data => {
      this.rssChannels = data as Array<RssModel>;
      console.log(this.rssChannels);
    });
  }

  onChannelSelect(rssId) {
    this.router.routeReuseStrategy.shouldReuseRoute = function() { return false; };
    this.router.navigate(['channel', rssId]);
  }

  onAddChannel(): void {
    /*alert('Saving: ' + this.newRssChannelLink);*/
    this.ds.saveRssChannel(this.newRssChannelLink)
      .subscribe(data => this.rssChannels = data as Array<RssModel>);
  }
}


