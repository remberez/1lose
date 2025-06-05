import api from './api';

export const MatchesService = {
  async list(filters = {}) {
    // Преобразуем filters в query string
    const params = new URLSearchParams(filters).toString();
    const { data } = await api.get(`/matches/${params ? '?' + params : ''}`);
    return data;
  },
  async get(matchId) {
    const { data } = await api.get(`/matches/${matchId}`);
    return data;
  },
  async create(matchData) {
    const { data } = await api.post('/matches/', matchData);
    return data;
  },
  async update(matchId, matchData) {
    const { data } = await api.patch(`/matches/${matchId}`, matchData);
    return data;
  },
  async delete(matchId) {
    await api.delete(`/matches/${matchId}`);
  },
};
