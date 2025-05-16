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

    async createEvent(eventData) {
        const response = await api.post("/events", eventData);
        return response.data;
    }

    async deleteEvent(eventId) {
        const response = await api.delete(`/events/${eventId}`);
        return response.status;
    }
}

export default new EventService();