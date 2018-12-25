import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SidebarComponent } from './sidebar/sidebar.component';
import {DataserviceService} from './dataservice.service';
import {HttpClientModule} from '@angular/common/http';
import { MainComponent } from './main/main.component';
import {RouterModule, Routes} from '@angular/router';
import { ChannelComponent } from './channel/channel.component';
import {MatSelectModule} from '@angular/material/select';
import { FormsModule } from '@angular/forms';

const appRoutes: Routes = [
  { path: '', component: MainComponent},
  { path: 'home', component: MainComponent},
  { path: 'channel/:id', component: ChannelComponent}
];

@NgModule({
  declarations: [
    AppComponent,
    SidebarComponent,
    MainComponent,
    ChannelComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    RouterModule.forRoot(appRoutes),
    MatSelectModule,
    FormsModule
  ],
  providers: [DataserviceService],
  bootstrap: [AppComponent]
})
export class AppModule { }
