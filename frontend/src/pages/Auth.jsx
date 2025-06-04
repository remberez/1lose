import { useState } from 'react';
import { observer } from 'mobx-react-lite';
import { userStore } from '../stores/user';
import { useNavigate } from 'react-router-dom';
import Input from '../components/ui/Input';
import Button from '../components/ui/Button';

const AuthPage = observer(() => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      await userStore.login({ username, password });
      navigate('/');
    } catch (e) {
      // Ошибка уже в userStore.error
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-[60vh]">
      <form onSubmit={handleSubmit} className="bg-blue-900 rounded-2xl p-8 w-full max-w-md shadow-xl flex flex-col gap-6">
        <h2 className="text-2xl font-bold text-center mb-2">Вход в аккаунт</h2>
        <Input
          label="Email"
          type="email"
          value={username}
          onChange={e => setUsername(e.target.value)}
          required
        />
        <Input
          label="Пароль"
          type="password"
          value={password}
          onChange={e => setPassword(e.target.value)}
          required
        />
        {userStore.error && <div className="text-red-400 text-center text-sm">{userStore.error}</div>}
        <Button type="submit" loading={loading} className="w-full">Войти</Button>
        <div className="text-center mt-2">
          <a href="/register" className="text-blue-300 hover:underline text-sm">Нет аккаунта? Зарегистрироваться</a>
        </div>
      </form>
    </div>
  );
});

export default AuthPage;
