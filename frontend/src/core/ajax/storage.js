import axios from "axios";
import ApiUrlService from "../../shared/services"

export class TokenStorage {
    static isAuthenticated() {
        return this.getToken() !== null;
    }
    static getAuthentication() {
        return {
            headers: { 'Authorization': 'Bearer ' + this.getToken() }
        };
    }
    static getNewToken() {
        return new Promise((resolve, reject) => {
            axios.post(ApiUrlService.refreshToken(), { refresh_token: this.getRefreshToken() })
                .then(response => {
                this.storeToken(response.data.token);
                this.storeRefreshToken(response.data.refresh_token);
                resolve(response.data.token);
            })
                .catch((error) => {
                reject(error);
            });
        });
    }
    static storeToken(token) {
        localStorage.setItem(TokenStorage.LOCAL_STORAGE_TOKEN, token);
    }
    static storeRefreshToken(refreshToken) {
        localStorage.setItem(TokenStorage.LOCAL_STORAGE_REFRESH_TOKEN, refreshToken);
    }
    static clear() {
        localStorage.removeItem(TokenStorage.LOCAL_STORAGE_TOKEN);
        localStorage.removeItem(TokenStorage.LOCAL_STORAGE_REFRESH_TOKEN);
    }
    static getRefreshToken() {
        return localStorage.getItem(TokenStorage.LOCAL_STORAGE_REFRESH_TOKEN);
    }
    static getToken() {
        return localStorage.getItem(TokenStorage.LOCAL_STORAGE_TOKEN);
    }
}
TokenStorage.LOCAL_STORAGE_TOKEN = 'token';
TokenStorage.LOCAL_STORAGE_REFRESH_TOKEN = 'refresh_token';

