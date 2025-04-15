const Button = ({ children, onClick, type = "button", className = "" }) => {
    return (
      <button
        type={type}
        onClick={onClick}
        className={`px-6 py-2 rounded-lg font-medium text-white bg-oneWinBrandBlue hover:bg-oneWinBrandBlue-600 transition-colors duration-200 ${className}`}
      >
        {children}
      </button>
    );
  };
  
  export default Button;
  