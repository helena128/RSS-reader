import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {DataserviceService} from '../dataservice.service';

@Component({
  selector: 'app-channel',
  templateUrl: './channel.component.html',
  styleUrls: ['./channel.component.scss']
})
export class ChannelComponent implements OnInit {

  public channelId: string;
  public rssInfo: Object[];
  public feeds: Object[];
  public pageSizes = ['10', '20', '50'];
  public pageSize = '10';
  public pageNumber = 0;
  public total = 10;
  private Math: any;

  constructor(private activeRoute: ActivatedRoute,
              private ds: DataserviceService) {
    this.Math = Math;
  }

  ngOnInit() {
    this.activeRoute.params.subscribe(params => {
      this.channelId = params.id;
      this.ds.getRssInfo(this.channelId)
        .subscribe(info => this.rssInfo = info[0]);
      this.getTotalFeeds();
    });
    this.getFeeds();
  }

  changePageSize(size) {
    if (this.pageSize === size) {
      return;
    }
    this.pageSize = size;
    this.getFeeds();
  }

  selectNextPage() {
    const totalRecords = this.total as number;
    const tmpPageSize = parseInt(this.pageSize, 0);
    if (this.pageNumber === this.Math.ceil(totalRecords / tmpPageSize) - 1) {
      return;
    }
    this.pageNumber++;
    this.getFeeds();
  }

  selectPreviousPage() {
    if (this.pageNumber === 0) {
      return;
    }
    this.pageNumber--;
    this.getFeeds();
  }

  onUpdate() {
    this.ds.updateRssChannel(this.channelId, this.pageSize)
      .subscribe(data => this.feeds = data);
  }

  private getFeeds() {
    this.ds.getFeedsForRssChannel(this.channelId, this.pageSize, this.pageNumber)
      .subscribe(data => this.feeds = data);
    this.getTotalFeeds();
  }

  private getTotalFeeds() {
    this.ds.getTotalFeeds(this.channelId).subscribe(data => this.total = data);
  }

}
