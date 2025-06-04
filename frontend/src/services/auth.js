import api from './api';

export const AuthService = {
  async login({ username, password }) {
    const form = new FormData();
    form.append('username', username);
    form.append('password', password);
    const { data } = await api.post('/auth/login', form);
    if (data.access_token) localStorage.setItem('access_token', data.access_token);
    if (data.refresh_token) localStorage.setItem('refresh_token', data.refresh_token);
    return data;
  },
  async register(userData) {
    const { data } = await api.post('/auth/register', userData);
    return data;
  },
  async logout() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    // Можно добавить логаут-запрос на бэкенд, если потребуется
  },
  async refresh() {
    const { data } = await api.post('/auth/refresh');
    if (data.access_token) localStorage.setItem('access_token', data.access_token);
    if (data.refresh_token) localStorage.setItem('refresh_token', data.refresh_token);
    return data;
  },
  async me() {
    const { data } = await api.get('/users/me');
    return data;
  },
};
