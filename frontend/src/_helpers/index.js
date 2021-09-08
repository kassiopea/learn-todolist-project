import { createBrowserHistory } from 'history';

export const history = createBrowserHistory({forceRefresh:true});

export const getCookie = (key) => {
    const b = document.cookie.match("(^|;)\\s*" + key + "\\s*=\\s*([^;]+)");
    return b ? b.pop() : "";
}

export const delCookie = (key) => {
    document.cookie = `${key}=;  expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
  }