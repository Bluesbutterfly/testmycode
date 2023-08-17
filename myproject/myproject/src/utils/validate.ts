/**
 * Created by PanJiaChen on 16/11/18.
 */

/**
 * 密码
 * @param {string} path
 * @returns {Boolean}
 */
export function checkPassWord(path) {
  return /^(?=.*\d)(?=.*[a-zA-Z])[\da-zA-Z~!@#$%^&*]{6,16}$/.test(path);
}
/**
 * 空中密码
 * @param {string} path
 * @returns {Boolean}
 */
 export function checkKzPassWord(path) {
  return /^[^\w\.\/]{6,16}$/ig.test(path);
}

/**
 * 账号
 * @param {*} path 
 * @returns {Boolean}
 */
export function checkUserNameZZ(path) {
  return new RegExp(
    "(^[a-zA-Z0-9_-][a-zA-Z0-9_+-]{3,15}$)|(^[a-zA-Z0-9_.-]{2,20}\\@[A-Za-z0-9]+((\\.|-)[A-Za-z0-9]+)*(\\.[A-Za-z]{2,5})+$)|(^1[3456789][0-9]{9}$)",
    "gi"
).test(path);
}
/**
 * 验证手机号码
 * @param {*} path 
 * @returns {Boolean}
 */
export function checkTelphone(path) {
  return /^(11[0-9]|13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}$/.test(path);
}
/**
 * 游戏昵称
 * @param {*} path 
 * @returns {Boolean}
 */
export function checkNickname(path) {
  return /^[\u4e00-\u9fa5a-zA-Z0-9]{2,14}$/.test(path);
}

/**
 * 验证码
 * @param {*} path 
 * @returns {Boolean}
 */
export function checksecurity(path) {
  return /^[0-9]{4,11}$/.test(path);
}

/**
 * 姓名
 * @param {*} path 
 * @returns {Boolean}
 */
export function checkName(path) {
  return /^[u4e00-\u9fa5]{2,11}$/.test(path);
}

/**
 * 身份证号码
 * @param {*} path 
 * @returns {Boolean}
 */
export function checkIdcard(path) {
  return /^[1-9]\d{7}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}$|^[1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}([0-9]|X)$/.test(path);
}

/**
 * @param {string} url
 * @returns {Boolean}
 */
export function validURL(url) {
  const reg = /^(https?|ftp):\/\/([a-zA-Z0-9.-]+(:[a-zA-Z0-9.&%$-]+)*@)*((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}|([a-zA-Z0-9-]+\.)*[a-zA-Z0-9-]+\.(com|edu|gov|int|mil|net|org|biz|arpa|info|name|pro|aero|coop|museum|[a-zA-Z]{2}))(:[0-9]+)*(\/($|[a-zA-Z0-9.,?'\\+&%$#=~_-]+))*$/;
  return reg.test(url);
}

/**
 * @param {string} str
 * @returns {Boolean}
 */
export function validLowerCase(str) {
  const reg = /^[a-z]+$/;
  return reg.test(str);
}

/**
 * @param {string} str
 * @returns {Boolean}
 */
export function validUpperCase(str) {
  const reg = /^[A-Z]+$/;
  return reg.test(str);
}

/**
 * @param {string} str
 * @returns {Boolean}
 */
export function validAlphabets(str) {
  const reg = /^[A-Za-z]+$/;
  return reg.test(str);
}

/**
 * @param {string} email
 * @returns {Boolean}
 */
export function validEmail(email) {
  const reg = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return reg.test(email);
}

/**
 * @param {string} str
 * @returns {Boolean}
 */
export function isString(str) {
  if (typeof str === "string" || str instanceof String) {
    return true;
  }
  return false;
}

