import { BrowserRouter, Route, Routes } from 'react-router-dom';
import MainPage from './pages/MainPage';
import Layout from './components/Layout';
import LoginPage from './pages/LoginPage';
import RegistrationPage from './pages/RegistrationPage';
import AdminLayout from './components/AdminLayout';
import UserAdminPage from './pages/UserAdminPage';
import MatchAdminPage from './pages/MatchAdminPage';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<MainPage />} />
          <Route path="/login" element={<LoginPage/>} />
          <Route path="/registration" element={<RegistrationPage/>}/>
          <Route path="/admin" element={<AdminLayout/>}>
            <Route path="users" element={<UserAdminPage/>}/>
            <Route path="matches" element={<MatchAdminPage/>}/>
          </Route>
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
