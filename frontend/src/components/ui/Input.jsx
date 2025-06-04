const Input = ({ label, ...props }) => (
  <label className="flex flex-col gap-1 text-white">
    <span className="text-sm font-medium mb-1">{label}</span>
    <input
      className="px-4 py-2 rounded-lg bg-blue-800 text-white border border-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-400 transition-all"
      {...props}
    />
  </label>
);

export default Input;
