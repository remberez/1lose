import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";
import userService from "../services/userService";

const validationSchema = Yup.object({
  email: Yup.string()
    .email("Неверный формат email")
    .required("Email обязателен"),
  balance: Yup.number()
    .typeError("Баланс должен быть числом")
    .required("Баланс обязателен"),
  role_code: Yup.string()
    .oneOf(["admin", "user", "moderator"], "Неверная роль")
    .required("Роль обязательна"),
  is_active: Yup.boolean(),
});

const UserEditPage = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [initialValues, setInitialValues] = useState(null);

  useEffect(() => {
    userService.getUserById(id).then((user) => {
      setInitialValues({
        email: user.email,
        balance: user.balance,
        is_active: user.is_active,
        role_code: user.role_code,
      });
    });
  }, [id]);

  if (!initialValues) {
    return <div className="text-oneWinBlue-500">Загрузка...</div>;
  }

  const handleSubmit = async (values) => {
    await userService.updateUser(id, values);
    navigate("/admin/users");
  };

  return (
    <div>
      <h1 className="text-2xl font-bold mb-6 text-oneWinBlue-500">Редактирование пользователя</h1>
      <Formik
        initialValues={initialValues}
        validationSchema={validationSchema}
        onSubmit={handleSubmit}
      >
        {({ values }) => (
          <Form className="space-y-4 max-w-lg">
            <div>
              <label className="block text-oneWinBlue-400 mb-1">Email</label>
              <Field
                name="email"
                type="email"
                className="w-full px-4 py-2 border rounded-xl focus:outline-none focus:ring-2 focus:ring-oneWinBrandBlue-500"
              />
              <ErrorMessage
                name="email"
                component="div"
                className="text-red-500 text-sm mt-1"
              />
            </div>

            <div>
              <label className="block text-oneWinBlue-400 mb-1">Баланс</label>
              <Field
                name="balance"
                type="text"
                className="w-full px-4 py-2 border rounded-xl focus:outline-none focus:ring-2 focus:ring-oneWinBrandBlue-500"
              />
              <ErrorMessage
                name="balance"
                component="div"
                className="text-red-500 text-sm mt-1"
              />
            </div>

            <div>
              <label className="block text-oneWinBlue-400 mb-1">Роль</label>
              <Field
                name="role_code"
                as="select"
                className="w-full px-4 py-2 border rounded-xl focus:outline-none focus:ring-2 focus:ring-oneWinBrandBlue-500"
              >
                <option value="">Выберите роль</option>
                <option value="admin">Админ</option>
                <option value="user">Пользователь</option>
                <option value="moderator">Модератор</option>
              </Field>
              <ErrorMessage
                name="role_code"
                component="div"
                className="text-red-500 text-sm mt-1"
              />
            </div>

            <div className="flex items-center space-x-2">
              <Field
                name="is_active"
                type="checkbox"
                className="w-4 h-4"
              />
              <label className="text-oneWinBlue-400">Активен</label>
            </div>

            <button
              type="submit"
              className="bg-oneWinBrandBlue-500 hover:bg-oneWinBrandBlue-600 text-white font-semibold py-2 px-6 rounded-xl shadow"
            >
              Сохранить
            </button>
          </Form>
        )}
      </Formik>
    </div>
  );
};

export default UserEditPage;
