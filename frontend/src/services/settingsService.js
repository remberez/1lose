import { api } from "./api";

class SettingsService {
    async getBusinessSettings() {
        const response = await api.get("/business-settings");
        return response.data;
    }

    async updateSetting(name, value) {
        const response = await api.patch(`/business-settings/${name}`, {name, value});
        return response.data;
    }

    async createSetting(name, value) {
        const response = await api.post("/business-settings", {name, value});
        return response.data;
    }

    async deleteSetting(name) {
        const response = await api.delete(`/business-settings/${name}`);
        return response.data;
    }
}

export default new SettingsService();