import { api } from "./api";

class TournamentService {
    async getAllTournaments() {
        const response = await api.get("/tournaments");
        return response.data;
    }
}

export default new TournamentService();