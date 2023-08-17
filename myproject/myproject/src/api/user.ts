import request from '@/utils/request'
const api = process.env.NODE_ENV == 'development'?'http://127.0.0.1:5000':'/'
//注册账号
export function register(params:any) {
    return request({
        url: api+'/register',
        method: 'POST',
        data: params
    })
}
// 登录
export function Login(params:any){
  return request({
      url: api+'/login',
      method: 'POST',
      data: params
  })
}
// 获取是否登录
export function GetuserStatus(){
  return request({
      url: api+'/userStatus',
      method: 'GET'
  })
}
// 注销用户
export function logout(){
  return request({
      url: api+'/logout',
      method: 'GET'
  })
}