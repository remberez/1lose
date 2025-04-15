import { FaGoogle, FaVk, FaTelegram, FaAt, FaYandex, FaOdnoklassniki, FaSteam } from 'react-icons/fa';
import { Link } from 'react-router-dom';

const LoginPage = () => {
  return (
    <div className="flex items-center justify-center h-full bg-oneWinBlue-400">
      <div className="bg-white rounded-2xl shadow-lg w-[360px] px-6 py-8">
        <div className="text-xl font-semibold text-oneWinBlue mb-1">Вход</div>
        <div className="text-sm text-gray-500 mb-5">Добро пожаловать в 1win</div>

        <div className="flex justify-between mb-5 gap-2">
          <button className="bg-white border rounded-lg p-2 text-lg"><FaGoogle className="text-[#DB4437]" /></button>
          <button className="bg-white border rounded-lg p-2 text-lg"><FaVk className="text-[#4C75A3]" /></button>
          <button className="bg-white border rounded-lg p-2 text-lg"><FaTelegram className="text-[#0088cc]" /></button>
          <button className="bg-white border rounded-lg p-2 text-lg"><FaAt className="text-gray-600" /></button>
          <button className="bg-white border rounded-lg p-2 text-lg"><FaYandex className="text-[#FF0000]" /></button>
          <button className="bg-white border rounded-lg p-2 text-lg"><FaOdnoklassniki className="text-[#EE8208]" /></button>
          <button className="bg-white border rounded-lg p-2 text-lg"><FaSteam className="text-[#171a21]" /></button>
        </div>

        <div className="flex items-center mb-5">
          <div className="flex-grow h-px bg-gray-200" />
          <span className="mx-2 text-gray-400 text-sm">или</span>
          <div className="flex-grow h-px bg-gray-200" />
        </div>

        <input
          type="text"
          placeholder="E-mail / телефон"
          className="w-full mb-3 px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-oneWinBrandBlue"
        />
        <input
          type="password"
          placeholder="Пароль"
          className="w-full mb-2 px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-oneWinBrandBlue"
        />

        <div className="text-right mb-5">
          <a href="#" className="text-sm text-gray-400 hover:text-oneWinBrandBlue">Забыли пароль?</a>
        </div>

        <button className="w-full py-2 rounded-lg bg-gradient-to-r from-oneWinBrandBlue to-blue-600 text-white font-semibold hover:opacity-90 transition">
          Войти
        </button>

        <div className="mt-5 text-center text-sm text-gray-400">
          Ещё нет аккаунта? <Link to={"/registration"} className="text-oneWinBrandBlue font-medium hover:underline">Зарегистрируйтесь</Link>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;