import { ModuleWithProviders }   from '@angular/core';
import { Routes, RouterModule }  from '@angular/router';
import { AppComponent }          from './app.component';
import { Leaderboard }        from './app.leaderboard';

import { addScore } from './app.addScore'
const appRoutes: Routes = [
  { path: 'Leaderboard', component: Leaderboard },

  { path: 'addScore', component: addScore },

];

export const routing: ModuleWithProviders = RouterModule.forRoot(appRoutes);
