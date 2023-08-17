import Cookies from 'js-cookie'

const tokenKey = 'token'

export const getToken = () => {
    return Cookies.get(tokenKey)
}
export const setToken = (token:any) => {
    return Cookies.set(tokenKey, token)
}

export const removeToken = () => {
    return Cookies.remove(tokenKey)
}