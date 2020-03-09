function setItem(item_name, item_value){
    localStorage.setItem(item_name, item_value);
}

function getItem(item_name){
    return localStorage.getItem(item_name);
}


export default class UserStorage {
    static isAuthenticated() {
        return this.getToken() !== null;
    }
    static getAuthentication() {
        return {
            headers: { 'Authorization': 'Bearer ' + this.getToken() }
        };
    }
    static storeToken(token) {
        setItem(UserStorage.LOCAL_STORAGE_TOKEN, token);
    }
    static storeRefreshToken(refreshToken) {
        setItem(UserStorage.LOCAL_STORAGE_REFRESH_TOKEN, refreshToken);
    }
    static storeUserData(user_data){
        const json_string = JSON.stringify(user_data);
        setItem(UserStorage.LOCAL_STORAGE_USER_DATA, json_string);
    }
    static getUserData(){
        const json_string = getItem(UserStorage.LOCAL_STORAGE_USER_DATA);
        if(!this.isAuthenticated() || json_string ===null || json_string.length === 0){
            return null;
        }
        return JSON.parse(json_string);
    }
    static clear() {
        localStorage.removeItem(UserStorage.LOCAL_STORAGE_TOKEN);
        localStorage.removeItem(UserStorage.LOCAL_STORAGE_REFRESH_TOKEN);
        localStorage.removeItem(UserStorage.LOCAL_STORAGE_USER_DATA);
    }
    static getRefreshToken() {
        return getItem(UserStorage.LOCAL_STORAGE_REFRESH_TOKEN);
    }
    static getToken() {
        return getItem(UserStorage.LOCAL_STORAGE_TOKEN);
    }

}
UserStorage.LOCAL_STORAGE_TOKEN = 'token';
UserStorage.LOCAL_STORAGE_REFRESH_TOKEN = 'refresh_token';
UserStorage.LOCAL_STORAGE_USER_DATA = 'user_data';
