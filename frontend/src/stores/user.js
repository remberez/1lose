import { makeAutoObservable, runInAction } from 'mobx';
import { AuthService } from '../services/auth';

class UserStore {
  user = null;
  isAuth = false;
  loading = false;
  error = null;

  constructor() {
    makeAutoObservable(this);
    this.checkAuth();
  }

  async login({ username, password }) {
    this.loading = true;
    this.error = null;
    try {
      const data = await AuthService.login({ username, password });
      const userData = await AuthService.me();

      runInAction(() => {
        this.isAuth = true;
        this.user = userData;
        this.loading = false;
      });
      return data;
    } catch (e) {
      runInAction(() => {
        this.error = e.response?.data?.detail || 'Ошибка авторизации';
        this.loading = false;
      });
      throw e;
    }
  }

  async register(userData) {
    this.loading = true;
    this.error = null;
    try {
      const data = await AuthService.register(userData);
      runInAction(() => {
        this.loading = false;
      });
      return data;
    } catch (e) {
      runInAction(() => {
        this.error = e.response?.data?.detail || 'Ошибка регистрации';
        this.loading = false;
      });
      throw e;
    }
  }

  logout() {
    AuthService.logout();
    this.isAuth = false;
    this.user = null;
  }

  async checkAuth() {
    const token = localStorage.getItem('access_token');
    this.isAuth = !!token;
    if (token) {
      try {
        const data = await AuthService.me();
        runInAction(() => {
          this.user = data;
        });
      } catch (e) {
        runInAction(() => {
          this.user = null;
          this.isAuth = false;
        });
      }
    } else {
      this.user = null;
    }
  }
}

export const userStore = new UserStore();
