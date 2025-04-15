import { useState } from 'react';
import { HiOutlinePlus } from 'react-icons/hi';
import { Link } from 'react-router-dom';

const RegistrationPage = () => {
  const [tab, setTab] = useState('fast');
  const [agreed, setAgreed] = useState(true);

  return (
    <div className="flex items-center justify-center h-full bg-oneWinBlue-400">
      <div className="bg-white rounded-2xl shadow-lg w-[400px] px-6 py-8 text-sm">
        
        <div className="text-xl font-semibold text-oneWinBlue mb-4">Регистрация</div>

        <div className="flex mb-5 bg-gray-100 rounded-lg overflow-hidden">
          <button
            onClick={() => setTab('social')}
            className={`flex-1 py-2 text-center font-medium transition ${
              tab === 'social' ? 'bg-white text-oneWinBlue shadow-sm' : 'text-gray-500'
            }`}
          >
            Соц. сети
          </button>
          <button
            onClick={() => setTab('fast')}
            className={`flex-1 py-2 text-center font-medium transition ${
              tab === 'fast' ? 'bg-white text-oneWinBlue shadow-sm' : 'text-gray-500'
            }`}
          >
            ✉ Быстрая
          </button>
        </div>

        <div className="mb-3">
          <label className="text-gray-600 text-sm mb-1 block">Валюта</label>
          <select className="w-full px-4 py-2 border rounded-lg bg-gray-50 text-sm">
            <option>Российский рубль (RUB)</option>
            <option>Доллар США (USD)</option>
            <option>Евро (EUR)</option>
          </select>
        </div>

        <div className="mb-3">
          <input
            type="tel"
            placeholder="+7 (912) 345 67-89"
            className="w-full px-4 py-2 border rounded-lg bg-gray-50 text-sm"
          />
        </div>

        <div className="mb-3">
          <input
            type="email"
            placeholder="E-Mail"
            className="w-full px-4 py-2 border rounded-lg bg-gray-50 text-sm"
          />
        </div>

        <div className="mb-3">
          <input
            type="password"
            placeholder="Пароль"
            className="w-full px-4 py-2 border rounded-lg bg-gray-50 text-sm"
          />
        </div>

        <div className="mb-4 flex items-center justify-between">
          <span className="text-gray-600">Промокод</span>
          <HiOutlinePlus className="text-oneWinBrandBlue cursor-pointer" />
        </div>

        <div className="flex items-start gap-2 mb-5">
          <input
            type="checkbox"
            checked={agreed}
            onChange={() => setAgreed(!agreed)}
            className="mt-1 accent-oneWinBrandBlue"
          />
          <span className="text-xs text-gray-500">
            Я подтверждаю, что ознакомлен и полностью согласен с{' '}
            <a href="#" className="text-oneWinBrandBlue underline">Условиями Соглашения</a>
          </span>
        </div>

        <button className="w-full py-2 rounded-lg bg-green-400 text-white font-medium hover:bg-green-500 transition">
          Зарегистрироваться
        </button>

        <div className="mt-5 text-center text-gray-400 text-sm">
          Уже есть аккаунт? <Link to={"/login"} className="text-oneWinBrandBlue hover:underline">Войти</Link>
        </div>
      </div>
    </div>
  );
};

export default RegistrationPage;
