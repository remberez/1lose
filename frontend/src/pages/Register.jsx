import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import { observer } from 'mobx-react-lite';
import { userStore } from '../stores/user';
import { useNavigate } from 'react-router-dom';
import Button from '../components/ui/Button';

const RegisterSchema = Yup.object().shape({
  email: Yup.string().email('Некорректный email').required('Обязательное поле'),
  password: Yup.string().min(6, 'Минимум 6 символов').required('Обязательное поле'),
});

const RegisterPage = observer(() => {
  const navigate = useNavigate();

  return (
    <div className="flex flex-col items-center justify-center min-h-[60vh]">
      <Formik
        initialValues={{ email: '', password: '', username: '' }}
        validationSchema={RegisterSchema}
        onSubmit={async (values, { setSubmitting, setErrors }) => {
          try {
            await userStore.register(values);
            navigate('/auth');
          } catch (e) {
            setErrors({ email: userStore.error || 'Ошибка регистрации' });
          } finally {
            setSubmitting(false);
          }
        }}
      >
        {({ isSubmitting }) => (
          <Form className="bg-blue-900 rounded-2xl p-8 w-full max-w-md shadow-xl flex flex-col gap-6">
            <h2 className="text-2xl font-bold text-center mb-2">Регистрация</h2>
            <label className="flex flex-col gap-1 text-white">
              <span className="text-sm font-medium mb-1">Email</span>
              <Field name="email" type="email" className="px-4 py-2 rounded-lg bg-blue-800 text-white border border-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-400 transition-all" />
              <ErrorMessage name="email" component="div" className="text-red-400 text-xs mt-1" />
            </label>
            <label className="flex flex-col gap-1 text-white">
              <span className="text-sm font-medium mb-1">Пароль</span>
              <Field name="password" type="password" className="px-4 py-2 rounded-lg bg-blue-800 text-white border border-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-400 transition-all" />
              <ErrorMessage name="password" component="div" className="text-red-400 text-xs mt-1" />
            </label>
            <Button type="submit" loading={isSubmitting} className="w-full">Зарегистрироваться</Button>
          </Form>
        )}
      </Formik>
    </div>
  );
});

export default RegisterPage;
