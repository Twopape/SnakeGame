import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Component({

  selector: 'Leaderboard',
  template: `      <h2>Leaderboard</h2>
  <table>
    <tr>
      <td style="width:550px"><h3>Username:</h3></td>
      <td style="width:550px"><h3>Score: </h3></td>
      <td style="width:300px"><h3>Difficulty: </h3></td>
    </tr>
    <tr *ngFor="let player of _leaderboard">
      <td>          {{player.player}}        </td>
      <td>          {{player.score}}        </td>
      <td>          {{player.difficulty}}        </td>
    </tr>
  </table>  ` // FIXME weird ` symbol on webpage i cant get rid of
})
export class Leaderboard {
  _http:HttpClient;
  _id:Number;
  _leaderboard: Array<any>;
  _errorMessage:String = "";


  constructor(private http: HttpClient) {
    this._http = http;
    this.allPlayers()
  }
  allPlayers() {
    this._http.get<any>('http://localhost:1337/Player/All')
      // Get data and wait for result.
      .subscribe(result => {
          this._leaderboard = result.players;
        },

        error =>{
          // Let user know about the error.
          this._errorMessage = error;
        })

  }
}
