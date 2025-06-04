// src/components/layout/Header.jsx
import { Link } from 'react-router-dom';
import { observer } from 'mobx-react-lite';
import { FiGift, FiHelpCircle, FiSettings, FiBell, FiLogIn, FiUser } from 'react-icons/fi';
import { FaTrophy } from 'react-icons/fa';
import { userStore } from '../../stores/user';
import { useEffect, useRef, useState } from 'react';

const navMain = [
  { name: 'Киберспорт', to: '/esports' },
  { name: 'Лотереи', to: '/lotteries' },
  { name: 'Наши клубы', to: '/clubs' },
  { name: 'Статистика', to: '/stats' },
  { name: 'Результаты', to: '/results' },
];
const navActions = [
  { name: 'Подарки', to: '/gifts', icon: <FiGift size={17} /> },
  { name: 'Турниры', to: '/tournaments', icon: <FaTrophy size={17} /> },
  { name: 'Помощь', to: '/help', icon: <FiHelpCircle size={17} /> },
];

const Header = observer(() => {
  useEffect(() => {
    userStore.checkAuth();
  }, []);

  const [menuOpen, setMenuOpen] = useState(false);
  const menuRef = useRef(null);
  let closeTimeout = useRef();

  // Закрытие меню при клике вне
  useEffect(() => {
    if (!menuOpen) return;
    const handleClick = (e) => {
      if (menuRef.current && !menuRef.current.contains(e.target)) {
        setMenuOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClick);
    return () => document.removeEventListener('mousedown', handleClick);
  }, [menuOpen]);

  // Корректная работа hover-меню: не закрывать при переходе с кнопки на меню
  const handleButtonMouseEnter = () => {
    clearTimeout(closeTimeout.current);
    setMenuOpen(true);
  };
  const handleButtonMouseLeave = () => {
    closeTimeout.current = setTimeout(() => setMenuOpen(false), 200);
  };
  const handleMenuMouseEnter = () => {
    clearTimeout(closeTimeout.current);
    setMenuOpen(true);
  };
  const handleMenuMouseLeave = () => {
    closeTimeout.current = setTimeout(() => setMenuOpen(false), 200);
  };

  return (
    <header className="sticky top-0 z-50 bg-blue-900 text-white shadow">
      <div className="container mx-auto flex items-center justify-between py-2 px-2 md:py-2 md:px-4">
        {/* Логотип */}
        <Link to="/" className="text-xl md:text-2xl font-extrabold tracking-widest select-none font-display text-white">
          1lose
        </Link>
        {/* Основные вкладки */}
        <nav className="flex gap-2 md:gap-4">
          {navMain.map((item) => (
            <Link key={item.to} to={item.to} className="px-2 py-1 rounded-md text-blue-100 hover:bg-blue-700 hover:text-white font-medium transition-colors text-sm md:text-base">
              {item.name}
            </Link>
          ))}
        </nav>
        {/* Actions */}
        <div className="flex items-center gap-2 md:gap-3">
          {navActions.map((item) => (
            <Link key={item.to} to={item.to} className="flex items-center gap-1 text-blue-200 hover:bg-blue-700 hover:text-white transition-colors px-2 py-1 rounded-md text-sm">
              {item.icon}
              <span className="hidden sm:inline text-sm">{item.name}</span>
            </Link>
          ))}
          {/* Иконки и кнопки */}
          <button className="p-2 rounded-full hover:bg-blue-700 text-blue-200 hover:text-white transition-colors" title="Настройки">
            <FiSettings size={17} />
          </button>
          <button className="p-2 rounded-full hover:bg-blue-700 text-blue-200 hover:text-white transition-colors" title="Уведомления">
            <FiBell size={17} />
          </button>
          {userStore.isAuth ? (
            <div className="relative" ref={menuRef}>
              <button
                className="flex items-center gap-2 ml-1 bg-blue-800 hover:bg-blue-700 text-white font-semibold px-4 py-2 rounded-lg text-sm md:text-sm transition-colors"
                onMouseEnter={handleButtonMouseEnter}
                onMouseLeave={handleButtonMouseLeave}
                type="button"
              >
                <FiUser size={17} />
                <span>{userStore.user?.balance}₽</span>
              </button>
              {menuOpen && (
                <div
                  className="absolute right-0 mt-2 w-48 bg-blue-900 border border-blue-700 rounded-lg shadow-lg py-2 z-50 flex flex-col text-white"
                  onMouseEnter={handleMenuMouseEnter}
                  onMouseLeave={handleMenuMouseLeave}
                >
                  <Link to="/profile" className="px-4 py-2 hover:bg-blue-800 transition-colors">Профиль</Link>
                  <button className="px-4 py-2 text-left hover:bg-blue-800 transition-colors w-full">Пополнить баланс</button>
                  <button className="px-4 py-2 text-left hover:bg-blue-800 transition-colors w-full" onClick={() => { userStore.logout(); setMenuOpen(false); }}>Выйти</button>
                </div>
              )}
            </div>
          ) : (
            <Link to="/auth" className="flex items-center gap-2 ml-1 bg-blue-700 hover:bg-blue-800 text-white font-semibold px-4 py-2 rounded-lg text-sm md:text-base transition-colors">
              <FiLogIn size={15} />
              <span>Войти</span>
            </Link>
          )}
        </div>
      </div>
    </header>
  );
});

export default Header;
