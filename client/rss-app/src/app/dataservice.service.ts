import { Injectable } from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';
import { Observable } from 'rxjs';
import {RssModel} from './models/rss.model';

@Injectable()
export class DataserviceService {

  private _url = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) { }

  getRssChannels(): Observable<RssModel[]> {
    return this.http.get<RssModel[]>(this._url + '/rss');
  }

  getFeedsForRssChannel(rssId, pageSize, pageNumber): Observable<Object[]> {
    return this.http.get<Object[]>(this._url + '/feeds?source=' + rssId +
      '&size=' + pageSize + '&page=' + pageNumber);
  }

  getRssInfo(rssId): Observable<Object> {
    return this.http.get<Object>(this._url + '/rss?id=' + rssId);
  }

  getTotalFeeds(rssId): Observable<any> {
    return this.http.get<any>(this._url + '/total?id=' + rssId);
  }

  saveRssChannel(rssLink): Observable<any> {
    return this.http.post<any>(this._url + '/rss', {'link': rssLink});
  }

  updateRssChannel(rssId, pageSize): Observable<Object[]> {
    return this.http.get<Object[]>(this._url + '/update?id=' + rssId + '&size=' + pageSize);
  }
}
