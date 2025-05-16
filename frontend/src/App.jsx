import { BrowserRouter, Route, Routes } from 'react-router-dom';
import MainPage from './pages/MainPage';
import Layout from './components/Layout';
import LoginPage from './pages/LoginPage';
import RegistrationPage from './pages/RegistrationPage';
import AdminLayout from './components/AdminLayout';
import UserAdminPage from './pages/UserAdminPage';
import MatchAdminPage from './pages/MatchAdminPage';
import GameAdminPage from './pages/GameAdminPage';
import TeamAdminPage from './pages/TeamAdminPage';
import TournamentAdminPage from './pages/TournamentAdminPage';
import BusinessSettingsAdminPage from './pages/BusinessSettingsAdminPage';
import { userStore } from './stores/authStore';
import { observer } from 'mobx-react-lite';
import { useEffect } from 'react';
import userService from './services/userService';
import UserEditPage from './components/UserEditPage';
import MatchPage from './pages/MatchPage';
import TeamEditPage from './pages/TeamEditPage';
import GameEditPage from './pages/GameEditPage';
import TournamentEditPage from './pages/TournamentEditPage';

function App() {
  useEffect(() => {
    const initAuth = async () => {
        const token = localStorage.getItem("token");

        if (token) {
            try {
                userStore.setIsLoading(true);
                const userData = await userService.getMe();
                userStore.login(userData);
                userStore.setIsLoading(false);
            } catch (e) {
                console.error("Ошибка при проверке токена:", e);
                userStore.logout();
            }
        }
    };

    initAuth();
  }, []);

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<MainPage />} />
          <Route path="/login" element={<LoginPage/>} />
          <Route path="/registration" element={<RegistrationPage/>}/>
          <Route path="/match/:id" element={<MatchPage/>}/>
          {
            !userStore.isLoading && userStore.user?.role_code === "admin" &&
              <Route path="/admin" element={<AdminLayout/>}>
                <Route path="users" element={<UserAdminPage/>}/>
                <Route path="users/:id" element={<UserEditPage/>}/>

                <Route path="matches" element={<MatchAdminPage/>}/>

                <Route path="games" element={<GameAdminPage/>}/>
                <Route path="/admin/games/:id" element={<GameEditPage />} />

                <Route path="teams" element={<TeamAdminPage/>}/>
                <Route path="teams/:id" element={<TeamEditPage />} />

                <Route path="tournaments" element={<TournamentAdminPage/>}/>
                <Route path="tournaments/:id" element={<TournamentEditPage />} />

                <Route path="business-settings" element={<BusinessSettingsAdminPage/>}/>
              </Route>
          }
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default observer(App);
