import { api } from "./api";

class BetService {
    async createBet({ event_id, outcome_id, amount }) {
        const response = await api.post("/bets", {event_id, outcome_id, amount});
        return response;
    }
}

export default new BetService();