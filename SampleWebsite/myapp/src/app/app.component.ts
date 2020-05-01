import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import {formatCurrency} from "@angular/common";

const BASE_URL = "http://localhost:1337/Product/";

@Component({
  selector: 'app-root',
  template:'    <a routerLink="/Leaderboard" routerLinkActive="active">Leaderboard</a> |\n' +
    '    <a routerLink="/addScore" routerLinkActive="active">Add Score</a>\n' +
    '    <!-- Where router should display a view -->\n' +
    '    <router-outlet></router-outlet>`\n'
})

export class AppComponent {
}
