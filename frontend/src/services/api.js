import axios from 'axios';

// Получение токенов из localStorage
function getAccessToken() {
  return localStorage.getItem('access_token');
}
function getRefreshToken() {
  return localStorage.getItem('refresh_token');
}
function setTokens({ access_token, refresh_token }) {
  if (access_token) localStorage.setItem('access_token', access_token);
  if (refresh_token) localStorage.setItem('refresh_token', refresh_token);
}

const api = axios.create({
  baseURL: 'http://localhost:8000/api', // настройте под свой backend
  withCredentials: true,
});

// Флаг для предотвращения бесконечных циклов refresh
let isRefreshing = false;
let failedQueue = [];

function processQueue(error, token = null) {
  failedQueue.forEach(prom => {
    if (error) {
      prom.reject(error);
    } else {
      prom.resolve(token);
    }
  });
  failedQueue = [];
}

api.interceptors.request.use(
  config => {
    const token = getAccessToken();
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  error => Promise.reject(error)
);

api.interceptors.response.use(
  response => response,
  async error => {
    const originalRequest = error.config;
    if (error.response?.status === 401 && !originalRequest._retry && getRefreshToken()) {
      if (isRefreshing) {
        return new Promise(function (resolve, reject) {
          failedQueue.push({ resolve, reject });
        })
          .then(token => {
            originalRequest.headers['Authorization'] = 'Bearer ' + token;
            return api(originalRequest);
          })
          .catch(err => Promise.reject(err));
      }
      originalRequest._retry = true;
      isRefreshing = true;
      try {
        const auth = "Bearer " + getRefreshToken();
        const response = await axios.post('http://localhost:8000/api/auth/refresh', {}, {
          headers: { 'Authorization': auth },
        });
        setTokens({access_token: response.data.access_token});
        api.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access_token;
        processQueue(null, response.data.access_token);
        return api(originalRequest);
      } catch (err) {
        processQueue(err, null);
        // Удаляем токены только если refresh тоже невалиден (например, 401 на /refresh)
        if (err.response && err.response.status === 401) {
          localStorage.removeItem('access_token');
          localStorage.removeItem('refresh_token');
          // Можно добавить редирект на /login
        }
        return Promise.reject(err);
      } finally {
        isRefreshing = false;
      }
    }
    return Promise.reject(error);
  }
);

export default api;
