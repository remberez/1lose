// routes.jsx — определение маршрутов для сайта 1lose
import { createBrowserRouter } from 'react-router-dom';
import Layout from './components/layout/Layout';
import Home from './pages/Home';
import Esports from './pages/Esports';
import Lotteries from './pages/Lotteries';
import Clubs from './pages/Clubs';
import Stats from './pages/Stats';
import Results from './pages/Results';
import Gifts from './pages/Gifts';
import Tournaments from './pages/Tournaments';
import Help from './pages/Help';
import AuthPage from './pages/Auth';
import RegisterPage from './pages/Register';

const router = createBrowserRouter([
  {
    path: '/',
    element: <Layout />,
    children: [
      { index: true, element: <Home /> },
      { path: 'esports', element: <Esports /> },
      { path: 'lotteries', element: <Lotteries /> },
      { path: 'clubs', element: <Clubs /> },
      { path: 'stats', element: <Stats /> },
      { path: 'results', element: <Results /> },
      { path: 'gifts', element: <Gifts /> },
      { path: 'tournaments', element: <Tournaments /> },
      { path: 'help', element: <Help /> },
      { path: 'auth', element: <AuthPage /> },
      { path: 'register', element: <RegisterPage /> },
    ],
  },
]);

export default router;
