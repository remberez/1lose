// src/components/layout/Layout.jsx
import Header from './Header';
import Footer from './Footer';
import { Outlet } from 'react-router-dom';

const Layout = () => (
  <div className="flex flex-col min-h-screen font-display text-white bg-gray-200">
    <Header />
    <main className="flex-1 w-full px-0 text-white">
      <div className="mx-auto text-white">
        <Outlet />    
      </div>
    </main>
    <Footer />
  </div>
);

export default Layout;
