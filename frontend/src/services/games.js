import api from './api';

export const GamesService = {
  async list() {
    const { data } = await api.get('/games/');
    return data;
  },
  async get(gameId) {
    const { data } = await api.get(`/games/${gameId}`);
    return data;
  },
  async delete(gameId) {
    await api.delete(`/games/${gameId}`);
  },
  // Можно добавить create/update если потребуется
};
