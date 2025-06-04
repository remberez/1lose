import { makeAutoObservable, runInAction } from 'mobx';
import { GamesService } from '../services/games';

class GamesStore {
  games = [];
  loading = false;
  error = null;

  constructor() {
    makeAutoObservable(this);
  }

  async fetchGames() {
    this.loading = true;
    this.error = null;
    try {
      const data = await GamesService.list();
      runInAction(() => {
        this.games = data;
        this.loading = false;
      });
    } catch (e) {
      runInAction(() => {
        this.error = e.response?.data?.detail || 'Ошибка загрузки игр';
        this.loading = false;
      });
    }
  }
}

export const gamesStore = new GamesStore();
