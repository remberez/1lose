import { Link } from "react-router-dom";
import Button from "../UI/Button";
import girslBanner from "../assets/girls-banner.png";

const MainBanner = () => {
    return (
        <section className="bg-gradient-to-br from-oneWinBlue-500 to-oneWinBrandBlue-700 text-white pt-5">
            <div className="container flex justify-between items-center px-16">
                <div>
                    <h2 className="text-5xl font-bold mb-4">
                        Безусловный фрибет<br/>
                        до 15 000 ₽
                    </h2>
                    <p className="text-xl mb-6">
                        Нужно только зарегистрироваться
                    </p>
                    <Button>
                        <Link to={"/registration"}>Зарегистрироваться</Link>
                    </Button>
                </div>
                <div>
                    <img 
                        src={girslBanner} 
                        alt="Баннер"
                        width={500}
                    />
                </div>
            </div>
        </section>
    )
}

export default MainBanner;