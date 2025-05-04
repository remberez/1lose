import { api } from "./api";

class EventService {
    async getEvents({match_id}) {
        const response = await api.get("/events", {
            params: {
                match_id,
            }
        });
        return response.data;
    }
}

export default new EventService();