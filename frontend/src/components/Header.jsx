import { Link } from "react-router-dom";
import logo from "../assets/logo.png";

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


const Header = () => {
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
                <div className="flex gap-x-4 h-full text-sm">
                    <Link className="bg-oneWinBlue-400 px-4 rounded-sm hover:bg-oneWinBlue-300 duration-200" to={"/login"}>
                        Войти
                    </Link>
                    <Link className="bg-oneWinBrandBlue px-4 rounded-sm hover:bg-oneWinBrandBlue-600 duration-200" to={"/registration"}>
                        Регистрация
                    </Link>
                </div>
            </div>
        </header>
    )
}

export default Header;