import { Link } from "react-router-dom";
import logo from "../assets/logo.png";
import { useEffect } from "react";
import { userStore } from "../stores/authStore";
import userService from "../services/userService";
import {observer} from "mobx-react-lite"
import authService from "../services/AuthService";

const NavBarItem = ({ children }) => {
    return (
      <Link className="
        hover:bg-oneWinBlue-600 
        transition-colors 
        duration-200 
        h-full 
        flex 
        items-center 
        px-2
        py-2
      ">
        {children}
      </Link>
    )
  }

const NavBar = () => {
    return (
        <nav className="flex min-h-[100%] text-sm">
            <NavBarItem>
                Киберспорт
            </NavBarItem>
            <NavBarItem>
                Лотереи
            </NavBarItem>
            <NavBarItem>
                Медиа
            </NavBarItem>
            <NavBarItem>
                Приложение
            </NavBarItem>
            <NavBarItem>
                Наши клубы
            </NavBarItem>
            <NavBarItem>
                Статистика
            </NavBarItem>
            <NavBarItem>
                Результаты
            </NavBarItem>
        </nav>
    )
}


const Header = observer(() => {
    useEffect(() => {
        const initAuth = async () => {
            const token = localStorage.getItem("token");
    
            if (token) {
                try {
                    const userData = await userService.getMe();
                    userStore.login(userData);
                } catch (e) {
                    console.error("Ошибка при проверке токена:", e);
                    userStore.logout();
                }
            }
        };

        initAuth();
    }, []);

    return (
        <header className="bg-oneWinBlue text-white">
            <div className="flex container items-center justify-between">
                <div className="flex gap-x-12 h-full">
                    <Link to={"/"}>
                        <img 
                            src={logo} 
                            alt="Логотип 1lose"
                            width={80}
                            height={20}
                            className="py-2"
                        />
                    </Link>
                    <NavBar/>
                </div>
                <div className="flex items-center gap-x-4 h-full text-sm">
                    {userStore.isAuth ? (
                        <div className="flex items-center gap-x-4">
                            <span className="text-white">Привет, {userStore.user?.email}</span>
                            <button 
                                onClick={async () => {
                                    await authService.logout();
                                    userStore.logout();
                                    localStorage.removeItem("token");
                                }}
                                className="text-sm bg-red-500 hover:bg-red-600 px-3 py-1 rounded-md transition"
                            >
                                Выйти
                            </button>
                        </div>
                    ) : (
                        <>
                            <Link 
                                className="bg-oneWinBlue-400 px-4 py-1 rounded-sm hover:bg-oneWinBlue-300 duration-200" 
                                to={"/login"}
                            >
                                Войти
                            </Link>
                            <Link 
                                className="bg-oneWinBrandBlue px-4 py-1 rounded-sm hover:bg-oneWinBrandBlue-600 duration-200" 
                                to={"/registration"}
                            >
                                Регистрация
                            </Link>
                        </>
                    )}
                </div>
            </div>
        </header>
    )
})

export default Header;