import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template:'    <a routerLink="/Leaderboard" routerLinkActive="active">Leaderboard</a> |\n' +
    // temp admin feature removed'    <a routerLink="/addScore" routerLinkActive="active">Add Score</a>\n' +
    '    <!-- Where router should display a view -->\n' +
    '    <router-outlet></router-outlet>`\n'
})

export class AppComponent {
}
