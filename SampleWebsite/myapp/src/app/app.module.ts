import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule }    from '@angular/forms';
import {HttpClientModule} from '@angular/common/http';
import { routing } from './app.routing';
import { Leaderboard } from './app.leaderboard'

import { addScore } from './app.addScore'
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent, Leaderboard, addScore
  ],
  imports: [
    BrowserModule, FormsModule, HttpClientModule, routing],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

