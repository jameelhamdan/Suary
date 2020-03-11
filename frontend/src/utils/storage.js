import SecureLS from "secure-ls";

const ls = new SecureLS({encodingType: "des", isCompression: false, encryptionSecret: "this-is-a-secret-key-but-its-meaningless-in-react"});
function setItem(item_name, item_value){
    ls.set(item_name, item_value);
}

function getItem(item_name){
    return ls.get(item_name);
}


export default class UserStorage {
    static isAuthenticated() {
        return this.getToken() !== null;
    }
    static getAuthentication() {
        return {
            headers: { "Authorization": "Bearer " + this.getToken() }
        };
    }
    static storeToken(token) {
        setItem(UserStorage.LOCAL_STORAGE_TOKEN, token);
    }
    static storeRefreshToken(refreshToken) {
        setItem(UserStorage.LOCAL_STORAGE_REFRESH_TOKEN, refreshToken);
    }
    static storeUserData(user_data){
        setItem(UserStorage.LOCAL_STORAGE_USER_DATA, user_data);
    }
    static getUserData(){
        const user_data = getItem(UserStorage.LOCAL_STORAGE_USER_DATA);
        if(!this.isAuthenticated() || user_data === null || user_data.length === 0){
            return null;
        }
        return user_data;
    }
    static clear() {
        ls.removeAll();
    }
    static getRefreshToken() {
        return getItem(UserStorage.LOCAL_STORAGE_REFRESH_TOKEN);
    }
    static getToken() {
        return getItem(UserStorage.LOCAL_STORAGE_TOKEN);
    }

}
UserStorage.LOCAL_STORAGE_TOKEN = "token";
UserStorage.LOCAL_STORAGE_REFRESH_TOKEN = "refresh_token";
UserStorage.LOCAL_STORAGE_USER_DATA = "user_data";
