import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import {formatCurrency} from "@angular/common";

@Component({
  selector: 'addScore',
  template:`
    <h3>ADD SCORE [TESTING]</h3>
    <table>
    <td>
      <input type="text"  style="width:300px" [(ngModel)]="_player"/>
    </td>
      <td>
        <input type="text"  style="width:300px" [(ngModel)]="_score"/>
      </td>
      <td>
        <input type="text"  style="width:300px" [(ngModel)]="_difficulty"/>
      </td>
      <td>
        <input type="submit" style="width:300px" value="Add Item to Menu" (click)="submitScore()" style="color:black">
      </td>
    </table>
    `
})


export class addScore {
  _productsArray: Array<any>;
  _http: HttpClient;
  _player: string;
  _score: number;
  _difficulty: string;
  _errorMessage: any;

  constructor(private http: HttpClient) {
    this._http = http;


  }


  async submitScore() {
    // This free online service receives post submissions.

    this.http.post("http://localhost:1337/Player/AddScore",
      {
        player: this._player,
        score: this._score,
        difficulty: this._difficulty

      })
      .subscribe(
        // Data is received from the post request.
        (data) => {
          // Inspect the data to know how to parse it.
          console.log("POST call successful. Inspect response.",
            JSON.stringify(data));
          this._errorMessage = data["errorMessage"];
        },
        // An error occurred. Data is not received.
        error => {
          this._errorMessage = error
        });
    if (this._errorMessage != ''){
      this._errorMessage = ''
    }
  }
}
