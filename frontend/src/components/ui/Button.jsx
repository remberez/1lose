// src/components/ui/Button.jsx
const Button = ({ children, loading, className = '', ...props }) => (
  <button
    className={`bg-blue-600 hover:bg-blue-700 text-white font-semibold px-6 py-2 rounded-lg text-base transition-colors disabled:opacity-60 disabled:cursor-not-allowed ${className}`}
    disabled={loading}
    {...props}
  >
    {loading ? 'Загрузка...' : children}
  </button>
);

export default Button;
