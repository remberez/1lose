import { makeAutoObservable } from "mobx";

class UserStore {
    user = null;
    isAuth = false;

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
}

export const userStore = new UserStore();