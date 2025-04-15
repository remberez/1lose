import logo from "../assets/logo.png";

const Footer = () => {
    return (
        <footer className="flex items-center justify-center bg-oneWinBlue py-5">
            <img 
                src={logo} 
                alt="Логотип 1lose"
                width={100}
                height={20} 
            />
        </footer>
    )
}

export default Footer;