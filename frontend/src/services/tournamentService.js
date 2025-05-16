import { api } from "./api";

class TournamentService {
    async getAllTournaments() {
        const response = await api.get("/tournaments");
        return response.data;
    }

    async createTournament(data) {
        const response = await api.post("/tournaments", data);
        return response.data;
    }

    async deleteTournament(tourId) {
        const response = await api.delete(`/tournaments/${tourId}`);
        return response.status;
    }

    async getTournamentById(id) {
        const response = await api.get(`/tournaments/${id}`);
        return response.data;
    }

    async updateTournament(id, data) {
        const response = await api.patch(`/tournaments/${id}`, data);
        return response.data;
    }
}

export default new TournamentService();