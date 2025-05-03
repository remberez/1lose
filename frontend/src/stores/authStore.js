import { makeAutoObservable } from "mobx";

class UserStore {
    user = null;
    isAuth = false;
    isLoading = null;

    constructor() {
        makeAutoObservable(this);
    }

    setUser(userData) {
        this.user = userData;
    }

    setAuth(status) {
        this.isAuth = status;
    }

    login(userData) {
        this.setUser(userData);
        this.setAuth(true);
    }

    logout() {
        this.setUser(null);
        this.setAuth(false);
    }

    setIsLoading(value) {
        this.isLoading = value;
    }
}

export const userStore = new UserStore();