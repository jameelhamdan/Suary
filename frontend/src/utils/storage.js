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
    static storeUserData(uuid=null, username=null, full_name=null, avatar_uuid=null){
        if(uuid != null){
            setItem('uuid', uuid);
        }
        if(username != null){
            setItem('username', username);
        }
        if(full_name != null){
            setItem('full_name', full_name);
        }
        if(avatar_uuid != null){
            setItem('avatar_uuid', avatar_uuid);
        }
    }
    static getUserData(){
        if(!this.isAuthenticated()){
            return {};
        }
        return {
            'uuid': getItem('uuid'),
            'username': getItem('username'),
            'full_name': getItem('full_name'),
            'avatar_uuid': getItem('avatar_uuid'),
        }
    }
    static clear() {
        localStorage.removeItem(UserStorage.LOCAL_STORAGE_TOKEN);
        localStorage.removeItem(UserStorage.LOCAL_STORAGE_REFRESH_TOKEN);
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
